from lowbalance import*

class Account:
    def __init__(self, acno, name, type, balance):
        self.acno=acno
        self.name=name
        self.type=type
        self.balance=balance

    def withdraw(self,amount):
        if(self.balance<amount):
            raise Lowbalance("deposite money")
        else:
            self.balance=self.balance-amount
        return self.balance

emp=Account("1234","naveen","savings",500)
print(emp.withdraw(100))
