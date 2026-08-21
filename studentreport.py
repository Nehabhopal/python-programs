class Student:
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
        self.__marks={}  #encapuslation

    def get_marks(self):
        return self.__marks

    def addmarks(self,subject,marks):
        self.__marks[subject]=marks

    def calculate_average(self):
        total=0
        for mark in self.__marks.values():
            total += mark
        average = total/len(self.__marks)
        return average

    def is_passed(self,marks):
        if not self.__marks:
            return False
        has_passed = all(marks>=35 for marks in self.__marks.values())
        if has_passed:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has failed")

    def calculate_grade(self):
        percentage = self.calculate_average()*100
        if percentage>=90:
            print("A")
        elif percentage>=85:
            print("B")
        else:
            print("C")

class ReportCard:
    @staticmethod
    def generate(student:Student):
        student_marks=student.get_marks()
        print(f"\nName: {student.name}\t Roll No.{student.roll_no}")
        print("------Marks------")
        for subject,marks in student_marks.items():
            print(f"{subject}-{marks}")
        print("------------")
        print(f"Average:{student.calculate_average()}")
        student.is_passed(student_marks)
        student.calculate_grade()

a = Student(1,"Neha")
a.addmarks("maths",95)
a.addmarks("science",34)

ReportCard.generate(a)
    