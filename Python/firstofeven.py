def first_5_even(n):
    count=0
    total=0
    for i in range(2,n+1,2):
        total+=i
        count+=1
        if count==5:
            break;
    return total
print(first_5_even(20))
        
        
#count
def count_even(n):
    count=0
    
    for i in range(2,n+1,2):
        count+=1
    return count
print(count_even(20))