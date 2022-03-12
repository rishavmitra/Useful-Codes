#include<bits/stdc++.h>
using namespace std;

long long gridTraveller(int m,int n, unordered_map<string,long long> &mp){
	string key = to_string(m)+','+to_string(n);
	
	if(mp.count(key)>0) return mp[key];
	
	if(m==1 && n==1)return 1;
	if(m==0 || n==0) return 0;

	mp[key]=gridTraveller(m-1,n,mp)+gridTraveller(m,n-1,mp);
	
	return mp[key];

}

int main(){
	int m,n;
	cin>>m>>n;
	unordered_map<string,long long> mp;
	cout<<gridTraveller(m,n,mp);
}