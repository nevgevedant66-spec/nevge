#1

'''class amount():
    
    def getvalues(self, bill):
        bill = int(input("enter your total bill: "))
        if bill > 1000:
            discount = bill * (15 / 100)
            print("you got a discount :", discount)
            return bill  
        else:
            print("you are not elegible for discount")
            return bill

    def calculate_gst(self):
        total_bill = self.getvalues(0) 
        gst1 = int(total_bill * (12 / 100))
        final_bill = total_bill + gst1
        print("your bill with gst is ", final_bill)
        return final_bill

d = amount()
d.calculate_gst()


class doctor_apportment(amount):
    doctor_days = {"dr manish": "monday", "dr suresh": "tuesday","dr tupe":"wednesday","dr sujeet":"thursday","dr ramesh":"friday","dr raju":"satursda"}
        
    def get_drname(self, dr_name):
        name = str(input("Enter doctor name: "))
        if name in dr_name:
            print(name, "is available on", dr_name[name])
            self.calculate_gst()
        else:
            print(name,"is not existing in my hospital")
            
    
                
dr=doctor_apportment()
dr.get_drname(doctor_apportment.doctor_days)'''
##########################################################################3
'''
#2
class flight:
    distonary={"kannad":"night=07:30","kalimat":"morning:08:30","dhule":"evening 05:30","pune":"night 09:30"}
    def sambhajinagar(self,ascept):
        get=input("enter your city name")
        if get in ascept:
            print(get,"this flight is going  on",ascept[get])


        else:
            print("no flight yet")
access=flight()
access.sambhajinagar(flight.distonary)

class bill_calculation:
       
        
    def discount(self,bill):
       bill=int(input("enter your flight  bill"))
       if bill>1000:
            c=bill*(50/100)
            print("you got discount",c)
            return bill

       else:
            print("you no elegible to discount")

            return 0
    def gst(self,gst) :
        v=self.discount(self)
        g=v*(12/100)
        f=g+v
        print("with gst your flight bill is",f)

    
        
f=bill_calculation()
f.gst(0)'''

 ###############################################################################   
 #3
'''class vedant():
    def __init__(self):
        name=input ("enter your name")
        print(name)
v=vedant()

class parameterise():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks       
f=parameterise("John", 85)
print(f.name, f.marks)

class student():
    def __init__(self,roll_no,marks):
        self.roll_no=roll_no
        self.marks=marks
d=student(57,97)
print(d.roll_no,d.marks)'''
######################################################
'''
#4
class student:
    def get_quantity(self,quantity):
        quantity=int(input("enter total no of student"))
        if quantity>1:

            a=quantity/7
            a1=quantity-a
            print("class a:",a)
        if quantity>a:
                b=quantity/7
                a2=quantity-b
                print("class b:",b)
        if quantity>a:
                c=quantity/7
                a3=quantity-c
                print("class c:",c)
        if quantity>a:
                d=quantity/7
                a4=quantity-d
                print("class d:",d)
        if quantity>a:
                e=quantity/7
                a5=quantity-e
                print("class e:",e)
        if quantity>a:
                f=quantity/7
                a5=quantity-f
                print("class b:",b)
        if quantity>a:
                g=quantity/7
                a2=quantity-g
                print("class g:",g)
        else:
            print("divission not possible")

        
d=student()
d.get_quantity(0)
'''
####################################################3
'''
#4
class demo:
    def __init__(self,name):
        self.name=name
        print("your name is:",name)
name=input("enter your name")
s= demo(name)


class a:
    def __init__(self,name):
        self.name=name
        print("your name is",name)

name=input("enter your name")
s=a(name)


class b(a):
    def __init__(self ,id):
        self.id=id
        print("your id is",id)

    

id=input("enter your id")
d=b(id)

'''