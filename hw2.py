'''temperature=[12,13,54,66,78,57]
hot_days=[temp for temp in temperature if temp>30]
print (hot_days)
'''------------------------------------------------------------------------'''
num=[12,32,4,3,5,67,8,6]
i=0
square=[sqr**2 for sqr in num   ]
print(square)
print("-----------------------------------------------------------------------")
list=["vedant","rohit","anush","atharv"]
i=0
while (i<len(list)):
    print(list[i].upper())
    i+=1
print("-------------------------------------------------------------------------")    
list=[10,15,22,41,57]
even=[eve  for eve in list if eve%2==0]
print(even)
 
print("--------------------------------------------------------------------------")
num=[10,-5,20,-3,15]
negative=[num1 for num1 in num if num1<0]
print(negative)
print(num.replace(negative.0))
print("---------------------------------------------------------------------------")

list=["Amit","Sandip","Anjali","Kiran","Akash"]
i=0
a=[b for  b in list if b[i]=='A']
print(a)
num.sort()
print(num)
num1=[10,50,20,40,30]
num1.sort()
print(num1)
print("-------------------------------------------------------------------------------")
list=["Apple","kivi","banana","pear"]
list.sort(key=len)
print(list)
print("-------------------------------------------------------------------------------")
list=[40,10,30,20]
a=sorted(list)
print(list)
print(a)

print("--------------------------------------------------------------------------------")
list=[12,45,78,23,89,56]
num=sorted(list)
print(num[3:])
list=['python is easy to learn']
i=0
list.sort(list[i]<len-1)
print(list)
print("---------------------------------------------------------------------------------------")
list=[12,34,-23,-43,-6,56]
i=0
list1=[num for num in list if num<0]
list1[i]=0
print(list1)
print("-------------------------------------------------------------------------------------------------")
num=[12,67,-9,-67,46,23,-89,-79]
i=0
for i in range (len(num)):
    if num[i]<0:
        num[i]=0
print(num)        
print("---------------------------------------------------------------------------------------------")
num=[12,-3,-2,-1,123,45,12]
i=0
a=[b if b<=0 else 0 for b in num ]
print(a)
list=["vedant","rohit","shayad","anush","shubham","saurabhbhai"]
i=0
num=[b if b[i]!='s'  else 'z' for b in list]
print(num)
list=[12,32,34,12,21,32,23,56,69,70,89,90]
i=0
demo=["found"if list[i]<35 else "not found"]
print(demo)'''


'''home=[12,-3,23,-45,-65,-65]
i=0
home1=["positive" if x>0  else"negative" if x<0 else "invalid number in list " for x in home]
print(home1)'''
i=0
a=[]
while i<5:
    list=input(f"enter{i}number ")
    i+=1
a.extend (list)    
a=["positive"if x>0 else "negative"if x<0 else "involid input" for x in a]    
print(f"{a}")