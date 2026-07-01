from abc import ABC,abstractmethod
"""
class dict:
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def get(self):
        pass

class dict2(dict):
    def __init__(self):
        d={1:12,2:34,3:45,3:50,3:28}

        self.lista=[]
        self.lista=d.values()

    def get(self):
        set2={}
        set2=set(self.lista)
        print(list(set2))
class dict3(dict2):
    def __init__(self):
        self.listb=[1,1,2,2,3,3,4,4,5,5,6,6]

    def get(self):
        set3=set(self.listb)
        print(list(set3))
p=dict2()
p.get()
d=dict3()
d.get()

class dict:
    @abstractmethod
    def __init__(self ):
        pass
    @abstractmethod
    def calculate_salary(self):
        pass
    @abstractmethod
    def calculate_gst(self):
        pass
        
class dict2(dict):
    def __init__(self ):
        i=0
        self.listb=[]
        while(i<5):
            lista=int(input("enter all employee salary"))
            self.listb.append(lista)
            i+=1

    def calculate_salary(self):
        set1=set(self.listb)
        self.listb1=list(set1)
        print(self.listb1)

    def calculate_gst(self):
        i=self.listb[0]
        if i>4000:
            v=i*0.012
        print("salary with gst",v)    
        
class  gst(dict2):
    def __init__(self ):
        j=0
        self.d={}
        while(j<5):
            self.lista=str(input("enter the name of employee"))
            self.listb=int(input("enter age"))
            self.d[self.lista]=self.listb
            j+=1
        print(self.d)    

    def calculate_salary(self):
        print(self.d.values())  
        
f=dict2()
f.calculate_salary()
f.calculate_gst()
d=gst()
d.calculate_salary()

"""
class student:
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def fees(self):
        pass
    @abstractmethod
    def age(self):
        pass
class structure:
    def __init__(self):
        self.s={}
        j=0
        while(j<5):
            self.name=str(input("enter the student name"))
            self.age=int(input("enter the student age"))
            self.s[self.name]=self.age
            j+=1
        print(self.s)
    def fees(self):
        feesb=[]
        i=0
        while(i<5):
            feesa=int(input("enter the total fees of collage of all students"))
            feesb.append(feesa)
            i+=1
        k=feesb[0]   
        g=[] 
        if i>200:
            self.d=k*0.012
            g.append(self.d)
        print(g)    
d=structure()
d.fees()