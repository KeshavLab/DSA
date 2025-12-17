n=5
# for rows
for i in range(1,n):

    #  for spaces
    spaces=n-i
    for j in range(spaces):
        print(" ",end=" ")

    # for stars
    for j in range(i):
        print("*",end=" ")

    print()    

 