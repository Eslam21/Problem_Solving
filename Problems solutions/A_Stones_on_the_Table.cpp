#include<bits/stdc++.h>
using namespace std;

int main(){

 /*
   My approach is to loop on the string and check if stone i is the same as stone i+1.
   If a stone equals any next stone then we need to remove one of them so add +1 to the answer.
   If the there are no duplicate neighboring then the ans is 0.
   
 */
  
   int len;
   int ans=0;
   string stone;
   cin>>len;
   cin>>stone;

   for(int i=0;i<len-1;i++){

        if (stone[i]==stone[i+1]){
                ans++;

        }
    }    

            cout<<ans<<endl;
    


  return 0;
}


