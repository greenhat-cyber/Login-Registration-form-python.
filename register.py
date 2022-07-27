from tkinter import *
from PIL import ImageTk
from tkinter import ttk, messagebox
import re
import pymysql


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False,False)
        self.root.config(bg="ORANGE")


#===========DATABASE==========
# Connecting to the Database where all information will be stored
#connector = sqlite3.connect('vehicle_new.db')
#cursor = connector.cursor()

#cursor.execute("CREATE TABLE IF NOT EXISTS VEHICLE_NEW (VEHICLE_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, NO_OF_VEHICLES TEXT, MONTH TEXT, TOT_AMNT TEXT)")


#=====Bgimage=======
        self.bg=ImageTk.PhotoImage(file='i1.jpg')
        Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
#====left image====
        self.left= ImageTk.PhotoImage(file="i2.png")
        left = Label(self.root, image=self.left).place(x=80, y=100)# relwidth=1, relheight=1)
#=====Register Frame===
        frame1=Frame(self.root,bg="orange",highlightthickness=2,highlightcolor="white")
        frame1.place(x=480,y=100,width=700,height=504)
        title=Label(frame1,text="REGESTER HERE",font=("times new roman",20,"bold"),bg="orange").place(x=50,y=30)
#=====ROW first name 1====
        f_name= Label(frame1, text="First name", font=("times new roman", 15, "bold"), bg="orange",fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,width=22,font=("times new roman",15))
        self.txt_fname.place(x=50,y=135,)
        l_name = Label(frame1, text="Last name", font=("times new roman", 15, "bold"), bg="orange", fg="black").place(x=400, y=101)
        self.txt_l_name = Entry(frame1,width=22,font=("times new roman", 15))
        self.txt_l_name.place(x=400, y=135)
# =====ROW last name 2====
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="orange", fg="black").place(x=50, y=167)
        self.txt_password = Entry(frame1,width=22,font=("times new roman", 15))
        self.txt_password.place(x=50, y=200)
        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="orange",fg="black").place(x=400, y=170)
        self.txt_cpassword = Entry(frame1,width=22,font=("times new roman", 15))
        self.txt_cpassword.place(x=400, y=200)
# =====ROW security q 3====
        security_Q= Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="orange",fg="black").place(x=50, y=237)

        self.cmb_quest=ttk.Combobox(frame1, font=("times new roman", 15),state='readonly',justify='center')
        self.cmb_quest['values']=("select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50, y=277)
        self.cmb_quest.current(0)
        Answer= Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="orange", fg="black").place(x=400,y=237)
        self.txt_Answer = Entry(frame1,width=22,font=("times new roman", 15,))
        self.txt_Answer.place(x=400, y=277)
# Email==
        email= Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="orange", fg="black").place(x=400, y=312)
        self.txt_email =Entry(frame1, width=22, font=("times new roman", 15,))
        self.txt_email.place(x=400, y=350)





#=====TERMS===
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms&Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="orange",font=("times new roman",12)).place(x=50,y=380)
        self.btn_img=ImageTk.PhotoImage(file="i3.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        btn_sign_in=Button(frame1,text="Sign In",bg="orange",font=("times new roman",'20'), bd=0, cursor="hand2",command=self.Sign_in).place(x=340, y=413)


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_l_name.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_Answer.delete(0, END)
        self.cmb_quest.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)

    def Sign_in(self):
        self.root.destroy()
        import login


            



    def register_data(self):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if self.txt_fname.get()=="" or self.txt_l_name.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="" "Select" or self.txt_Answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All fields required",parent=self.root)


        

        elif self.txt_password.get()!= self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password Should be same..",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please accecpt our terms & condition",parent=self.root)

        elif re.fullmatch(pattern, self.txt_email.get()) is None:
            messagebox.showerror("Error","enter valid email!!",parent=self.root)
            
        else:

            try:
                con= pymysql.connect(host="localhost",user="root",password="sherin",database="srz esports")
                cur=con.cursor()
                cur.execute("select * from players where email=%s",self.txt_email.get())
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","User already exits,Please try another email.", parent=self.root)

                else:
                    cur.execute("insert into players(f_name,l_name,email,question,answer,password)values(%s,%s,%s,%s,%s,%s)",

                            (self.txt_fname.get(),
                             self.txt_l_name.get(),
                             self.txt_email.get(),
                             self.cmb_quest.get(),
                             self.txt_Answer.get(),
                             self.txt_password.get()
                             ))
                con.commit()
                con.close()
                self.clear()
                messagebox.showinfo("Sucess", "Register Sucessfull", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"error due to: {str(es)}",parent=self.root)



root=Tk()
obj=Register(root)
root.mainloop()
