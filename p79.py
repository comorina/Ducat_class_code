s=input("enter string:")
s=s.lower()
s1=""
count=0
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        s1=s1+i.upper()
        count+=1
    else:
        s1=s1+i
print(s)
print(s1)
print(count)
