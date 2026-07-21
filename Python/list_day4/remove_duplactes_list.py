def rem_dup(arr):
    result=[]
    for num in arr:
        if num not in result:
            result.append(num)
    return result
print(rem_dup([12,12,13,14,14,15,15,16,17]))
            
            
            
            
