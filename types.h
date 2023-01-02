#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

namespace types
{

  class str
  {
  public:
    string val;
    template <class T>
    str(T a) 
    {
      val = a;
    }
    auto upper() -> string
    {
      string out = "";
      for (int i = 0; i < val.length(); i++) {
        out += toupper(val[i]);
      }
      return out;
    }
  };

  class num
  {
    public:
      float val;

      template <class T>
      num(T a) 
      {
        val = a;
      }

      void from_str(string s)
      {
        val = stof(s);
      }

      auto power(float n) -> float
      {
        return pow(val, n);
      }

      auto length() -> int
      {
        return (int) floor(log(val)/log(10))+1;
      }

      auto index(int n) -> float
      {
        int len = length();
        int eval = val - (int) floor(val) % (int) pow(10, len);
        return eval;
      }     
  };

}
