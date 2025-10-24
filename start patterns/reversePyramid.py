n=5
for i in range(n,0,-1):
    spaces=n-i
    for j in range(spaces):
        print(" ",end=" ")

    stars=2*i-1
    for j in range(stars):
        print("*",end=" ")

    print()