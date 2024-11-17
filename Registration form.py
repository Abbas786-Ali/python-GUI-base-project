from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("350x330")
root.resizable(False,False)
Label(root,text=' Registration form',font="ar 15 bold").grid(row=8,column=2)
Name=Label(root,text="Name:",font="ar 12 bold")
phone=Label(root,text="Phone:",font="ar 12 bold")
gender=Label(root,text="Gender:",font=" ar 12 bold")
address=Label(root,text="Address:",font="ar 12 bold")
email=Label(root,text="Email Id:",font="ar 12 bold")
password=Label(root,text="Password:",font="ar 12 bold")
Name.grid(row=60,column=1)
phone.grid(row=80,column=1)
gender.grid(row=95,column=1)
address.grid(row=120,column=1)
email.grid(row=130,column=1)
password.grid(row=210,column=1)

namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
addressvalue=StringVar
emailvalue=StringVar
passwordvalue=StringVar
checkvalue=IntVar
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
addressentry=Entry(root,textvariable=addressvalue)
emailentry=Entry(root,textvariable=addressvalue)
passwordentry=Entry(root,textvariable=addressvalue,show=".")
nameentry.grid(row=60,column=2)
phoneentry.grid(row=80,column=2)
genderentry.grid(row=95,column=2)
addressentry.grid(row=120,column=2)
emailentry.grid(row=130,column=2)
passwordentry.grid(row=210,column=2)
checkbutton=Checkbutton(text="remember me?",variable=checkvalue)
checkbutton.grid(row=230,column=2)
def getvals():
    print ("you registred succesfully")
Button(text="Registred",bg='blue',command=getvals).grid(row=280,column=2)
root.mainloop()