print("hello")
l=[10,20,30,40]
try:
    index=int(input("enter index[0-3]:"))
    print("Value:",l[index])
    print("apple")
except Exception:
    index=0
    print("invalid index,assigning 0 as default index")
    print("Value:",l[index])
print("Bye")
