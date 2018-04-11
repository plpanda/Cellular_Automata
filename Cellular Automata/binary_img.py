from tkinter import *
import tkinter as tk
from cellular_functions import *

def create(master,arr):
    master.destroy()
    master=Frame(f2,bg="#ebf0f5",width=500,height=500)
    master.place(x=0,y=0)
    arr=x=[list(map(int,i)) for i in arr]
    w1 = Canvas(master, width=500, height=500)
    w1.pack()
    s=len(arr[0])
    n=len(arr)
    w=500/s
    h=500/n
    x,y=0,0
    for i in (arr):
        for j in (i):
            if j==0:
                w1.create_rectangle(x, y, x+w, y+h, fill="white",outline="")
            else:
                w1.create_rectangle(x, y, x+w, y+h, fill="black",outline="")
            x=x+w
        y=y+h
        x=0
def particular_pattern(string,rule):
    st=[]
    for i in range(161):
        st.append(string)
        string=apply(string,rule)
    create(f,st)
win=tk.Tk()
win.geometry("800x500")
win.resizable(0,0)

f1=Frame(win,bg="#408eba",width=300,height=500)
f2=Frame(win,bg="#ebf0f5",width=500,height=500)
f1.grid(row=0,column=0)
f2.grid(row=0,column=1)

f3=Frame(f1,bg="#408eba",width=300,height=250)
f4=Frame(f1,bg="#408eba",width=300,height=250)
f3.grid(row=0,column=0)
f4.grid(row=1,column=0)

l1=Label(f3,text="Enter the Rule code : ",bg="#408eba",fg="black",font="times 20 bold")
e1=Entry(f3,fg="black",font="times 18")
l1.place(x=10,y=20)
e1.place(x=20,y=60)
f=Frame(f2,bg="#ebf0f5",width=500,height=500)
f.place(x=0,y=0)
Button(f3,text=" Visualise ",font="Times 20",command=lambda:particular_pattern('0'*80+'1'+'0'*80,[int(e1.get())]*161)).place(x=60,y=100)
win.mainloop()
