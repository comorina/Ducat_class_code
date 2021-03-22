import os
print(os.getcwd())
if(os.path.exists("test")==True):
    print("folder exists..")
else:    
    os.mkdir("test")
    print("folder created")
