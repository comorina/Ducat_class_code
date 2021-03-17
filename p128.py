def show(x,y):#Non-default parameters
    print(f"X={x},Y={y}")

show(10,20)     #Positional Arguments
show(x=10,y=20) #keyword Arguments
show(y=20,x=10) #keyword Arguments
#show(x=10,y=20,x=30) error(keyword arg repeated)
show(10,y=20)
#show(10,x=20)error(got multiple values for x)
#show(x=10,20)error(positional arg follows keyword arg)

    
