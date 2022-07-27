from tkinter import *
import pymysql
from PIL import ImageTk
from tkinter import messagebox
import re

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1119x600+100+50")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="b3image.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        ## frame login
        Frame_login=Frame(self.root,bg="black")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="black").place(x=90,y=30)
        decs = Label(Frame_login, text="Players login area", font=("Goudy", 15, "bold"), fg="#d25d17", bg="black").place(x=90,y=100)
        #username
        lbl_user = Label(Frame_login, text="Email", font=("Goudy", 15, "bold"), fg="gray",bg="black").place(x=90, y=140)
        self.txt_email=Entry(Frame_login,font=("time new roman",15),bg="lightgray")
        self.txt_email.place(x=90,y=170,width=350,height=35)
        #password
        lbl_password = Label(Frame_login, text="Password", font=("Goudy", 15, "bold"), fg="gray", bg="black").place(x=90,y=210)
        self.txt_password = Entry(Frame_login, font=("time new roman", 15), bg="lightgray")
        self.txt_password.place(x=90, y=240, width=350, height=35)
        forget = Button(Frame_login, text="Regiter new account",command=self.REGISTER_win,bg="black",fg="#d77337",bd=0,font=("times new roman",12)).place(x=150,y=280)
        Login = Button(Frame_login, text="Login ||",command=self.login, bg="black", fg="#d77337", bd=0,font=("times new roman", 13)).place(x=90, y=280)




   
    def REGISTER_win(self):
        self.root.destroy()
        import register

            



    def login(self):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if self.txt_email.get() =="" or self.txt_password.get()=="":
            messagebox.showerror("ERROR","ALL Fields are required",parent=self.root)
        elif re.fullmatch(pattern, self.txt_email.get()) is None:
            messagebox.showerror("Error","enter valid email!!",parent=self.root)
        else:
            try:
                con=pymysql.Connect(host="localhost",user="root",password="sherin",database="srz esports")
                cur=con.cursor()
                cur.execute("select * from players where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row== None:
                    messagebox.showerror("Error","invalid email and password", parent=self.root)
                else:
                    messagebox.showinfo("Admin", "You are the clan leader", parent=self.root)
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"error due to:{str(es)}",parent=self.root)

root=Tk()
obj=Login(root)
root.mainloop()
