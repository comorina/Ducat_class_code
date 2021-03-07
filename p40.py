amt=int(input("enter amount:"))
if(amt>=1000):
    amt=amt-50
    pc=input("enter promocode:")
    if(pc=='bharat'):
        amt=amt-50
print("Final Amount:",amt)        
        
