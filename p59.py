"""
        1
    2   1
3   2   1
"""
for i in range(1,4):
    for j in range(i,3):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    print()    
