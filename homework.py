# 1-program print your name
'''print("neha")

# 2-p perform a arithmatic operations on two number
a,b=10,20
print(a+b)
print(a*b)
print(a/b)
print(a%b)
print(a-b)

# 3-p swap the number
a,b=10,20

print(f"a:{a},b:{b}")
b,a=a,b

print(f"a:{a},b:{b}")

# 4-p string manipulations

user=input("enter a string:")
print("uppercase:",user.upper())
print("lowercase:",user.lower())
print("underscore", user.replace("","_"))
print("whitespace", user.strip())

#5-p 
string=input()
print(len(string.replace("","")))

# 6-p
print("hello\n\tthis is neha\nthe backspacing \\")

# 7-p 
a=int(input("enter a first number:"))
b=int(input("enter a second number:"))

print(a>10 and b>10)
print(a<5 or b<5)
print(not(a>5))

# 8-p
age=int(input("enter your age:"))
if age>=18:
    print("you are an adult")
else: 
    print("you are a minor")

# 9-p membership operator
string=input("enter a string:")
print("a" in string)
print("python" not in string)

# 10-p bitwise operator

a=int(input("enter a number:"))
b=int(input("enter a number:"))
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b>>1)

# 11-p
l=[1,2,3,4,5]
l.append(6)
print(l)
l.insert(1,"4")
print(l)

# 12-p
l=[23,24,5,7,8]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

print(l[::-1])

# 13-p tuple operation
t1=(1,2,3,4,5)
t2=(6,4,5,4,3)
print(t1+t2)
print(t1[1:3])

# 14-p
foods=["idili","vada","dosa"]

u_foods=[item.upper() for item in foods]
print(u_foods)

#15-p
l={
    "name":"neha",
    "age": 12,
}

l=[num**2 for num in range(1,11)]
print(l)

l=[
    {
        "name":"neha",
        "marks": 32
    },
    {
        "name":"varun",
        "marks": 65
    },
    {
        "name":"akhila",
        "marks": 75
    }
]

for student in l:
    print(student["name"],"-",student["marks"])

rows = int(input("enter the number of rows:"))
columns=int(input("enter the number of columns:"))

matrix = []

for i in range(rows):
    row=[]
    for j in range(columns):
        x=int(input("enter the element:"))
        row.append(x)
    matrix.append(row)

print(matrix)

def tables(num):
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")

tables(5)

def func(num):
    return int((str(num))*5)

a= func(34)
b=100

c= a + b
print(c)

def greet():
    print("Hello!! i have a nice day")

greet()
name=input("enter a name:")
def greet_user():
    print("Hello!, This is",name)

greet_user()

def add_numbers(a,b):
    sum=0
    sum=a+b
    print(sum)

add_numbers(2,6)

def student_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")

student_info(name="neha",age=15,course="be")

add = lambda a,b : a+b
print(add(1,2))

def greet():
    print("Hello!!")
    greet()
greet()

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(6))

a=lambda a,b : a*b
print(a(1,8))

def recursive(n):
    if n==0:
        return 0
    return n + recursive(n-1)

print(recursive(5))'''

