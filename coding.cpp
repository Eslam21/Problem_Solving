#include<bits/stdc++.h>
using namespace std;
#include <string>

long long gcd(long a, long b)
{
    if (b==0)return a;
    return gcd(b, a % b);   
}

vector<long long> divisors(long long num){

set <long long>numdiv;
for (int i=1;i<=sqrt(25);i++)
{
  if (num%i==0){

    // cout<<i<<endl;
   
    numdiv.insert(num/i);
    numdiv.insert(i);

  } 
 
}
vector<long long> v(numdiv.begin(), numdiv.end());
 return v;
}

int main(){
//                                      ---My Approach---     
/*
      
*/      
 

long long x=21;
long long y=7;

vector<long long> abdo=divisors(x);
vector<long long> ginger=divisors(y);


for(auto n:ginger){
  cout<<n<<" ";
} 



  return 0;
}


