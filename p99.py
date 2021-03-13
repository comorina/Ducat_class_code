l1=[10,20,30,[40,50]]
import copy
l2=copy.deepcopy(l1)#deep copy
print(l1)
print(l2)
l1[0]=100
l1[3][0]=400
print(l1)
print(l2)
