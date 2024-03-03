'''from abc import abstractmethod
import random

class ATM:
    @abstractmethod
    def CreateAccount(self):
        pass
    @abstractmethod
    def DepositAmount(self,bal):
        pass
    @abstractmethod
    def WithdrawAmount(self,amount):
        pass
    @abstractmethod
    def CheakBal(self):
        pass
    @abstractmethod
    def Exit(self):
        pass

class Bank(ATM):
    Balance=0
    def __init__(self,x,z,a):
        self.name=x
        self.AadharNo=z
        self.Branch=a
        self.AccountNo=random.randint(10000,999999)
    def CreateAccount(self):

        print("Emp name is",self.name)
        print("emp AadharNo is",self.AadharNo)
        print("emp Branch Name",self.Branch)
        print("emp Account No is",self.AccountNo)
    def DepositAmount(self,bal):
        self.Balance=self.Balance+bal
    def WithdrawAmount(self,amount):
        self.Balance=self.Balance-amount
    def Checkbal(self):
        print(self.Balance)
    def Exit(self):
        pass

name=input("enter the name of emp")
AadharNo=int(input("enter the AadharNo"))
Branch=input("enter the branch Name")

k=Bank(name,AadharNo,Branch)

while True:
    print("1. CreateAccount")
    print("2. Deposit")
    print("3. withdraw")
    print("4. Checkbal")
    print("5. Exit")
    x=int(input("enter the choice"))
    if(x==1):
        k.CreateAccount()
    elif(x==2):
        b=int(input("enter the deposit amount"))
        k.DepositAmount(b)
    elif(x==3):
        b2 = int(input("enter the withdraw amount"))
        k.WithdrawAmount(b2)
    elif(x==4):
        k.Checkbal()
    elif(x==5):
        break'''