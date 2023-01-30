class CheckingAccount:
    def __init__(self, name, address, account_number, balance):
        self._balance = balance
        self.name = name
        self.address = address
        self.account_number = account_number

    def credit(self, amount):
        self._balance += amount

    def debit(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds on account")

    def return_balance(self):
        return self._balance

if __name__ == "__main__":
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    account_number = input("Enter your account number: ")
    balance = float(input("Enter your account balance: "))

    account = CheckingAccount(name, address, account_number, balance)

    print("Account balance:", account.return_balance())

    debit_amount = float(input("Enter debit amount: "))
    account.debit(debit_amount)
    print("Balance after debit:", account.return_balance())

    credit_amount = float(input("Enter credit amount: "))
    account.credit(credit_amount)
    print("Balance after credit:", account.return_balance())