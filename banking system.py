class Account:
    def __init__(self,id,holder_name):
        self.id=id
        self.holder_name=holder_name
        self._balance=0         #encapusation

    def check_balance(self):
        print(f"Balance: {self._balance}")

    def deposit(self,amount):
        self._balance += amount
        print(f"Deposite successful.updated balance:{self._balance}")

    def withdraw(self,amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"withdrawed successful.updated balance:{self._balance}")
        else:
            print("Balance is less than ask")

class savingsaccount(Account):
    def calculate_interest(self):
        interest_rate = 0.04
        interest =self._balance * interest_rate
        print(f"interest:{interest}")

class CurrentAccount(Account):
    def withdraw(self, amount): #polymoriphism
        overdraft_limit=1000
        if self._balance + overdraft_limit >= amount:
            self._balance -= amount
            print(f"withdrawed successful.updated balance:{self._balance}")
        else:
            print("Balance is ask over")

class Bank:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__account={}

    def create_account(self,id,holder_name,type):
        if type=="savings":
            new_accounts=savingsaccount(id,holder_name)
        elif type=="Current":
            new_accounts=CurrentAccount(id,holder_name)
        else:
            return None
        self.__account[id] = new_accounts
        print("Account creation successful")
        return new_accounts

    def get_account(self,id):
        if id not in self.__account:
            print("Account not found!")
            return None
        else:
            account=self.__account[id]
            print(f"\nID: {account.id}\n holder name: {account.holder_name}")
            return account

sbi=Bank("State bank of india","raichur")

s1=sbi.create_account("1","neha","savings")
c1=sbi.create_account("2","varun","Current")
s1.deposit(1000)
c1.deposit(10)

s1.withdraw(2000)
c1.withdraw(104)

s1.calculate_interest()