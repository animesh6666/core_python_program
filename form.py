from tkinter import *
window = Tk()
window.title("Login Form")
def printdata():
    print("Username : %s\n Password : %s"%(username.get(),password.get())
    #username.delete(0,END)
    #password.delete(0,END)
    #Label(window,text = "User Name : %s"%(username.get()),bg = "Blue",fg = "white").grid(row = 4,column = 1)
    #Label(window,text = "Password : %s"%(password.get()),bg = "Blue",fg = "white").grid(row = 5,column =1)

Label(window,text = "User Name",bg = "Blue",fg = "white").grid(row=0)
username = Entry(window)
username.grid(row = 0,column =1)
Label(window,text = "Password",bg = "Blue",fg = "white").grid(row=1)
password = Entry(window)
password.grid(row = 1,column =1)
#Label(window,password).grid(row = 6,column =5)

submit = Button(window,text = "Submit",bg = "Blue",fg = "white",command = printdata).grid(columnspan = 2)

window.mainloop()
mainloop()
