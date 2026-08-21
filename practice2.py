'''seats = 8
while seats > 0:
    print("seats booked")
    seats -= 1
    print("available seats:",seats)
print("All seats are booked")'''

'''count=10
while count > 0:
    print(count)
    count -= 1

print("happy new year!")

bag=["red","yellow","green"]

for i in range(2,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")'''

'''for i in range(1,31): #multiples of 3
    if(i%3==0):
        print(i)'''
'''sum =0
for i in range(1,11):# sum of first 10 numbers
    i = i%10
    sum += i
    i=i/10
    print(sum)'''

'''string =input("enter your word:")
count = 0
for ch in string:
    if ch in "aeiouAEIOU":
        count +=1
print("number of vowels :",count)'''

'''student_marks = {"Anand": 85,"Geeths":78,"Kumar": 78}

for student,marks in student_marks.items():
    print(f"{student}---{marks}")'''

'''students=["chandan","darshan","narendra"]
marks=[25,90,78]

student_marks={}

for index,students in enumerate(students):
    student_marks[students]= marks[index]
print(student_marks)'''

'''names = ["neha","varun","akhila"]

d={name:len(name) for name in names}
print(d)'''

'''cp ={
    "bengaluru": 84,
    "mysuru":34,
    "hubbali": 8,
    "mangaluru":5
}

lc={city:value for city,value in cp.items() if value>60}
print(lc)'''

class Movie:
    def__init__(self,title,rating):
        self.title=title
        self.rating=rating
    
    def display(self):
        print(f"{self.title} is movie title and its rating is {self.rating}")


s=Movie("24",5.6)
s.display()
    


