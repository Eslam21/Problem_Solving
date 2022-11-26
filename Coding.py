                                ##### The Approach #####
"""
             
                                
"""

##################################################################################################
#The Code#   
num = int(input())
magnet= [input() for i in range(num)]
ans=[ 1  for i in range(0,num-1) if magnet[i][1] != magnet[i+1][1]  ]

print(len(ans)+1)        