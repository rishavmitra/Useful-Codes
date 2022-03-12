#include<bits/stdc++.h>
using namespace std;
#define ll long long

ll fib(int n, unordered_map<ll,ll> &mp){
  if(mp.count(n)>0)
    return mp[n];
  if(n<=2)
    return 1;
  mp[n]= fib(n-1, mp)+fib(n-2, mp);
  return mp[n];
}


int main()
{
  int n;
  cin>>n;
  unordered_map<ll,ll> m;
  cout<<fib(n,m)<<endl;
}