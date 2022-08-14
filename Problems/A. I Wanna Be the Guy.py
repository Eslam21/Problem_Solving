
                                ##### The Approach #####
                                
#Make a set that takes the levels of x and y.
#Loop through the given levels
#If a level in the set doesn't exist then it will print 'Oh, my keyboard!'

#The Code

n=int(input())

X=list(map(int,input().split()))
Y=list(map(int,input().split()))

sett=set(X[1:]).union(Y[1:])

for i in range(1,n+1):
    if i in sett:
        ans=1
    else:
        ans=-1
        break
if ans ==1:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")    