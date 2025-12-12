def factorial(n):
    return 1 if n==0 else n*factorial(n-1)


num=int(input("enter a number :"))
result=factorial(num)
print(f"factorial of {num} is {result}")