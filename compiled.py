from os import system as cmd
from sys import argv
from re import sub, findall, escape

class Parser:
    def __init__(self, **kwargs):
        cmd("clear")
        for key in kwargs.keys():
            self.__setattr__(key, kwargs[key])

    def read(self):
        with open(self.file+".MAD", "r") as file:
            content = file.read()
        self.file_content = content.replace("\n\n","\n")
        return content

    def unescape(self):
        replacements = {
            "\-":  "-",
            "\[":  "[",
            "\]":  "]",
            "\\":  "\\",
            "\ ":  " ",
            "\^":  "^",
            "\(":  "(",
            "\)":  ")",
            "\$":  "$",
            "\*":  "*",
            "\.":  "."
        }
        for i in replacements.keys():
            self.file_content = self.file_content.replace(i, replacements[i])

    def parse(self):
        for exp in self.regex_replace:
            _format, _search, _replace = exp
            temp_find = findall(_search, self.file_content)
            for find in temp_find:
                find = escape(find)
                self.file_content = sub(escape(_format).replace("\{x\}", find), _replace.replace("{x}", find), self.file_content)

        if self.semicolons == True:
            self.file_content = sub("(?<![\{\;\@\}])\n",";\n",self.file_content).replace("@","")

    def write(self):
        with open("/home/manjaro/.cache/muck/"+self.outfile, "w") as file:
            file.write(self.file_content)
        cmd(f"astyle --style=allman ~/.cache/muck/{self.outfile}")
    
    def run(self):
        cmd(f"g++ ~/.cache/muck/{self.outfile}.c++ -I /home/manjaro/Languages/MAD/ -o {self.outfile}")
        if self.clear_before_run == True: cmd("clear")
        cmd(f"./{self.outfile}")

def main():
    args = argv
    args.pop(0)
    parser = Parser(
        file = args[0],
        outfile = args[1],
        regex_replace = {
            ("$$","$$","types::"),
            ("use({x})", "(?<=use\().+?(?=\))", "#include \"{x}.h\"@\nusing namespace {x};"),
            ("for {x}", "for (.*)", "for (auto {x}){"),
            ("if {x}", "if (.*)", "if ({x}){"),
            ("while {x}", "if (.*)", "while ({x}){"),
            (" <- ","\ \<\-\ "," : "),
            ("def {x}", "def (.*)", "auto {x}{"),
            ("let {x}", "let (.*)","auto {x}"),
            ("end\n", "end\n", "}\n"),
            ("## {x}", "## (.*)", "// {x}")
        },
        semicolons = True,
        clear_before_run = False
    )
    parser.read()
    parser.parse()
    parser.unescape()
    parser.write()
    parser.run()

if __name__ ==  "__main__":
    main()
