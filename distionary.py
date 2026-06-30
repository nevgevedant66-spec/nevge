"""class dis:
    def __init__(self):
        self.car={"brand":"toyota","model":"camry","year":2022,"color":"blue"}
        print(self.car)

    def find(self):
        key=(input("enter the key to remove"))
        if key in self.car:
            del self.car[key]
        print(self.car)
o=dis()
o.find()





class a:
    def __init__(self):
        self.key=["name","city","age"]
        self.value=["vedant","kannad",21]

    def show(self):
        list4 = []
        for i in  self.key:
            list3={self.key[i]:self.value[i]}
            list4.append(list3)
        print(list4)

p=a()
p.show()
class a:
    def __init__(self):
        self.distionary={"apple":10,"bananas":5,"orange":8}
        print(self.distionary)
       
    def show(self):
        self.distionary.clear()

        print(self.distionary)    

obj=a()
obj.show()
class demo1:
    def __init__(self):
        self.dis1={"a":1,"b":2}
        self.dis2={"b":3,"c":4}

    def intersection(self):
        dis4=self.dis1|self.dis2
        print(dis4)
s=demo1()
s.intersection()
import dis


class ascept:
    def __init__(self):
        marks={}
        i=0
        self.list1=[]
        self.list2=[]
        while (i<5):
            self.list1=str(input("enter the subject"))
            self.list2.append(self.list1)
            i+=1
        print("entered marks is")
        marks=dis(self.list2)
        print(marks)

d=ascept()
"""

#####################################################

"""class SubjectData:
    def __init__(self):
        self.student_marks = {}

    def accept_marks(self):
        
        for i in range(5):
            subject = input(f"Enter the name of subject {i+1}: ")
            marks = float(input(f"Enter marks for {subject}: "))
            self.student_marks[subject] = marks



class ReportGenerator(SubjectData):
    def display_report(self):
        for subject, marks in self.student_marks.items():
            print(f"{subject}: {marks}")

    def calculate_and_display_stats(self):
        total_marks = sum(self.student_marks.values())
        average_marks = total_marks / len(self.student_marks)
        
        print(f"Total Marks:   {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")


report = ReportGenerator()

report.accept_marks()  
report.display_report()  
report.calculate_and_display_stats()  
class product:
    def __init__(self):
        self.distionary={"pen":10,"book":100,"bag":500,"bottol":250}
        print("product details is",self.distionary)
        self.key=input("enter key to display its  value")


class display(product):
    def show(self):
        if self.key in self.distionary:
            print(f"the prize of {self.key}is {self.distionary [self.key]}")
        else:
            print("item is not in list") 

    
a=display()
a.show()


                        


class doctors:
    def __init__(self):
        self.doctor={101: "Dr. Smith",102: "Dr. Johnson",103: "Dr. Williams"}
        print("avalable doctors",self.doctor)

class avalable(doctors):
    def calculation(self):
        key=int(input("enter the number to search"))

        if key in self.doctor:
            print(f" this no assine to {self.doctor[key]}")

        else:
            print("invalid number")

d= avalable()
d.calculation()
"""

from abc import ABC abstractmethod