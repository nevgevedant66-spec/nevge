from abc import ABC , abstractmethod
class get_empname():
    @abstractmethod
    def __init__(self,name):
        pass
    
    @abstractmethod
    def salary_e(self):
        pass
    @abstractmethod
    def salary2(self):
        pass
    @abstractmethod
    def calculation(self):
        pass
class get_data(get_empname):
    def __init__(self):
       pass
    
    def salary_e(self):
        i=0
        name1=[]
        self.name2=[]
        while(i<5):
            name1=str(input(f"enter the {i}name"))
            self.name2.append(name1)
            i+=1
        print(self.name2)

    def salary2(self):
        self.salary_e()
        v=0
        salary1=[]
        self.salary_t=[]
        while(v<5):
            salary1=int(input(f"enter the {v}salary of"))
            self.salary_t.append(salary1)
            v+=1
        print(self.salary_t)        
    def calculation(self):
    
        self.salary2()
        total=0
        for c in self.salary_t:
            total=total+c
            d=total/len(self.salary_t)
            print(f"average{c}",d)
        
a=get_data()
a.calculation()
"""
from abc import ABC ,abstractmethod
class get:
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def addition(self):
        pass
    @abstractmethod
    def subtraction(self):
        pass
    @abstractmethod
    def multiplication(self):
        pass
    @abstractmethod
    def divission(self):
        pass
    

class add(get):
    def __init__(self):
        self.a=int(input("enter the 1st number"))
        self.b=int(input("enter 2nd number"))
    def addition(self):
        c=self.a+self.b
        print(c)
    def subtraction(self):
        d=self.a-self.b
        print(d)
class div(add):
    def multiplication(self):
        s=self.a*self.b
        print(s) 
    def divission(self):
        self.multiplication()
        m=self.a/self.b
        print(m)    
g=add()
g.addition()
g.subtraction
f=div()
f.multiplication()
f.divission()

"""