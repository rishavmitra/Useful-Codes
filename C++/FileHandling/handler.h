#include<fstream>
#include<string>
#include<iostream>
#include<vector>
#include<unordered_map>

std::vector<std::string> opening(){
    char rdata[100];
    std::unordered_map<std::string,int> matcher;
    std::fstream fout;
    std::vector<std::string> data;

    fout.open("files/1.txt");
    fout>>rdata;

    while(fout){
        matcher[rdata]++;
        if(matcher[rdata]>1){
            matcher[rdata]++;
        }
        else
        {
            data.push_back(rdata);
        }
        fout>>rdata;
    }

    return data;
    fout.close();
}