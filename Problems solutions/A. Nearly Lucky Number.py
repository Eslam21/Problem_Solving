                                ##### The Approach #####
"""
             He wants to count the number of lucky numbers(4 and 7)
             If they equal a lucky number(even if the input is not a lucky number) then YES it is nearly lucky
             Else NO
                                
"""

##################################################################################################
#The Code#   

ans=[0  if num !='4' and num !='7' else 1 for num in str(input())] # It adds 1 to the list if the input is 4 or 7
# print(sum(ans))
print("NYOE S"[sum(ans)==7 or sum(ans) ==4 ::2]) # if the sum is 7 or 4 it is True(0) Else is False(1)
    
              
         
        
  
  

