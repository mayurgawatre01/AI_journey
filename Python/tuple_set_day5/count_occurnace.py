def count_occurrences(t, target):
    count = 0
    for num in t:
        if num==target:
            count+=1
    return count
print(count_occurrences((1,2,2,3,4,4,5,5,6,6,6,6,10,10,1),6))


arr=(1,1,2,2,3,3,3,3,4,4,4,5,5)
print(arr.count(3))