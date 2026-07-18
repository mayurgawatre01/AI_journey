def count_num(n):
    num=n
    count=0
    while num>0:
        ld=num%10 
        count+=1
        num=num//10
    return count
    
print(count_num(12345))