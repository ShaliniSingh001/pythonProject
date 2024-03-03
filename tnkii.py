from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk

top = Tk()
top.geometry("1500x600")
top.title('Welcome')

def insert():
    k=E1.get()
    k2=E2.get()
    k3=int(E3.get())
    k4=int(E4.get())
    k5=p.get()
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='12345',db='project')
    cur=db.cursor()

    s="insert into emp values('%s','%s','%s','%s','%s')" %(k,k2,k3,k4,k5)
    result=cur.execute(s)
    if(result>0):
        messagebox.showinfo("Result","Record insert successfully")
    else:
        messagebox.showinfo("Result","Record not inserted")
    db.commit()
    E1.delete(0,'end')
    E2.delete(0,'end')
    E3.delete(0,'end')
    E4.delete(0,'end')

def show():
    for i in tv.get_children():
        tv.delete(i)
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='12345', db='project')
    cur = db.cursor()
    s="select * from emp"
    cur.execute(s)
    result=cur.fetchall()
    for col in result:
        name=col[0]
        last=col[1]
        sal=col[2]
        age=col[3]
        gen=col[4]
        tv.insert("",'end',values=(name,last,sal,age,gen))

# def search():
#     k=E5.get()
#     import pymysql as sql
#     db = sql.connect(host='localhost',user='root',password='12345',db='project')
#     cur =db.cursor
#     p= "select * from emp where name=%s"
#     cur.execute(p,k)
#     result=cur.fetchall()
#     for col in result:
#         name=col[0]
#         lastname=col[1]
#         salary=col[2]
#         age=col[3]
#         gen=col[4]
#         tv.insert("",'end',values=(name,lastname,salary,age,gen))

# ################################ Search ####################################################################

def search():
    k = E5.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='12345', db='project')
    cur = db.cursor()
    p = "SELECT * from emp where name =%s"
    cur.execute(p,k)
    result = cur.fetchall()
    for col in result:
        name = col[0]
        lastname = col[1]
        salary = col[2]
        age = col[3]
        gen = col[4]
        tv.insert("", 'end', values=(name, lastname, salary, age, gen))
#  ################################################### Delete ##################################################
def Delete():
    k=E5.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root',password='12345',db='project')
    cur = db.cursor()
    p = "delete from emp where name=%s"
    result=cur.execute(p, k)
    if(result>0):
        messagebox.showinfo("Result","Record delete")
    else:
        messagebox.showinfo("Result","Record not deleted")
    db.commit()

def Login():
    top.destroy()
    import Login


def Exit():
    top.destroy()

# Create a StringVar to store the selected gender
p = StringVar()

path = "C:/Users/HOME/Downloads/nature.jpg"
img2 = ImageTk.PhotoImage(Image.open(path))

L2 = Label(top, image=img2)
L2.pack()

tv = ttk.Treeview(top)
tv['columns']=('Name','Lastname','Salary','Age','Gender')
tv.column('#0', width=0,stretch=NO)
tv.column('Name',anchor=CENTER,width=110)
tv.column('Lastname',anchor=CENTER,width=110)
tv.column('Salary',anchor=CENTER,width=110)
tv.column('Age',anchor=CENTER,width=110)
tv.column('Gender',anchor=CENTER,width=110)



tv.heading('Name',text='Name',anchor=CENTER)
tv.heading('Lastname',text='Lastname',anchor=CENTER)
tv.heading('Salary',text='Salary',anchor=CENTER)
tv.heading('Age',text='Age',anchor=CENTER)
tv.heading('Gender',text='Gender',anchor=CENTER)

tv.place(x=800,y=100)


L = Label(top, text='Registration', bg='black', fg='white', font=('Arial 30 bold'))
L.place(x=400, y=50)

L3 = Label(top, text='NAME', bg='black', fg='white', font=('Arial 20 bold'), width=11)
L3.place(x=200, y=200)

E1 = Entry(top,bd=5, font=('Arial 20 bold'))
E1.place(x=420, y=200)

L4 = Label(top, text='LASTNAME', bg='black', fg='white', font=('Arial 20 bold'), width=11)
L4.place(x=200, y=250)

E2 = Entry(top,bd=5 ,font=('Arial 20 bold'))
E2.place(x=420, y=250)

L5 =Label(top,text= "SALARY", bg='black', fg='white', font=('Arial 20 bold'), width=11)
L5.place(x=200, y=300)

E3 = Entry(top,bd=5,font=('Arial 20 bold'))
E3.place(x=420,y=300)

L6 = Label(top, text= "AGE", bg='black', fg='white', font=('Arial 20 bold'), width=11)
L6.place(x=200, y=350)

E4=Entry(top,bd=5,font=('Arial 20 bold'))
E4.place(x=420,y=350)

L7 = Label(top, text= "GENDER", bg='black', fg='white', font=('Arial 20 bold'),width=11)
L7.place(x=200, y=400)

r1=Radiobutton(top,text='Male',value='Male',variable=p,font=('Arial 15 bold'))
r1.place(x=420,y=400)

r2=Radiobutton(top,text='Female',value='Female',variable=p,font=('Arial 15 bold'))
r2.place(x=520,y=400)

r3=Radiobutton(top,text='Other',value='Other',variable=p,font=('Arial 15 bold'))
r3.place(x=650,y=400)

# L8 = Label(top, text="Search", bg='black', fg='white', font=('Arial 20 bold'))
# L8.place(x=800, y=50)

# E5 = Entry(top, bd=5, font=('Arial 20 bold'))
# E5.place(x=920, y=50)


B1 = Button(top, text="Submit",bg='pink', font=('Arial 15 bold'),command=insert)
B1.place(x=450, y=500)

B2 = Button(top,text="Exit",bg='red',font=('Arial 15 bold'),command = Exit)
B2.place(x=350, y=500)

B3 = Button(top,text="Show",bg='green',font=('Arial 15 bold'),command=show)
B3.place(x=700,y=500)

B4 = Button(top,text="Delete",bg='Black', fg='white',font=('Arial 15 bold'),command=Delete)
B4.place(x=1180,y=50)

B5 = Button(top,text="Login",bg='purple',font=('Arial 15 bold'),command=Login)
B5.place(x=800,y=500)

B6 = Button(top, text="Search", bg='black', fg='white', font=('Arial 16 bold'),command=search)
B6.place(x=800, y=50)

E5 = Entry(top, bd=5, font=('Arial 16 bold'))
E5.place(x=900, y=50)





top.config()
top.mainloop()




