from tkinter import * 
#from PIL import ImageTk 
from tkinter import messagebox
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("login system")
        self.root.geometry("1199x689+100+50")
        self.root.resizable(False,False)
        login_fram=Frame(self.root,bg="white")
        login_fram.place(x=360,y=200,width=500,height=400)
        
        Label(login_fram,text="Login Here",font="ar 20 bold",fg="black").place(x=100,y=30)
        Label(login_fram,text="UserName:",font="ar 15 bold",fg="black").place(x=90,y=100)
        Label(login_fram,text="Password:",font="ar 15 bold",fg="black").place(x=90,y=160)  
        self.username=Entry(login_fram,bg="white")  
        self.username.place(width=300,height=30,x=90,y=130) 
        self.password=Entry(login_fram,bg="white",show=".")  
        self.password.place(width=300,height=30,x=90,y=190) 
        Forget=Checkbutton(login_fram,text="forget password")
        Forget.place(x=90,y=220)
        login_button=Button(login_fram,command=self.condition,text="Login",font="ar 15 bold",bg="blue")
        login_button.place(x=100,y=270,width=100,height=50)
    def condition(self):
        if self.username.get()==""or self.password.get()=="":
            messagebox.showerror("Error","All field required fill",parent=self.root)
        elif self.username.get()!="Ali Abbas"or self.password.get()!="12345678":
            messagebox.showerror("Error","incorret username or password",parent=self.root)
        else:
            messagebox.showinfo("welcome" , f"{self.username.get()}")
root=Tk()
obj=login(root)
root.mainloop()