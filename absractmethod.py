 

"""class a:
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def diaplay(self):
        pass
class b(a):
    def __init__(self):
        print("abstract class called")

    def display(self):
        print("second absytract class called")
s=b()
s.display()
"""
#########################################################################
#question no1(class)
"disire the shape system where circle and rectangle both implement in  iterface area"
from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
        
    @abstractmethod
    def display(self):
        pass

class Ascept(Shape):
    def __init__(self):
        self.circle = int(input("Enter the radius of circle: "))
        self.rectangle = int(input("Enter the side of rectangle: "))
        

    def area(self):
        self.area1 = 3.14 * (self.circle * self.circle)  
        self.side = self.rectangle * self.rectangle  

    def display(self):
        print("Area of circle is:", self.area1)
        print("Area of rectangle is:", self.side)


d = Ascept()
d.area()  
d.display()        
