#include<bits/stdc++.h>
using namespace std;

int main()
{
    string A[3];
    string s;
    getline(cin,s);

    //Only removes the spaces

    /*stringstream ss(s);
    string word;
    while(ss>>word){
        cout<<word<<endl;
    }*/

    string word;
    string delimiter = ":";

    size_t pos =0;
    int i=0;
    //npos is the highest value of type size_t, mostly means the end of the string.
    while((pos = s.find(delimiter)) != string::npos)
    {
        word = s.substr(0,pos);
        cout<<word<<endl;
        //erasing the string from 0 to the position of the delimiter
        s.erase(0,pos+delimiter.length());
    }
    cout<<s<<endl;
}

//Referenced from StackOverflow
//User(Vincenzo Pii)- https://stackoverflow.com/users/528313/vincenzo-pii
