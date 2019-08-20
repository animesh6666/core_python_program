from tkinter import *

def add():
    c = 12+23
    label = Label(screen  ,text = c).pack(expand = "yes")

def sub():
    c = 23-12
    label = Label(screen ,text = c).pack(expand = "yes")

def mul():
    c = 12*23
    label = Label(screen ,text = c).pack(expand = "yes")

def div():
    c = 23/12
    label = Label(screen ,text = c).pack(expand = "yes")


screen = Tk()
screen.title("Calculator")
addition = Button(screen,text = "+",command = add)
addition.pack(side = "right" )
#addition.place(bordermode = OUTSIDE, side = "right")

substraction = Button(screen,text = "-",command = sub)
substraction.pack(side ="left" )

mult = Button(screen,text = "*",command = mul)
mult.pack(side = "top")

divison = Button(screen,text = "/",command = div)
divison.pack(side = "bottom")

quit_button = Button(screen,text = 'Clear', command = lambda :self.label.grid_forget())


mainloop()