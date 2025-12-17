n=int(input("enter a number :"))

for i in range(1,n):

    # /spaces
    
    for j in range(n-i):
        print(" ",end=" ")

    # for stars
    stars=2*i-1
    for j in range(stars):
        print("*",end=" ")

    print()


for i in range(n,0,-1):

    # /spaces
    
    for j in range(n-i):
        print(" ",end=" ")

    # for stars
    stars=2*i-1
    for j in range(stars):
        print("*",end=" ")

    print()
