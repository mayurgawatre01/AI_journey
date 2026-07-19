def searching_target(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    else:
        return -1
print(searching_target([12,23,444,33,23],444))



