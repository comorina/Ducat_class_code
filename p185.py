print("hello")
l=[10,20,30,40]
try:
    index=int(input("enter index[0-3]:"))
    print("Value:",l[index])
    print("apple")
except:
    print("default except")
except IndexError:
    print("except of index error")
except Exception:
    print("except of Exception")
print("Bye")
