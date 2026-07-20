def maxi(arr):
    maxi=arr[0]
    for i in arr:
        if i>maxi:
            maxi=i
    return maxi
print(maxi((12,34,54,2,456,78,65,7)))