def swapNUm(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

a=int(input("enter first number: "))
b=int(input("enter second number: "))
a,b=swapNUm(a,b)
print("After swapping: ",a,b)