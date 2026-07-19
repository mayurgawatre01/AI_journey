def is_sorted(arr): 
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    else:
        return True
        

print(is_sorted([12,21,23,24,51]))