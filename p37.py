cp=int(input("enter cp:"))
sp=int(input("enter sp:"))
print(1)
if(sp>cp):
    print("profit",sp-cp)
print(2)
elif(cp>sp):
    print("loss",cp-sp)
print(3)
elif(cp==sp):
    print("No profit no loss")
    
