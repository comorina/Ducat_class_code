cp=int(input("enter cp:"))
sp=int(input("enter sp:"))
if(sp>cp):
    print("profit",sp-cp)
elif(cp>sp):
    print("loss",cp-sp)
else:
    print("No profit no loss")
    
