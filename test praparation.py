"""list=[1,2,3,4,5,54,4,3,4,5,4]
largest=list[0]
for i in list:
    if i>largest:
        largest=i
print(largest)

list1=[1,3,2,1,3,4,2]
smallest=list1[0]
for i in list1:
    if i<smallest:
        smallest=i
print(smallest)  
 
list2=[1,2,3,4,5,6,7,8,9,10,11]
for i in list2:
    if i%2==0:
       print(i)
list3=[1,2,3,4,5,6,7,8,9,10,11]
for i in list3:
    if i%2==1:
        print(i)
list4=[1,2,3,4,5,6,7,8,9,10,11]
i=0
sum=0
for i in list4:
    sum+=i
print(sum)

lista=[1,2,3,4,5,6]
sub=0
for i in lista:
    sub-=i
print(sub)
i=0
listc=[]
while (i<5):
    listb=int(input(f"enter {i} number"))
    listc.append(listb)
    i+=1
print("your list is",listc)
find=int(input("enter no to be fount in list"))
for i in listc:
    if find==i:
        print("no found at",i)

    
setw={12,23,45,56,67,87,'vedant'}
print(set)
set3=[]
s=[]
i=0
while i<5:
    set2=input(f"enter no {i} element")
    seta=list(set2)
    set3.append(seta)
    i+=1
print(set3)
find=int(input("enter the no to be fount"))
for i in set3:
    if find==i:
        print("fno fount at:",i)
set2={12,3,4,5,6,7,8,9,1}
for i in set2:
    if i%2==0:
        print(i)
seta={12,23,34,34,45,56,67,78,89,90,23}
for i in seta:
    if i%2!=0:
        print(i)

setb={1,23,42,3454,5,43,424,23,2}
count=1
for i in setb:
    count+=1
print(count)

setc={12,23,34,23,34,5,56,34,24,566,8}
largest=0
for i in setc:
    if i>largest:
        largest=i
print(largest)
class student:
    def ___init__(self):
        self.data={'name':'vedant','address':'andhaner','roll_number':60,'id':23}
        print(self.data)


class final(student):
    def display(self,key):
        super().__init__()
        if key in self.data:
            print("value=",self.data[key])
        else:
            print("key not found")

obj=final()
key=input("enter key to search")
obj.display(key)


class student:
    def  __init__(self):
        self.name=str(input("enter the name"))
        self.fees=int(input("enter student feese"))
        
    def display(self):
        print("student name is",self.name)
        print("student feese is",self.fees)
        
class fees_structure(student):
    def fees(self):
        super().__init__()
    
        print("student fees is",self.feese)
        if self.feese>5000:
            total=self.feese*(12/100)
            final=total+self.feese
            print("student feese with 12persent discount",final)

    def gst(self):
        self.fees(self)
        if self.final>5000:
            final1=self.final*(50/100)
            print("you got discount of 50 persent",final1)
obj=fees_structure()
obj.display()
obj.gst()

############################################################################
class student:
    def __init__(self):
        self.name=str(input("enter student name"))
        self.feese=int(input("entr student feese"))
    
    def display(self):
        print("student name is",self.name)
        print("student feese is",self.feese)

class calculation(student):
    def __init__(self):
        super().__init__()

    def  gst(self):
        if self.feese>5000:
            gst=self.feese*(12/100)
            print("with gst",gst)
b=calculation()
b.display()
b.gst()
################################################################################

class a:
    def __init__(self):
        self.name=str(input("enter your name"))
        self.fees=int(input("enter fees"))
        print("student name is",self.name)
        print("student feese is",self.fees)

class v(a):
    def __init__(self):
        super().__init__()
        if self.fees>2000:
            gst=self.fees*(12/100)
            print("with gst total feese is",gst)

        else:
            print("amount is not elegible for gst")
d=v()
####################################################################

class a:
    def get(self):
        self.name=str(input("enter name of student"))
        self.fees=int(input("enter feese of student"))

    def display(self):
        self.get()
        print("student name is",self.name)
        print("student feese is",self.fees)

class b(a):
    def calculate(self):
        super().display()
        if self.fees>2000:
            self.gst1=self.fees*(12/100)
            self.gst=self.gst1+self.fees


        else:
            print("amount is not elegible for gst")

    def show(self):
        self.calculate()
        print("amount with gst",self.gst)

c=b()
c.show()

"""
i=0
listc=[]
while (i<5):
    listb=int(input(f"enter {i} number"))
    listc.append(listb)
    i+=1
print("your list is",listc)
find=int(input("enter no to be fount in list"))
for i in listc:
    if find==i:
        print("no found at",i)

class a:
    def __init__(self):
        print("this is class a")

    def __init__(self):
        self.__init__(self)
        print("this is class a/1")

class b(a):
    def __init__(self):
        print("this is class b")

    def __init__(self):
        
        print("this is class b/1")
