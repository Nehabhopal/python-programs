'''lass Movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
    
    def display(self):
        print(f"{self.title} is movie title and its rating is {self.rating}")


s=Movie("24",5.6)
s.display()
    

class Employee:
    def __init__(self,name,designation,salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary

    def details(self):
        print(f"the name {self.name} and designation{self.designation},salary:${self.salary}")

n=Employee("neha","developer",5789)
s=Employee("summy","designer")
n.details()
s.details()

    
'''
'''class BankAccount:
    def __init__(self,__balance):
        self.__balance=balance

    def withdraw(self):
        print("f{self.__balance} is withdrawed")

ba=BankAccount(45000)
ba.withdraw()
print(ba)'''

'''
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def details(self):
        print(f"The mobile is a{self.brand} brand and its price is {self.price}rs")


m1=Mobile("iphone",100000)
m2=Mobile("samsanga",87398)

m1.details()
m2.details()'''


'''ss Shape:
    def calc_area(self):
        print("Area calculated")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def calc_area(self):
        print(f"area of ciecle:{(22/7)*self.radius*self.radius}")


class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def calc_area(self):
        print(f"area of rectangle:{self.l*self.b}")

c=Circle(5)
r=Rectangle(4,2)

c.calc_area()
r.calc_area()'''

'''class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,updated_balance):
        if updated_balance<0:
            print("Error")
            return
        self.__balance=updated_balance
s=BankAccount(5758)
s.get_balance()
s.set_balance(89909)
'''

'''
def menu():
    print(">>>banking system>>>>")
    print("1.check_balance\n2.deposit\n3.withdraw\n4.exit")
balance=0
while(True):
    for choice in {1,2,3}:
        choice=int(input("Enter your choice:"))
        
        if choice==1:
            print("Your balance:",balance)
        elif choice==2:
            amount = int(input("Enter a deposit here:"))
            balance += amount
            print("you depoisted",balance)
        elif choice==3:
            amount = int(input("Enter a whithdraw here:"))
            balance -= amount
    
        elif choice==4:
            print(exit)
            break
        else:
            print("invalid choice")'''
'''
def grocerystore():
    print("---Grocerystore----")
    print("1.Add items to their cart\n 2.Remove items\n 3.View the total price\n 4.exit")
cart={}
while(True):
    grocerystore()
    choice=int(input("Enter your choice:"))

    if choice==1:
        items=input("Enter a item:")
        price=float(input("Enter a price item:"))
        cart[items]=price
        print("total items in cart",cart)
    elif choice==2:
        items=input("Enter a item:")
        price=float(input("Enter a price item:"))
        del cart[items]
        print("total items in cart",cart)
    elif choice==3:
        total = sum(cart.values())
        print("The total price",total)
    elif choice==4:
        print("Exit")
        break
    else:
        print("invalid choice")'''

def eductionsystem():
    print("---eductional System---")
    print("1.add student details\n2.display student details\n3.exit")

while(True):
    eductionsystem()    
    choice=int(input("Enter a choice here:"))
    if choice==1:
        name=input("Enter a name here:")
        age=int(input("Enter a age here:"))
        dob=input("Enter a dob here:")
        
    elif choice==2:
        if name == " ":
            print("no student details available")
        else:
            print(f"{name} is a name and the age is{age} years also dob{dob}")

    elif choice==3:
        print("Exit")
        break
    else:
        print("Invalid choice")