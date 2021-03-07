cp=int(input("enter cp:"))
sp=int(input("enter sp:"))
print(1)
if(sp>cp):
    print("profit",sp-cp)
print(2)
if(cp>sp):
    print("loss",cp-sp)
print(3)
if(cp==sp):
    print("No profit no loss")
    
