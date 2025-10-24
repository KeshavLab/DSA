def oddEven(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
    
num=int(input("enter a number: "))
print(oddEven(num))