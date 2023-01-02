using namespace std;
#include <vector>
#include <string.h>

namespace mad
{
  template <class T>
  void print(T a, bool eol = true){
    switch (eol) {
      case false:
        cout << a;
        break;
      default:
        cout << a << "\n";
        break;
    }
  }

  auto range(int x) -> vector<int>
  {
    vector<int> vec;
    for (int i = 0; i < x; i++) {
      vec.push_back(i);
    }
    return vec;
  }

  string input(string text)
  {
    string inp = "";
    print(text, false);
    cin >> inp;
    string out(inp);
    return out;
  }
}
