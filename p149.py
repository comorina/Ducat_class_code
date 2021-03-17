x=10
y=20
def add():
    global x,y
    x=5
    y=6
    print(x+y)

def mul():
    print(x*y)

add()
mul()
