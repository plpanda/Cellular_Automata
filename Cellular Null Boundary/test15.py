from tkinter import *

def create(arr):
    arr=x=[list(map(int,i)) for i in arr]
    master = Tk()
    master.resizable(0,0)
    w1 = Canvas(master, width=600, height=600)
    w1.pack()
    s=len(arr[0])
    n=len(arr)
    w=600/s
    h=600/n
    x,y=0,0
    for i in (arr):
        for j in (i):
            if j==0:
                w1.create_rectangle(x, y, x+w, y+h, fill="red",outline="")
            else:
                w1.create_rectangle(x, y, x+w, y+h, fill="blue",outline="")
            x=x+w
        y=y+h
        x=0
    mainloop()
