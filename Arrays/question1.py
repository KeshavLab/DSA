# find the largest and smallest number in array
n=int(input("enter the number of element you want inside the list:"))
l=[]
for i in range(n):
    ele=int(input("enter the element:"))
    l.append(ele)
print("my list=",l)

l.sort()
print("sorted list =",l)

minimum_number=l[0]
print("minimum number =",minimum_number)

maximum_number=l[-1]
print("largest number =",maximum_number)