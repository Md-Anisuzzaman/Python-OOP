class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 2000

    def GET_BALANCE(self):
        return self.balance

    def DEPOSIT(self, amount):
        if amount > 0:
            self.balance += amount

    def WITHDRAW(self, amount):
        if amount < self.min_withdraw:
            print(f"{self.name} you can't withdraw this min amount")
            print("\n")
        elif amount > self.max_withdraw:
            print(f"{self.name} you can't withdraw this max ammount")
            print("\n")
        else:
            self.balance -= amount
            print(f'{self.name} take your money {amount} TK')
            print(
                f'{self.name} the remaining money in your account is {self.GET_BALANCE()}')
            print("\n")


juel = Bank("Juel", 5000)
juel.DEPOSIT(600)
juel.WITHDRAW(2000)


Rubel = Bank("Rubel", 10000)
Rubel.DEPOSIT(5000)
Rubel.WITHDRAW(1500)
