from tkinter import *
from tkinter.scrolledtext import ScrolledText
root=Tk()
root.state('zoomed')
Label(root,text='Address :',font=('arial',20,'bold')).place(x=500,y=360)
add_ety=ScrolledText(root,height=0.1,width=36)
add_ety.place(x=650,y=360)

root.mainloop()
