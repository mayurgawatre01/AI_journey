def productofdigits(n):
    product=1
    while n >0:
        
        last_digit=n%10
        product*=last_digit
        n=n//10
    return product
print(productofdigits(123))
        