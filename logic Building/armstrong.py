num=int(input("enter a number :"))

n=len(str(num))
sum=0
for digit in str(num):
    sum +=int(digit)**n


if sum==num:
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")

