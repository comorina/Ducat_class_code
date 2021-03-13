s={1,2,3,4,5}
l=['a','b','c','d']
d={}
for i in range(4):
    d[s.pop()]=l[i]
print(d)
