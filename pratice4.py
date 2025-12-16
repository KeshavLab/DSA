# count digits

n=int(input("enter a number :"))


count=0
original_n=n
while n>0:
    digit=n%10
    count =digit +count
    n=n//10

print(f"the number of digits in {original_n} is {count}")