'''def add(a,b):
    c = a + b
    print(c)
def sub(x, y):
     z = x - y
     print(z)
def mul(n, n2):
    n3 = n * n2
    print(n3)
def div(r, r2):  # add,sub,div,mul modules
    r3 = r / r2
    print(r3)
add(5, 6)
sub(9, 5)
mul(9, 9)
div(5, 6)'''

'''def sum(a,b):
    c=a+b
    print(c)
def mul(x,y):
    r=x*y
    print(r)
def div(r,r2):
    c=r/r2
    print(c)'''

'''sum(7,4)
mul(5,5)
div(4,4)'''

'''import calculator

calculator.fibonacci(n)'''


'''def add(x,y,z):  # parameterised function
    t = x + y + z
    print(t)


x = int(input("enter the value:"))
y = int(input("enter the second value:"))
z = int(input("enter the third value:"))

add(x,y,z)'''


'''def shopping_discount(DLF):
    def inner(amount):
        if amount > 4000:
            print("Congratulations! You get a free carry bag.")
        elif amount > 3000:
            discount = 0.2 * amount
            final_amount = amount - discount
            print(f"Wow! You get a 20% discount. Final amount: {final_amount}")
        elif amount > 1000:
            print("No offers.")
        else:
            print("No special offers at the moment.")
        return DLF(amount)
    return inner
@shopping_discount
def calculate_bill(amount):
    print(f"Total bill amount: {amount}")
calculate_bill(3200)'''

'''def smartshopping(fun):
    def inner(x,y):
        t=x*y
        if(t>4000 and t<10000):
            s=t*20/100
            p=t-s
        elif(t>10000 and t<20000):
            t=t*40/100
            p=t-s
        return fun (x,p)
    return inner
@smartshopping
def shopping(x,y):
    print(x)

shopping(300,8)'''

'''def smartshopping(fun):
    def inner(x,y):
        t=x*y
        if(t>4000 and t<10000):
            s=t*20/100
            p=t-s
        elif(t>10000 and t<20000):
            t=t*40/100
            p=t-s
        return fun (p,y)
    return inner
@smartshopping
def shopping(x,y):
    print(x)

shopping(40,400)'''




'''def smartshopping(fun):
    def inner(x, y):
        t = x * y
        if t > 4000 and t < 10000:
            s = t * 20 / 100
            p = t - s
        elif t > 10000 and t < 20000:
            s = t * 40 / 100
            p = t - s
        return fun(x, y)
    return inner

@smartshopping
def shopping(x, p):
    print(x)

shopping(40, 4000)'''

'''x=10
y=20
z=x+y
print(z)'''

'''def show (x,y):
    z=x+y
    print(z)

show(2,5)'''



'''def smartbill(t):
    def inner(u,r):
        if(u>4000):
            u="A shopping bag",u*r
        elif(u>=3000):
            u=u-20/100
        elif(u>=1000):
            u='no discount',u*r
        return t(u,r)
    return inner;
@smartbill
def shoppingbill(u,r):
    total=u*r
    print(total)
shoppingbill(300,20)'''



'''class one:
    def show(self):
        print("hello")
class second(one):
    def show(self):
        print("hi")
class third(second): 
    def show(self):
        print("bye")

k=third()
k.show()'''#niche wale ne upar ke menthod ko override kia hua h

#methodoverloading

'''class one:
    def add(self,x=None,y=None,z=None,a=None,b=None):
        if(x!=None and y!=None and z!=None and a!=None and b!=None):
            r=x+y+z+a+b
            print("this is five parameter add",r)
        elif(x!=None and y!=None and z!=None and a!=None):
            v=x+y+z+a
            print("this is four parameter add",v)
        elif(x!=None and y!=None and z!=None):
            s=x+y+z
            print("this is three parameter",s)
        elif(x!=None and y!= None):
            p=x+y
            print("this is two parameter",p)
        elif(x!=None):
            print("this is one parameter",x)
        else:
            print("no parameters")
k=one()
k.add(5,6,5,2)'''
# method overriding
'''class apple13():
    ram='12'
    storage='256'
    color='black'
    camera='12mp'
    battery='2500mh'
    def show(self):
        print("mobile ram is",self.ram)
        print("mobile storage is",self.storage)
        print("mobile color is",self.color)
        print("mobile camera is",self.camera)
        print("mobile battery is",self.battery)
class apple14(apple13):
    ram='18'
    battery='5000mh'
    facelocking='yes'
    def show(self):
        print("mobile ram is",self.ram)
        print("mobile storage is",self.storage)
        print("mobile color is",self.color)
        print("mobile camera is",self.camera)
        print("mobile battery is",self.battery)
        print("mobile facelocking is",self.facelocking)
k=apple14()
k.show()'''

#single level inheritance

'''class one:
    x = 10
    y = 20

    def add(self):
        t = self.x + self.y
        print(t)


class second(one):    #single level inheritance
    a = 30
    b = 80

    def mul(self):
        e = self.a * self.b
        print(e)


t = second()
t.mul()
t.add() '''

# multiple inheritance
'''class one:
    x=45
    y=5
    def add(self):
        r=self.x+self.y
        print(r)
class second:
    a=6
    b=3
    def sub(self):
        t=self.a-self.b
        print(t)
class third(one,second):
    n1=56
    n2=5
    def mul(self):
        q=self.n1*self.n2
        print(q)
t=third()
t.mul()'''

# t.add()
# t.sub()
# t.mul()



# multilevel inheritance


#constractor

'''class emp:
    
    def __init__ (self,x,y,z,a):     # user define parameterized 
        self.name=x         # instance variable of class
        self.lastname=y
        self.age=z
        self.salary=a
    def show(self):                 # instance method of class
        print("emp name is",self.name)
        print("emp lastname is",self.lastname)
        print("emp age is",self.age)
        print("emp salary is",self.salary)

name=input("enter the name")
lastname=input("enter the lastname")
age=int(input("enter the age"))
salary=int(input("enter the salary"))

k=emp(name,lastname,age,salary)
k.show()'''







































