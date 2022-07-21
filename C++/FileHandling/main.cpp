#include<iostream>
#include<stdlib.h>
#include"handler.h"
#include<vector>
using namespace std;

int main(){

    vector<string> data;
    data=opening();

    for(string iter:data)
    {
        cout<<iter<<endl;
    }
}