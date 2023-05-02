                                ##### The Approach #####
                                
#Sum the x's,y's and z's. Check if all of them equal 0

#The Code#   

n=int(input())
x,y,z=0,0,0
for i in range(0,n):
    arr=list(map(int,input().split()))
    x,y,z=arr[0]+x, arr[1]+y, arr[2]+z 
print('NYOE S'[x==0 and y==0 and z==0::2])  # returns either True:0 or Flase:1 
print(['NO','YES'][x==y==z==0])  # returns either True:0 or Flase:1 