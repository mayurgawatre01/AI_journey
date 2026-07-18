def fibonacci(n):
    a=0
    b=1
    for i in range(2,n):
        next=a+b
        a=b
        b=next
    print(next)
fibonacci(6)
        