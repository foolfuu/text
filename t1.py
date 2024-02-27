from tkinter import *
class erfun:
    def add():
        x = b.get()
        y = a.get()
        for i in range(len(y)):
            a.delete(0)
        for i in x:
            a.insert(END,i)
root = Tk()
root.geometry("300x300")
root.resizable(False,False)
a = Entry(root);a.pack()
b = Entry(root,bg = 'pink');b.pack()
c = Button(root,text = 'click',command = erfun.add);c.pack()
root.mainloop()