#include<bits/stdc++.h>
using namespace std;

int main(){
//                                      ---My Approach---     
/*
      The idea is that if x1 is boy and x2 is girl then we swap and shift what we point at one step forward. 
      Anything else remains as it is. 
      We repeat those steps n times.
*/      
 
string line;
int n,siz;
cin>>siz>>n;
cin>>line;

while(n--){

  for (int i=0; i<siz-1;i++){

    if (line[i] == 'B' && line[i+1]=='G'){ 
      line[i]='G';
      line[i+1]='B';
      i++;
      }

    else {
      line[i]=line[i];

      }
  }

}

for (int i=0; i<line.size();i++){

    cout<<line[i];
              
  }
  return 0;
}


