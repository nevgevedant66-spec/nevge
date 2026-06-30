"""class a:
    def __init__(self):
        self.list1=[]
        self.list2=[]
        i=0
        while (i<5):
            list1=str(input("enter the cource"))
            self.list2.append(list1)
            i+=1
        print(self.list2)

    def show(self):
            self.set1=set(self.list2)
            print(self.set1)

class b(a):
     def __init__(self):
          super().__init__()
          pass
     def count(self):
          count=0
          for i in self.set1:
               count+=1

          print("cource is",count)
d=b()
d.show()
d.count()
"""
class emp:
    def __init__(self):
        self.name=str(input("enter the name of employee"))
        self.id=int(input("enter the id of employee"))
        
    def show(self):
        print(self.name)
        print(self.id)

class dis(emp):
    def __init__(self):
        super().__init__()
        self.distionary={"manager":10000,"emp":70000,"staff":50000}
        print(self.distionary)

    def calculation(self):
        print(self.distionary["manager"])
        for i in self.distionary:
            print(i)

        a=str(input("enter the name  for calculation"))
        if a in self.distionary:
            hra=self.distionary[a]*(0.020)
            da=self.distionary[a]*(0.030)
            total=hra+da
            print(total)
d=dis()
d.show()
d.calculation()