from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Window
from room import Roombooking
from details import DetailsRoom
from time import strftime  
from tkinter import messagebox
from staff import StaffPage


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title('Hotel Management System')
        self.root.attributes("-fullscreen", True)

        
        
        

#================1st image============
        img1=Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\hotel1.jpg")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

#==================logo=============
        img2=Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\logohotel.png")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #===========title============
        lbl_titel=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_titel.place(x=0,y=140,width=1550,height=50)

        #==========main frame==========
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #======menu=======
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        

        #=======btn frame========
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn = Button(btn_frame, text="DETAILS", command=self.details_login1, width=22,
                     font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        staff_btn=Button(btn_frame,text="STAFF",command=self.details_login2,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        staff_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)



        #=======right side image=======
        img3=Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)


        #==========down images========

        img4=Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\myh.jpg")
        img4 = img4.resize((230, 210), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)


        img5=Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\khana.jpg")
        img5 = img5.resize((230, 190), Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)

        self.clock_label = Label(self.root, font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        self.clock_label.place(x=1, y=140, width=230, height=50)
        self.update_clock()  # Start the clock

    def update_clock(self):
        
        current_time = strftime("%H:%M:%S")  # Get current time in HH:MM:SS format
        self.clock_label.config(text=current_time)  # Update the label with the current time
        self.clock_label.after(1000, self.update_clock)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Window(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_login1(self):
        self.login_window = Toplevel(self.root)
        self.login_window.title("Manager")
        self.login_window.geometry("300x200+550+300")

        Label(self.login_window, text="Username:").pack(pady=5)
        self.username_entry = Entry(self.login_window)
        self.username_entry.pack(pady=5)

        Label(self.login_window, text="Password:").pack(pady=5)
        self.password_entry = Entry(self.login_window, show="*")
        self.password_entry.pack(pady=5)

        Button(self.login_window, text="Login", command=self.verify_login1).pack(pady=10)

    def verify_login1(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.login_window.destroy()
            self.new_window = Toplevel(self.root)
            self.app = DetailsRoom(self.new_window)
        else:
            messagebox.showerror("Error", "Invalid Credentials", parent=self.login_window)


    def details_login2(self):
        self.login_window = Toplevel(self.root)
        self.login_window.title("Manager")
        self.login_window.geometry("300x200+550+300")

        Label(self.login_window, text="Username:").pack(pady=5)
        self.username_entry = Entry(self.login_window)
        self.username_entry.pack(pady=5)

        Label(self.login_window, text="Password:").pack(pady=5)
        self.password_entry = Entry(self.login_window, show="*")
        self.password_entry.pack(pady=5)

        Button(self.login_window, text="Login", command=self.verify_login2).pack(pady=10)

    def verify_login2(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.login_window.destroy()
            self.new_window = Toplevel(self.root)
            self.app = StaffPage(self.new_window)
        else:
            messagebox.showerror("Error", "Invalid Credentials", parent=self.login_window)
 
    def logout(self):
        self.root.destroy() 







if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
