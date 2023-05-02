
                                ##### The Approach #####
"""
            In here we are looping from the year+1 until it finds a number == set(number).
            Because it will take a lot of complexity and memory due to generating many numbers that satisfies the criteria 
            and we only need one number, I used the generator one time which generates a number 
            each time i call it. 
                                
"""

##################################################################################################
#The Code#   

num=int(input())
ans=(i for i in range(num+1,10000) if len(str(i))==len(set(str(i))))
print(next(ans))