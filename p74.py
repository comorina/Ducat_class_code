u=input("enter username:")
p=input("enter password:")
u=u.strip()
u=u.lower()
if(u=="admin" and p=="admin"):
    print("valid")
else:
    print("invalid")
