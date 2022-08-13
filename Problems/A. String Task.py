# to take input list 
# arr=list(map(int,input().split()))



myList = [value.lower() for value in str(input()) if value not in 'aeiouy' and value not in 'AEIOUY']
print('.',end='')
print(*myList,sep='.')        