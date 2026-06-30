'''list=[12,45,7,89,34,67]
i=0
j= list[0]
while(i<len(list)):
    if(list[i]%2==0):
        j=list[i]
    i+=1    
print(j)        

list=[10,15,22,31,44,57,68]
i=0
j=list[0]
liss=[]
while i<len(list):
    if list[i]%2==0:
        j=list[i]
        liss.append(j)
    i+=1
print(liss)        
list=[2,3,4,5]
liss=[]
i=0
for i in list:
    a=i**2
    liss.append(a)
print(liss)    
number=[10,-5,20,-3,15,-8]
num=[]
for i in number:
    if i>0:
        num.append(i)
print(num)        '''
list= ['vedant,''rohit','saurabh','Additya','Atharv']
liss1=[]
for liss in list:
    if liss[0]=='A':
        liss1.append(liss)
print(liss1)       