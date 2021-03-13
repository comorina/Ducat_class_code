l1=[10,20,30,[40,50]]
l2=l1.copy() #shallow copy
print(l1)
print(l2)
l1[0]=100
l1[3][0]=400
print(l1)
print(l2)
