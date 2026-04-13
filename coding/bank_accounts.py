class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, subtract):
        self.balance -= subtract
        return subtract

    def display_balance(self):
        print(self.balance)


franco_herrera = BankAccount('Franco', 'Herrera', 1000, 'Recurring', 52487, 100.00)
franco_herrera.deposit(96)
franco_herrera.withdraw(25)
franco_herrera.display_balance()