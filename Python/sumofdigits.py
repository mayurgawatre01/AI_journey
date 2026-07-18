def sumofdigits(n):
    count=0
    while n >0:
        ld=n%10
        count+=ld
        n=n//10
    return count
print(sumofdigits(1234))
        
    