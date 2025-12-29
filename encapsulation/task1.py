class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
        self.__transaction_history= []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited ${amount}")
        else:
            print("Deposit amount must be greater than 0")
    def withdraw(self, ammount):
        if ammount<500:
            print("Minimum withdrawal amount is $500")
            return
        if ammount<=self.__balance:
            self.__balance -= ammount
            self.__transaction_history.append(f"Withdrew ${ammount}")
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self.__balance
    def get_transaction_history(self):
        return self.__transaction_history
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())
print("Transaction History:")
for transaction in account.get_transaction_history():
    print(transaction)
