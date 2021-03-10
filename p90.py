l=[]
for i in range(5):
    m=int(input("enter marks:"))
    l.append(m)
l.sort(reverse=True)
print(l[:3])
