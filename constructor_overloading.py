"""class vehicle:
    def __init__(self):
        self.vehicle1=str(input("enter vehicle name"))
        self.model=int(input("enter model name"))
        print(f"{self.vehicle1} {self.model}")
class bill(vehicle):
    def __init__(self,total_prize,days):
        super().__init__()
        self.total_prize=total_prize
        self.days=days
        f=total_prize*days
        gst=f*(12/100)
        sum=gst+f
        print("with gst",sum)
        if sum>5000:
            u=sum*(45/100)
            print("you got discount",u)
        else:
            print("amount is not elegible for discount")
obj=bill(5000,12)
#############################################################3
class student:
    def __init__(self):
        name=str(input("enter student name"))
        id=int(input("enter student id"))
        print("student name is",name )
        print("student id is",id)


class roll2(student):
    def __init__(self):
        super().__init__()
        rollno=int(input("enter student roll number"))
        print("student roll no is",rollno)
        fees=int(input("enter student fees"))
        if fees>20000:
            d=fees*(50/100)
            f=d+fees
            print("with discount",f)
        else:
            print("amount is not elegible for discount")
class fees1(roll2):
    def __init__(self):
        super().__init__()
        age=int(input("enter student age"))
        if age>18:
            print("elegible for collage examilation demo")
        else:
            a=18-age
            print("try",a,"year leter")


f=fees1()
####################################################
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        print("student name:",name)
        print("student roll no:",rollno)
class fees1(student):
    def __init__(self,fees,month):
        super().__init__(name="vedant",rollno=60)
        self.fees=fees
        self.month=month
        print("fees:",fees)
        print("you have",month,"month")
        if month>=3:
            inc=fees+6000
            print("your fees is after penelty",inc)
        else:
            print("pay regular fees")

class calculation(fees1):
    def __init__(self):
        super().__init__(fees=10000,month=3)
        total=self.fees*(12/100)
        f=total+self.fees
        print("your fees after gst is",f)
        if f>40000:
            d=f*(50/100)
            g=f-d
            print("you got a discount",g)
        else:
            print("amount is not elegible for discount")

d=calculation()

######################################################################
"""

class shop:
    def __init__(self):
        name=str(input("enter shop name"))
        address=str(input("enter address"))
        print("shop name is",name)
        print("shop address is",address)
class buying_goods(shop):
    def __init__(self,s=0,i=0):
        super().__init__()
        while(i<5):
            goods1=str(input(f"enter {i}goods you buy"))
            
            i+=1
        print("your goods is",goods1)
        

class billing_goods(buying_goods):
    def __init__(self):
        super().__init__()
        total=int(input("enter your total bill"))
        if total>500:
            gst=total*(12/100)
            gst1=gst+total
            print("with gst your bill is",gst1)
        if gst1>5000:
            discount=gst1*(50/100)
            print("you got discount",discount)
s=billing_goods()