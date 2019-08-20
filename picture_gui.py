from tkinter import *
from PIL import Image, ImageTk 

global open_image
global open_image1
global open_imag2
global open_image3

screen = Tk()
screen.title("Calculator")
screen.geometry("500x500+0+0")
canvas = Canvas(screen,width = 300, height = 300)
canvas.grid(row = 2, column = 1)

def add(self):
   # c = 12+23
    add1 = Image.open("Panda.png")
    self.open_image = ImageTk.PhotoImage(add1)
    self.canvas.create_image(20,20, anchor = NW, image = self.open_image)
    self.canvas.image  = self.open_mage

def sub():
   # c = 23-12
    subst = Image.open("Moon.png")
    open_image1 = ImageTk.PhotoImage(subst)
    l2 = Label(canvas ,image = open_image1 )
    l2.grid(row=2,column=1)

def mul(self):
   # c = 12*23
    multiphication1 = Image.open("nature.png")
    open_image2 = ImageTk.PhotoImage(multiphication1)
    l3 = Label(canvas ,image = open_image2 )
    l3.grid(row=2,column=1)

def div():
    #c = 23/12
    div1 = Image.open("cat.png")
    open_image3 = ImageTk.PhotoImage(div1)
    l4 = Label(canvas ,image = open_image3 )
    l4.grid(row=2,column=1)



addition = Button(screen,text = "+",command = add)
addition.grid(row = 0 )
#addition.place(bordermode = OUTSIDE, side = "right")

substraction = Button(screen,text = "-",command = sub)
substraction.grid(row = 0, column = 2)

mult = Button(screen,text = "*",command = mul)
mult.grid(row = 3, column = 0)

divison = Button(screen,text = "/",command = div)
divison.grid(row = 3, column = 2)


mainloop()