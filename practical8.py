n=int(input("enter a number :"))

for i in range(1,n+1):

    # spaces
    spaces=n-i
    for j in range (spaces):
        print(" ",end=" ")

    # stars
    stars=n
    for j in range(stars):
        print("*",end=" ")

    print()