
n=5
for i in range(n,0,-1):

    #  for spaces
    spaces=n-i
    for j in range(spaces):
        print(" ",end=" ")

    # for stars
    for j in range(i):
        print("*",end=" ")

    print()  