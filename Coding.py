                                ##### The Approach #####
"""
             
                                
"""

##################################################################################################
#The Code#   
import itertools
def check_lucky(x):
    x=str(x)
    lucky=True
    for i in x:
        if i != '4' and i != '7':
            lucky=False
            break
            
        else:
         continue
    
    return lucky
 
def generate_lucky():
   lucky=[]
 
   for x in range(1,4):
    for i in itertools.product(['4', '7'],repeat=x):
        lucky.append(int(''.join(i)))
   return lucky
 
num=int(input())
 
if check_lucky(num)==True:
    print('YES')
else:
    for i in generate_lucky():
        if num%i==0:
            print("YES")
            break
    else:
        print("NO")  