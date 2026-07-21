def commom_ele(a,b):
    x=a.intersection(b)
    return x
print(commom_ele({10,2,3,4},{10,2,5,6}))
    
    
    
#optimized solution 
def common_elements(a, b):
    
    set_a = set(a)      # Fast lookup ke liye

    result = set()      # Answer store karega

    for num in b:       # Dusri list traverse karo

        if num in set_a:    # Common hai?
            result.add(num)

    return result
print(common_elements([10,20,30],[30,40,50]))