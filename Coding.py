                                ##### The Approach #####
"""
             
                                
"""

##################################################################################################
#The Code#   
# import numpy as np
num_shops=5
bottle_price=[3,10,8,6,11]
num_days=4
coins=[1,10,3,11]
bottle_price.sort()
for coin in  coins:
    
    left = 0
    right = len(bottle_price) - 1
 
    count = 0
 
    while (left <= right):
        mid = int((right + left) / 2)
 
        # Check if middle element is
        # less than or equal to key
        if (bottle_price[mid] <= coin):
 
            # At least (mid + 1) elements are there
            # whose values are less than
            # or equal to key
            count = mid + 1
            left = mid + 1
         
        # If key is smaller, ignore right half
        else:
            right = mid - 1
     
    print(count)
    
              
         
        
  
  

