from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk

top = Tk()
top.geometry("1500x600")
top.title('Welcome')

def Exit():
    top.destroy()


p = StringVar()

path = "C:/Users/HOME/Downloads/nature.jpg"
img2 = ImageTk.PhotoImage(Image.open(path))

L2 = Label(top, image=img2)
L2.pack()

j=['Select','Java','Python','HTML','CSS','Bootstrap','Ruby','MYSQL']

L3 = Label(top, text='Welcome', bg='black', fg='white', font=('Arial 20 bold'), width=11)
L3.place(x=500, y=200)

cb=ttk.Combobox(top,values=j,font=('Arial 20 bold'))
cb.place(x=200,y=300)
cb.current(0)

C=Checkbutton(top,text='java',font=('Arial 16 bold'))
C.place(x=200,y=400)

C2=Checkbutton(top,text='Python',font=('Arial 16 bold'))
C2.place(x=290,y=400)

C3=Checkbutton(top,text='HTML',font=('Arial 16 bold'))
C3.place(x=400,y=400)

C4=Checkbutton(top,text='Ruby',font=('Arial 16 bold'))
C4.place(x=500,y=400)

C5=Checkbutton(top,text='Mysql',font=('Arial 16 bold'))
C5.place(x=600,y=400)

C6=Checkbutton(top,text='Bootstrap',font=('Arial 16 bold'))
C6.place(x=700,y=400)

top.config()
top.mainloop()