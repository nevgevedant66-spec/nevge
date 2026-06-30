'''def addition(a,b):
       sum=a+b
       return sum
print(addition(4,6))
#####################################################################

def average(): 
     sum=addition(2,4)# compelsary  argument are given because of seprate  fun block of code
     avg=sum/2
     return avg
print(average())#call of block required  function () this argument
def subtraction(a,b):
      sub=a-b
      return sub
print(subtraction(6,3))
def average():
      sub=subtraction(4,2)
      avg=sub/2
      return avg
print(average())
#write a python funcction to reversed the string  and check it palentrom or not
def string(a): 
    b=list(reversed(a))
    return b
print(string("dad"))
#####################################################################

i=0
def reverse1():
   stt=string("dad")
   if stt==stt[::-1]:
      print("it is palentrom")
   else:
      print("not palentrom")  
reverse1()
#####################################################################

def addition(a,b):
    sum=a+b
    return sum
print(addition(4,6))

def average():
    sub=addition(4,7)
    avg=sub/2
    return avg
print(average())
#####################################################################

def string(a):
    if a==a[::-1]:
        print("palentrom")
    else:
        print("not palentrom")
print(string("dad"))

#####################################################################


def num(a):
    c=1234
    if a==c:
        print("you can access this app")
    else:
        print("you can not access")

a=int(input("enter id"))
print(num(a))
#####################################################################
def string(a,b):
    s="vedant"
    p=1234
    if a==s:
      if b==p:
          print("you can access this app")
a= str (input("enter your user name"))
b= str(input("enter your id"))
print(string(a,b))
##########################################################################
def palentrom(v):
    if v==v[::-1]:
        print("it is palentrom")
    else:
        print("it not palentrom")

v= str(input("enter your string to check it is palentrom or not "))
print(palentrom(v))
#######################################################################
def  combine(a,b,c):
    if a>b and a>c:
        print("a is greater")
    elif b>a and b>c:
            print("b is greater")
    elif c>a and c>b:
         print("c is greater")
    else:
         print("equal number  not allowed")
    return a,b,c

a= int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number "))
print(combine(a,b,c)) '''
'''def demo(a):
     c=a/95
     return c

def demo1(a):
     demo(a)
     return a
a=int(input("enter INR to convert into Doller"))
print(demo(a))

def demo2(b):
     d=b*95
     return d

def demo3(b):
     demo2(b)
     return b
b=int(input("enter doller to convert into INR"))
print(demo2(b))

def  converssion_rate(b):
     demo2(b)
     n=b*0.02
     g=b-n
     print("commition=",g)
print(converssion_rate(b))



         
def demo1(a):
     dollar = a / 95  
     return dollar
a = int(input("enter INR to convert into Doller: "))
print("Dollars:", demo1(a))
def demo2(b):
     d = b * 95
     return d
def demo3(b):
     d = demo2(b)     
     return d         
b = int(input("enter doller to convert into INR: "))
print("INR:", demo3(b))
def converssion_rate(b):
     total_inr = demo2(b)            
     commission = total_inr * 0.02   
     if total_inr > 50000:
          discount = total_inr * 0.05
     else:
          discount = 0
     net_amount = total_inr - commission - discount
     print("commission =", commission)
     print("discount =", discount)   
     return net_amount               
print("commition:", converssion_rate(b))

'''
"""their are three method for function
1)get method=without parameter
2)post method
3)put method

def currency(a):#post method
     b=a*95
     return b
a=int(input("enter your currency to convert into INR"))
print("your ammount ",currency(a))

def currency1(b):
     d=currency(b)
     f=d*0.02
     return f
print("commition:",currency1(a))

def currency3(a):
     e=currency(a)
     if e>50000:
          h=e*0.05
          e=e-h
          return e
    
print("discount=",currency3(a))

def currency4(a):
     total_amount=currency(a)-currency1(a)-currency3(a)

     return total_amount
print("taoal amount=",currency4(a))



class cat:
     name="manu"
     
print("cat walk")
cat1=cat()
print(cat1.name)

class cat3:
     name1="vishal"

cat2=cat3()
print(cat2.name1)
print(cat1.name)     

"""
"""

class amount:
    def ascept(a):
        b=a=a
        return b
a=int(input("enter your bill"))
print("your ammount ",ascept(a))
    
def calculate(b):
        d=ascept(b)
if d>1000:
        c=a
        
else:
        print("not elegible for discount")   
print(calculate(a))
def gst(c):
    g=c*0.015
    return g

print("your amount with gst",gst(a))    
m=amount()
"""
#self is a refrence of current object in out program we write genetate bill self refrance to the object bill useng self one method  can access other mothod and varriables of thesame object
class amount:
    c=int(input("enter your bill"))
    def bill(self,a):
        if self.c>1000:
            self.f=self.c*0.015
        else:
            print("you are not elegible for discount")
    print(bill(c,self.a))

    def calculation(self,c):
        e=self.bill(self,c,self.a)
        k=e*0.016
        return k
    print("your final amount",calculation(c))

c=amount()
