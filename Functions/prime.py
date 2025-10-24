def primeNum(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return "Not a prime number"
            
            else:
                return "Prime number"
            
    else:
        return "Not a prime number"
    

num=int(input("Enter a number: "))
print(primeNum(num))