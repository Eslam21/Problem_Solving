#In this problem:
# 1-"It" always printed at last
# 2-If the number is odd then it is "I hate" so it will always be Hate at first
# 3-If the number is even then it is "I love"
# 4-"That" always printed if it is more than 1 emotion (n>1) and it is not the last word

Hate="I hate"
Love="I love"

n=int(input())
if n==1:
    print(Hate,end=" ")
else:    
    for i in range(1,n+1):
        if i%2==1:
            print(Hate,end=" ")
            
        if i%2==0:
            print(Love,end=" ")
        if i!=n:
            print("that",end=" ")
            
print("it") 