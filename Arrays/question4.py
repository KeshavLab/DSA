n=int(input("enter the number of elemet do you want in array:"))
l=[]

for i in range(n):
    ele=int(input("enter the element:"))
    l.append(ele)
print("my list:",l)

# l.sort()

# print("sorted list:",l)

if l==sorted(l):
    print("array is soorted")

else:
    print("array is not sorted")
