def solution(arr:list):
    temp_arr=[]
    cnt=-1
    for i in range(0,len(arr)):
        if i%2==0:
            temp_arr.append(arr[i//2])       
        else:
            temp_arr.append(arr[cnt])
            cnt-=1
            
    if temp_arr==sorted(temp_arr) and len(set(temp_arr))==len(temp_arr):
        return True

    else:
        return False    
