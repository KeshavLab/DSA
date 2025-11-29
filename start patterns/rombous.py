n=int(input("enter your number :"))
for i in range(1,n+1):
    spaces=n-i
    for j in range(spaces):
        print(" ",end=" ")

    for j in range(n):
        print("*",end=" ")


    print()