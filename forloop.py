list=[1,2,3,4,5,6,7,8,9,10]
list[1]=5
list.append(66)# one element can insert at the end of list
print(list)
list.insert(5,88)#one lelemnt insert at specific possition
print(list)
list.extend([23,45,67,78,93,23,2,3,3])#multiple element insert at the end of list
print(list)
list[3]=34
print(list)
list.pop(3)
print(list)
list.remove(list[5])
print(list)
del list[1]
print(list)
list.clear()
print(list)
list.append(5)
print(list)
list.insert(1,34)
print(list)
list[1]=66
print(list)