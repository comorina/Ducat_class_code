while(True):
    n1=int(input("enter 1st num:"))
    n2=int(input("enter 2nd num:"))
    ch=int(input("enter choice:\n1.add\n2.mul\n"))
    if(ch==1):
        print(n1+n2)
    elif(ch==2):
        print(n1*n2)
    else:
        print("invalid choice!")
    c=input("Do you want to run this code again(y/n)?")
    if(c=='y'):
        continue
    else:
       break

print("Thank You!!")






