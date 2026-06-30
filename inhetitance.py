'''class car:
    def name(self):
        print("car name is discover")

    def color(self):
        print("color is yello")

class toyota(car):
    def __init(self,name):
        self.name=name


demo=toyota()
print(demo.name())'''
'''
class a:
    def  name (self):
        print("this is class a")
    def  id(self):
        print("this is id class")

class b(a):
    def name1(self):
        print("this is  name for class b")
    def id1(self):
        print("this is id of class b")

class c(b):
    def name2(self):
        print("this is name of class c")
    def id2(self):
        print("this is id of class c")

demo=c()
print(demo.name2())
print(demo.name1())
print(demo.id())
print(demo.id1())
'''
'''
class student:
    def student_name(self,name):
        print("student name is:",name)
        

    def student_fees(self,amount):
        print("student  fees is:",amount)

        if amount>40000:
            a=amount*(50/100)
            print("you got a discount of your fees:",a)
        else:
            print("fees amount is not elegible for discount")

class branch_c(student):
    def computer_sciance(self,branch):
        print("student branch is:",branch)
        if branch=="computer sciance":
            print("good luck for programming")
        else:
            print("good luck for next study")
    
    def resistation_fees(self,rupees):
        print("your resistation fees is ",rupees)
        if rupees>6000:
            d=rupees*(14/100)
            print("you got discount of",d)
        else:
            print("ammount is not elegible for discount")

name=str(input("enter student name"))
amount=int(input("enter collage fees"))
id=int(input("enter student id"))
branch=str(input("enter student branch"))
rupees=int(input("enter student tution fees"))


demo=branch_c()
print(demo.student_name(name))
print(demo.student_fees(amount))
print(demo.computer_sciance(branch))
print(demo.resistation_fees(rupees))

class a:
    def demo(self):
        print("class call")
class b(a):
    def fake(self):
        self.demo()
        print("class 4 call")

g=b()
print(g.fake())

class student:
    def get_name(self,name):
        name=str(input("enter student name"))
        print("student name is",name)
    def get_id(self,id):
        id=int(input("enter student id"))
        print("student id is",id)
class staff(student):
    def get_staffname(self,s_name):
        self.get_name(self)
        self.get_id(self)
        s_name=str(input("enter staff name"))
        print("staff name is",s_name)
    def get_staff_id(self,s_id):
        s_id=int(input("enter staff id"))
        print("staff id is",s_id)

s=staff()
print(s.get_staffname(0))
print(s.get_staff_id(0))'''
#dessign and implement  a vehecle management system using constructor and inheritance 
#create a parent class vehecle  used constructor to unitilize vehecle no and moddle 
#create method to display vehicle details
#create a child class  'car' inherit from vehicle
#calculate the totle bill and display it  
#create a child class bike  for the return day and charges per day
#calculate total bill of bike 
#add and delete the vehicle meke a child class for  it 
#create a child class billing  inherit either car or bike 
#calculate tatal bill and aplay total doscount50000 18  10
#method 2 
"""
class vehicle:
    def __init__(self,vehicle_name,vehicle_model):
     self.vehicle_name=vehicle_name
     self.vehicle_model=vehicle_model

     print(f"{vehicle_name},{vehicle_model}")
            

class car(vehicle):
   def __init__(self,prize,days):
     super().__init__(vehicle_name=1,vehicle_model="car")
     self.prize=prize
     self.days=days
     d=prize*days
     print("total bill of car",d)
class bike(car):
   def __init__(self,return_day,chargeper_days):
     super().__init__(prize=1000,days=6)
     self.return_day=return_day
     self.chargeper_day=chargeper_days
     def __init__(self,return_day,chargeper_days):
      f=return_day*chargeper_days
      print("total charge of car",f)
    


ob=bike(3,78)
print(ob.return_day)
print(ob.chargeper_day)


"""



    