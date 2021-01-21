from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Clock")

def time():
    # string = stringVar()
    string = strftime('%H:%M:%S %p')
    label1.config(text=string)
    label1.after(1000, time)

label1 = Label(root, font =('calibri', 40, 'bold'), background= 'pink', foreground ='black')

label1.pack( anchor = 'center')
time()

mainloop()