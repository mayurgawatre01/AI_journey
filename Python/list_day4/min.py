def list_min(arr):
    min=arr[0]
    for num in arr:
        if min>num:
            min=num
        
    return min
print(list_min([12,23,345,5,67,899,88]))




arr2=[12,3233,342,12,2,90,89,78]
print(min(arr2))
