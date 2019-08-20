from tkinter import *
Click =0
def hello():
    global Click
    Click  = Click +1
    if(window.config(text = Click)%2==0):
        a = Label(window,text = "hii")
        a.pack()

window = Tk()
window.title("Hii")
p = Button(window,text = 'Click Me !', command=hello)
p.pack()
window.mainloop()