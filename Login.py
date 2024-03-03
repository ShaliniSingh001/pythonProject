from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk

top = Tk()
top.geometry("1500x600")
top.title('Welcome')


def Login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='12345', db='project')
    cur = db.cursor()
    cur.execute("select * from emp where name=%s and lastname=%s",(E1.get(),E2.get()))
    row = cur.fetchone()

    if row == None:
        messagebox.showerror("Error", "Invalid User Name And Password")
    else:
        top.destroy()
        import sss

def Exit():
    top.destroy()


p = StringVar()

path = "C:/Users/HOME/Downloads/nature.jpg"
img2 = ImageTk.PhotoImage(Image.open(path))

L2 = Label(top, image=img2)
L2.pack()


L3 = Label(top, text='NAME', bg='black', fg='white', font=('Arial 20 bold'), width=11)
L3.place(x=200, y=200)

E1 = Entry(top,bd=5, font=('Arial 20 bold'))
E1.place(x=420, y=200)

L4 = Label(top, text='LASTNAME', bg='black', fg='white', font=('Arial 20 bold'), width=11)
L4.place(x=200, y=250)

E2 = Entry(top,bd=5 ,font=('Arial 20 bold'),show="*")
E2.place(x=420, y=250)

B1 = Button(top, text="Login",bg='pink', font=('Arial 15 bold'),command=Login)
B1.place(x=500, y=400)




top.config(bg='green')
top.mainloop()