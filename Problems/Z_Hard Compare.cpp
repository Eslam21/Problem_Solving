#include<bits/stdc++.h>
using namespace std;

int main(){
//                                      ---My Approach---     
/*
          solution would be to just compute a^{b} and c^{d} and compare them. 
          But a,b,c and d can be large enough that x^y can not be stored even in long long int.
          Efficient approach is to use logarithm(natural logarithm). If we take log(a^b) and log(c^d), the problem reduces to comparing a*log(b) and c*log(d). 
          Note that 700^{10} = 2.82475249×10^{28} and 10*log(700)= 65.5108033504 so this will reduce a lot of memory
*/       
 
long double A,B,C,D;
cin>>A>>B>>C>>D;
if (B*log10(A) > D*log10(C) )
{cout<<"YES";}
else{cout<<"NO";}


  return 0;
}


