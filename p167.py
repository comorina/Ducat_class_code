import random as rd
print(rd.random())
print(rd.uniform(5,10))
print(rd.randint(1,100))
l=[10,20,30,40,50,60,70,80,90,100]
print(rd.sample(l,5))
rd.shuffle(l)
print(l)
print(rd.choice(l))
otp=rd.randint(1000,9999)
print(otp)
