from abc import ABC, abstractmethod
class employee:
    @abstractmethod
    def __init__(self,salary,days):
        pass
    def calculate_salary(self):
        pass
class Fulltime_employee(employee):
    def __init__(self,salary,days):
        self.salary=salary
        self.days=days
    def calculate_salary(self):
        total1=self.days*self.salary
        self.fd1=total1*0.012
        print("total salary:",total1)
        print("salary with fd:",self.fd1)
class parttime_employee(Fulltime_employee):
    def __init__(self,salary,days):
        self.salary=salary
        self.days=days
    def calculate_salary(self):
        total=self.salary*self.days
        fd=total*0.012
        print("total salary:",total)
        print("salary with fd",fd)
#part 2
class manager(Fulltime_employee):
    def __init__(self,salary,allowance):
        self.salary=salary
        self.allowance=allowance

    def calculate_salary(self):
        sum=self.salary+self.allowance
        gst=sum*0.012
        final=sum-gst
        print("salary with allowance and with gst:",final)
a=Fulltime_employee(12000,30)
a.calculate_salary()
b=parttime_employee(10000,30)
b.calculate_salary()
c=manager(12000,1000)
c.calculate_salary()