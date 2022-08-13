#include<bits/stdc++.h>
using namespace std;

int main(){
//                                      ---My Approach---     
/*
        The idea: There is that we have n × m meters shape and we want to put in it a×a flagstones.
        The question: What is the least number of flagstones needed to pave the Square? knowing that
        It's allowed to cover the surface larger than the Theatre Square.

        The code Idea:
        Assuming we have a 6×6 theatre and a 4×4 flagstones,

        1- we have 6m width and we want to see how many 4m width flagstones it the 6m can handle 
        so we divide 6/4=1.5 flagstones and since it is allowed to cover surface > theater we round up to become 2 flagstones

        2- we have 6m height and we want to see how many 4m height flagstones the 6m can handle 
        so we divide 6/4=1.5 flagstones and since it is allowed to cover surface > theater we round up to become 2 flagstones

        3-since it can handle 2 flagstones in the 4m width and 2 in the 4m height. Then it can contain 2*2=4 flagstones 
*/      
 


 long long h,w,x,y,res;
 double s;
 cin>>h>>w>>s;
 x=ceil(h/s);
 y=ceil(w/s);

 res=x*y;
 cout<<res;

  return 0;
}


