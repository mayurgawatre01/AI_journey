def sum_of_odd(n):
    total=0
    for i in range(1,n+1,2):
        total=total+i
    return total
print(sum_of_odd(5))