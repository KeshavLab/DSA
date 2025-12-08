class BankAccount:
    def __init__(self,acc_holder,balance):
        self.acc_holder=acc_holder
        self.__balance=balance

    def deposite(self,amount):
        if amount>0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")

    def withdraw(self,amount):
        if 0<amount <=self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount}. New balance is {self.__balance})")


    def getbalance(self):
        return self.__balance
    

acc1=BankAccount("john",1000)

acc1.deposite(500)
acc1.withdraw(200)

print(f"current balance is :{acc1.getbalance()}")