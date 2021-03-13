s={1,2,3,4,5}
l=['a','b','c','d']
d={}
j=0
for i in s:
    if(j<=3):
        d[i]=l[j]
        j+=1
    else:
        break
print(d)
