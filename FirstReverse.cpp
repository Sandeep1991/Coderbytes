#include <iostream>
using namespace std;

string FirstReverse(string str) { 

  // code goes here  
  string rstr;
	
	// loop through characters in str
	for (int i = 0; i < str.size(); ++i) {
		// add characters to the front of rstr
		rstr = str[i] + rstr;
	}
	return rstr;
}

  
int main() { 
  
  // keep this function call here
  cout << FirstReverse(gets(stdin));
  return 0;
    
}           
