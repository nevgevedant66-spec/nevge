
from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass
        
    @abstractmethod
    def display(self):
        pass

class circle(Shape):
    def __init__(self,radius):
        self.radius=radius
       
    def area(self):
        d=3.14*self.radius**2
        print("area of circle is",d)
        

    
class reactangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def display(self):
        areais=self.width*self.height
        print("ares is",areais)

f=circle(43)
f.area()

c=reactangle(123,65)
c.display()
#dessign imployee manage ment system  create an abstract class employee  with abstrace method calculate salary class 1.full time employee 2.part time employee 3. enter  
#create a class manager  that inherit from  employee the manager class should  have one additional attribut allows (extra pay) 2.override the calculate salary in manager  to include  allowes in the  salary