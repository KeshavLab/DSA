n=5
for i in range(1,n+1):
    spaces=n-i
    for j in range(spaces):
        print(" ",end=" ")

    stars=2*i-1
    for j in range(stars):
        print("*",end=" ")

    print()