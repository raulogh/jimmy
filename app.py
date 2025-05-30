import tkinter as t
import random as r

def f():
    w = t.Tk()
    w.geometry('400x200')
    w.title('jimii')
    l = t.Label(w, text='I loke You, Do you like me?')
    l.pack(pady=7)
    b1 = t.Button(w, text='Yes')
    b1.place(x=50,y=100)
    b2 = t.Button(w, text='No')
    b2.place(x=170,y=100)
    def mv(e):
        a=400
        b=200
        c=100
        d=30
        x=r.randint(0,a-c)
        y=r.randint(30,b-d)
        b2.place(x=x,y=y)
    b2.bind('<Enter>',mv)
    w.mainloop()

if __name__=='__main__':
    f() 