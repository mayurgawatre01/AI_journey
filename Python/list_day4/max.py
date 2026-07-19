def list_max(arr):
    maxi=-900999999990909
    
    for i in arr:
        if i>maxi:
            maxi=i
        
    return maxi
        
    
print(list_max([12,33,4,5,67,55,7,23,212,23]))

arr2=[678,2,32,2,2,2,3,3,3,33334334,4,4,3]
print(max(arr2))