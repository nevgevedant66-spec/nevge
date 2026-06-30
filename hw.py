'''list=[]
i=0
while(i<5):
    a=input(f"enter {i} numbers")
    i+=1   
    list.append(a)
for a in list:
    print(f"numbers in a{a}")
print("----------------------------------------------------------------------")  
color=[]
i=0
while(i<5):
    color1=input(f"enter{i}color name")
    i+=1
    color.append(color1)
for a in color:
    print(f"your entered color is {a}")
print("----------------------------------------------------------------------")  

list=[]
lis=int(input("enter no of list element"))
i=0
while(i<lis):
    liss= input (f"enter{i}string")
    i+=1
    list.append(liss)
for a in list:
    print("your enter string is",a)
print("----------------------------------------------------------------------")  
list1=[1,2,3,4,5,6]
list2=[7,8,9,10]
i=0
for  i in range(4):
    for j in range(4):
          print("*" ,end ="")
    print()

print("mobile calling ")
a=input("can you sure  to make voice call if yess the enter yess if not the enter no:")
if a=="yess":
    print("wet for call receiving")
    b=input("can you receive a call if yess the enter ok if not then enter cancle:")
    if b=="ok":
        print("call recerved successfully")
        c= int (input("enter your calling duration"))
        d=0.5*c
        print("your total paid amount is:",d)
        m=100-d
        print("your corrent balance is",m)
    elif b=='cancle':
        print("call  is cut")
    else:
        print("plese entera valid input ok/cancle")
elif a=='no':
    print("fine if you want to make a voice call then enter yess")
else:
    print("enter valid input yess/not ")    '''

    



