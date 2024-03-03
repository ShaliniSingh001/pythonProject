from tkinter import *
from PIL import Image, ImageTk

top = Tk()
top.geometry("1200x700")
top.title('Welcome')

def add():
    k = int(E1.get())
    k2 = int(E2.get())
    k3 = k + k2
    E4.config(text=k3)

def sub():
    k=int(E1.get())
    k2=int(E2.get())
    k3=k-k2
    E4.config(text=k3)

def mul():
    k=int(E1.get())
    k2=int(E2.get())
    k3=k*k2
    E4.config(text=k3)

def div():
    k=int(E1.get())
    k2 = int(E2.get())
    k3=k/k2
    E4.config(text=k3)

def Exit():
    top.destroy()

path = "C:/Users/HOME/Downloads/blue gradient (1).jpg"
img2 = ImageTk.PhotoImage(Image.open(path))

L2 = Label(top, image=img2)
L2.pack()

L = Label(top, text='Calculator', bg='green', fg='white', font=('Arial 30 bold'))
L.place(x=500, y=50)

L3 = Label(top, text='FirstNO', bg='green', fg='white', font=('Arial 20 bold'))
L3.place(x=300, y=200)

E1 = Entry(top, font=('Arial 20 bold'))
E1.place(x=450, y=200)

L4 = Label(top, text='SecondNo', bg='green', fg='white', font=('Arial 20 bold'))
L4.place(x=300, y=250)

E2 = Entry(top, font=('Arial 20 bold'))
E2.place(x=450, y=250)

B1 = Button(top, text="ADD", font=('Arial 15 bold'), command=add)
B1.place(x=300, y=300)

B2 = Button(top,text="SUBTRACT",font=('Arial 15 bold'), command=sub)
B2.place(x=390, y=300)

B3 = Button(top,text="MULTIPLY",font=('Arial 15 bold'), command=mul)
B3.place(x=550, y=300)

B4 = Button(top, text="DIVIDE", font=('Arial 15 bold'), command=div)
B4.place(x=700, y=300)


L5 = Label(top, text="Result", bg='green', fg='white', font=('Arial 20 bold'))
L5.place(x=400, y=400)

E4=Label(top,font=('Arial 20 bold'))
E4.place(x=500,y=400)


top.config(bg='green')
top.mainloop()