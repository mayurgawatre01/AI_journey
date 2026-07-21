def remove_duplicates(arr):
    result=[]
    for num in arr:
         if num not in result:
             result.append(num)
    return result
print(remove_duplicates([10,10,23,23,45,56,45,89,87]))



#optimized solution 


def opti(arr):
    seen=set()
    result=[]
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
print(opti([10,10,23,34,23,34,45,56]))