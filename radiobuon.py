from tkinter import *
from tkinter import messagebox as m
top=Tk()
top.geometry('500x500')
top.title('writer')
var=StringVar()
var.set('yes')
Label(text='What would u like to have?',justify=LEFT,font=20,pady=20).pack()
radio=Radiobutton(text='dosa',variable=var,value='dosa').pack()
radio=Radiobutton(text='bada',variable=var,value='bada').pack()
radio=Radiobutton(text='idli',variable=var,value='idli').pack()
radio=Radiobutton(text='uttapam',variable=var,value='uttapam').pack()
radio=Radiobutton(text='upma',variable=var,value='upma').pack()
top.mainloop()
