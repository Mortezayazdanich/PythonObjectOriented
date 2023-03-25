class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def __repr__(self) -> str:
        return 'User: %r' % (self.name)


class Bank(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('Not enough money')
        else:
            self.balance -= amount
            print(f"The balance has been updated: the new balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"The balance has been updated: the new balance is: ${self.balance}")
    
    def show_balance(self):
        print(self)
        print(f"The balance is: ${self.balance}")
