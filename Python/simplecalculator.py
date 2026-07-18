x=int(input("enter the first number"))
y=int(input("enter the second number"))
c=input("enter the operator")
if c=="+":
    print(x+y)
elif c=="-":
    print(x-y)
elif c=="*":
    print(x*y)
elif c=="/":
    if y==0:
        print("can not diivide by zero")
    else:
        print(x/y)
elif c=="%":
    print(x%y)
else:
    print("enter the valid oprator or number")
    