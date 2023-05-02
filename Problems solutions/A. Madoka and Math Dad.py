
                                ##### The Approach #####
"""
    The question: Here's a number n- find a decimal number-sum of digits equals n-number cannot have zero or repetition between adjacent- output is largest value.
    
    Solving Idea: The idea is to make our number as large as possible so what combination of numbers would make it largest possible number ? it is grouping 1 and 2.
    For example 4 is 31 or 121, 9 is 3123 or 212121 and so on.
    So we have a number and we divide it by 3 to check how many 3 it can form in terms of '21'.
    For example 9//3=3 so it can form '21'*3 which equals 212121=9 .
    But we have problem, what if the number is 4 for example 4//3=1 = '21'. 
    So what we need to do is to check the reminder num%3 and we add what remains weather in front or behind the number according to what is the first digit 1 or 2.
    for Example 11//3= 3= '212121' which equals 9 so we have 2 remaining(9%3), we check if in the first digit has 2 then we put it in the last digit.          
                                
"""

##################################################################################################
#The Code#   

num=int(input())
for i in range(0,num):
    x=int(input())
    ans=list((x//3)*'21')
    
    if x==1:
        print(1)
        
    elif x==2:
        print(2)
    elif x%3==1:
        if ans[0]=='1':
            ans.append('1')
        else:
            ans.insert(0,'1')
    elif x%3==2:
        if ans[0]=='2':
            ans.append('2')
        else:
            ans.insert(0,'2')
               
            
    print(*ans,sep='')  