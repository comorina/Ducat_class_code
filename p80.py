age=20
name="sonu"
marks=89.5
s="Age:"+str(age)+",Name:"+name+",Marks:"+str(marks)
s1="Age:%d,Name:%s,Marks:%.2f"%(age,name,marks)
s2="Age:{},Name:{},Marks:{}".format(age,name,marks)
s3="Age:{a},Name:{n},Marks:{m},Age:{a}".format(n=name,m=marks,a=age)
s4=f"Age:{age},Name:{name},Marks:{marks}"
print(s)
print(s1)
print(s2)
print(s3)
print(s4)


