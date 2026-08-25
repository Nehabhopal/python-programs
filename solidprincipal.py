'''class Book:
    def __init__(self,pages):
        self.rate=self.determine_rate(pages)
        self.pages=pages

    def determine_rate(self,pages):
        if pages==100:
            return "50rs"
        elif pages==200:
            return "100rs"

class BookDetails(Book):
    @staticmethod
    def details(self):
        print(f"For{self.pages}pages the book rate is{self.rate}")

b=Book(200)

BookDetails.details(b)'''

'''try:
    age=int(input("Enter your age:"))
    if age >=0:
        years=100-age
        if years>0:
            print(f"you will be 100 years old in {years} years.")
        elif years==0:
            print("you are already 100 years old.")
        else:
            print("invalid input..age cannot be negative")

except Exception as e:
    print(f"exception:{e}")
'''
'''try:
    a=int(input("a:"))
    b=int(input("b:"))
    print(a/b)
except ZeroDivisionError:
    print("you cannot divide by one")
except ValueError:
    print("enter valid input")
    '''
'''l=["neha","varun","akhila"]
file=open("friends.txt","w")
for name in l:
    file.write(name + "\n")'''

