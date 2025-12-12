num=int(input ("enter a number :"))

original_num=num
n=len(str(num))

count=0
while num>0:
    digit=num%10
    count +=digit**n
    num=num//10


if count==original_num:
    print(f"number {original_num} is an armstrong number ")
else:
    print(f"number {original_num}is not armstrong number")