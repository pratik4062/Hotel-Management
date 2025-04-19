from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import time
import datetime
from hotel import HotelManagementSystem
from customer import Cust_Window
from room import Roombooking
from details import DetailsRoom
import user


def main():
     win=Tk()
     app=Login_Window(win)
     win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1 = Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)
        lblimg1.image = photoimage1

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)
        #=====label===
        username=lbl=Label(frame,text="Username",font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=190,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        password.place(x=70,y=235)

        self.txtpass=ttk.Entry(frame,font=("times new roman",20,"bold"),show="*")
        self.txtpass.place(x=40,y=270,width=270)

#==icon images=====
        img2 = Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\LoginIconAppl.png")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
        photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=330, width=25, height=25)
        lblimg1.image = photoimage2

        img3 = Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\lock-512.png")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
        photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=410, width=25, height=25)
        lblimg1.image = photoimage3
#===============login button=========
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=320,width=120,height=35)

        #===========registerbutton=========
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=370,width=160)

#======= forget password button===========
        loginbtn=Button(frame,text="Forget Password",command=self.forget,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=10,y=390,width=160)

        userbtn=Button(frame,text="User",command=self.user,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        userbtn.place(x=250,y=390,width=60)

    def register_window(self):
         self.new_window=Toplevel(self.root)
         self.app=register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Field Are Required")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="pass@123":
             messagebox.showinfo("Success","Welcome To Hotel Management System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                   self.txtuser.get(),
                                                                   self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=HotelManagementSystem(self.new_window)
                else:
                        if not open_main:
                                return
            conn.commit()
            conn.close()

#==========reset password=========
    def reset_pass(self):
         if self.combo_security_q.get()=="Select":
              messagebox.showerror("Error","Select Security Question",parent=self.root2)
         elif self.txt_security.get()=="":
              messagebox.showerror("Error","Please Enter The Answer",parent=self.root2)
         elif self.txt_newpass.get()=="":
              messagebox.showerror("Error","Please Enter The New Password",parent=self.root2)
         else:
              conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
              my_cursor=conn.cursor()
              qury=("select * from register where email=%s and securityq=%s and securitya=%s")
              vlaue=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get(),)
              my_cursor.execute(qury,vlaue)
              row=my_cursor.fetchone()
              if row==None:
                   messagebox.showerror("Error","Please Enter The Correct Answer",parent=self.root2)
              else:
                   query=("update register set password=%s where email=%s")
                   value=(self.txt_newpass.get(),self.txtuser.get())
                   my_cursor.execute(query,value)

                   conn.commit()
                   conn.close()
                   messagebox.showinfo("Info","Your Password Has Been Reset ,Please Login New Password",parent=self.root2)
                   self.root2.destroy()
              

#===================forget password==============
    def forget(self):
             if self.txtuser.get()=="":
                  messagebox.showerror("Error","Please Enter The Email Address To Reset Password")
             else:
                  conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                  my_cursor=conn.cursor()
                  query=("select * from register where email=%s")
                  value=(self.txtuser.get(),)
                  my_cursor.execute(query,value)
                  row=my_cursor.fetchone()
                  #print(row)

                  if row==None:
                       messagebox.showerror("My Error","Please Enter The Valid User Name")
                  else:
                       conn.close()
                       self.root2=Toplevel()
                       self.root2.title("Forget Password")
                       self.root2.geometry("340x450+610+170")

                       l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                       l.place(x=0,y=10,relwidth=1)
                       security_q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                       security_q.place(x=50,y=80)

                       self.combo_security_q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                       self.combo_security_q["values"]=("Select","Your Birth Place","Your Pet Name")
                       self.combo_security_q.place(x=50,y=110,width=250)
                       self.combo_security_q.current(0)

                       security_a=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                       security_a.place(x=50,y=150)

                       self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                       self.txt_security.place(x=50,y=180,width=250)

                       new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                       new_password.place(x=50,y=220)

                       self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                       self.txt_newpass.place(x=50,y=250,width=250)

                       btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                       btn.place(x=100,y=290)
    
    def user(self):
        self.new_window=Toplevel(self.root)
        self.app=user.UserPage(self.new_window)
                  

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #===text variables==
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        



#=============bg image============
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


#=============left image============
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\thought-good-morning-messages-LoveSove.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

#===========main frame=========
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #======lable & entries========
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)


        security_q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_q["values"]=("Select","Your Birth Place","Your Pet Name")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)

        security_a=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_a.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securitya,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #========check button========
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #=====buttons=========
        
        img = Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\register-now-button1.jpg")
        img = img.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage,command=self.register_data, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\loginpng.png")
        img1 = img1.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=200)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="Select":
                messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get()!= self.var_confpass.get():
                messagebox.showerror("Error","Password & Confirm Password Must Be Same")
        elif self.var_check.get()==0:
                messagebox.showerror("Error","Please Agree Our Terms & Condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exists,Please Try Another Mail")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                          self.var_fname.get(),
                                                                                          self.var_lname.get(),
                                                                                          self.var_contact.get(),
                                                                                          self.var_email.get(),
                                                                                          self.var_securityq.get(),
                                                                                          self.var_securitya.get(),
                                                                                          self.var_pass.get()

                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
         self.root.destroy()









if __name__=="__main__":
     main()