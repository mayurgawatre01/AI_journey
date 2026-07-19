def reverse_list(arr):
    arr.reverse()
    return arr
print(reverse_list([12,2,3,34,4]))


def rev(arr):
    result=[]
    for i in range(len(arr)-1,-1,-1):
        result.append(arr[i])
    return result
print(rev([12,13,14,15,16,17]))



arr=[90,80,70,60]
arr.reverse()
print(arr)


mayur=[78,79,80]
print(list(reversed(mayur)))

chachi=[12,13,14,15]
x=arr[::-1]

print(x)