# Reverssed array
n=int(input("enter the number do you want inside the array:"))
l=[]

for i in range(n):
    ele=int(input("enter element :"))
    l.append(ele)
print("my array:",l)

l.reverse()
print("reversed array:",l)