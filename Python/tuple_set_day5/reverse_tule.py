def reverse_tuple(t):
    result=()
    for i in range(len(t)-1,-1,-1):
        result+=(t[i],)
    return result
   
print(reverse_tuple((1,2,3,4,5)))


arr=(1,2,3,4,5)
x=arr[::-1]
print(arr)