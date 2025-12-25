class DigitalWallet:
    def __init__(self, pin):
        self.__pin=pin
        self.__balance=0
        self.__unlock=False
    def is_unlock(self,pin):
        if self.__pin==pin:
            self.__unlcok=True
        else:
            print("wrong PIN")

    def deposit(self,ammount):
        if self.__unlcok and ammount>0:
            self.__balance+=ammount
        else:
            print("please log in first or ammount is not valid")
    def withdraw(self, ammount):
        if self.__unlock and ammount<=self.__balance:
            self.__balance-=ammount
        else:
            print("please log in first or ammountt is low")
    def balanced_amount(self):
        if self.__unlock==False:
            print("please log in first")
        else:
            return self.__balance

account1= DigitalWallet("1234")
account1.is_unlock("1234")
account1.balanced_amount()
