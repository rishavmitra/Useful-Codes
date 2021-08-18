#include<bits/stdc++.h>
using namespace std;

int main()
{
   string s;
   getline(cin,s);

   //creating a stream ss from s
   stringstream ss(s);

   int temp_int;
   string temp_str;

   //Unless ss reaches the end of the file
   //it check if each word can be converted to int
   while(!ss.eof()){
        ss>>temp_str;
    if(stringstream(temp_str)>>temp_int)
    {
        cout<<temp_int<<" ";
    }
   }
}
//Referenced from tutorialspoint.com
