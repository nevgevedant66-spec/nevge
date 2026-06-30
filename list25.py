
from abc import ABC ,abstractmethod
"""class a:
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def sum(self):
        pass

class b(a):
    def __init__(self):
        self.list1=[1,2,3,4,5,6,7,8]
    def sum(self):
        print(sum(self.list1))

c=b()
c.sum() 

class aggregator:
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def aggregate_data(self):
        pass

class Listsummer(aggregator):
    def __init__(self):
        self.list1=[1,2,3,4,5,6]
        
        
    def aggregate_data1(self):
        print(sum(self.list1))
    
class Dictvalue_summer(Listsummer):
    def __init__(self):
        super().__init__()
        self.dict={"marathi":12,"math":23,"java":34,"python":45}

    def aggregate_data(self):
        print(sum(self.dict.values()))

c=Dictvalue_summer()
c.aggregate_data1()
c.aggregate_data()

"""
class uniquefinder:
    @abstractmethod
    def __init__(self,list1,dect1):
        pass
    @abstractmethod
    def removeduplicate1(self):
        pass
    @abstractmethod
    def removeduplicate2(self):
        pass

class original(uniquefinder):
    def __init__(self,list1,dict1):
        self.list1=list1
        self.dict1=dict1
        

    def removeduplicate1(self ):
        set1=set(self.list1)
        print(set1)

class original2(original):
    def removeduplicate2(self):
        list2=[]
        list3=[]
        for i in self.dict1:
            list2=self.dict1.values()
            list3.append(list2)
        set3=set(list3)
        print(set3)
            
list1=[1,1,2,2,3,3,4,5,6,6]
dict1={1:2,3:2,4:3,5:3}
c=original2(list1,dict1)
c.removeduplicate2()
d=original(list1,dict1)
d.removeduplicate1()
            
