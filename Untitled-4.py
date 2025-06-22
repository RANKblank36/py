from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():

    top = Toplevel()
    top.geometry("180x100")
    top.title("Error")

    l2 = Label(top, text="ERROR")
    l2.pack()

l = Label(root, text="This is root window")
btn = Button(root, text="Click here to open error window", command=topwin)

l.pack()
btn.pack()

root.mainloop()