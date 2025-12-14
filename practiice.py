n=int(input("enter a number :"))
count=0
while n>0:
    digit=n%10
    count=digit+count
    n=n//10


print(count)
