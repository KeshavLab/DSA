def factorialNUm(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorialNUm(num-1)
    

print(factorialNUm(5))
