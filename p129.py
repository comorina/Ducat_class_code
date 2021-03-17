def show(x,*,y):#all params after * become keyword only
    print(f"X={x},Y={y}")
show(10,y=20)
show(x=10,y=20)

    
