# 0 0 0 0 0
# 0 0 0 0 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# Middle is [3,3]
# [3,3]-[2,5]---->|1,2|--->1+2=3


matrix=[]
for i in range(0,5):
  X=list(map(int,input().split()))
  matrix.append(X)

for i in range(0,len(matrix)):
    for j in range(0,len(matrix)):
       if matrix[i][j]==1:
           
           rowdiff=abs(3-(i+1))
           coldiff=abs(3-(j+1))
           print(rowdiff+coldiff)