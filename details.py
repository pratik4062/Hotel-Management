
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

# Function to validate numeric input
def validate_number(input_text):
    return input_text.isdigit() or input_text == ""

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1295x550+226+195")
        self.root.title('Hotel Management System')

         #=====title=========
        lbl_titel=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_titel.place(x=0,y=0,width=1295,height=50)


        #=============logo=============
        img2=Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

      #============LabelFrame===========
        labeframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2)
        labeframeleft.place(x=5,y=50,width=540,height=350)
        contactvc = labeframeleft.register(validate_number)

#=======floor
        lbl_floor=Label(labeframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        ent_floor=ttk.Entry(labeframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"),validate="all", validatecommand=(contactvc, "%P"))
        ent_floor.grid(row=0,column=1,sticky=W)

        #=======room no
        lbl_RoomNo=Label(labeframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_roomno=StringVar()
        ent_RoomNo=ttk.Entry(labeframeleft,textvariable=self.var_roomno,width=20,font=("arial",13,"bold"),validate="all", validatecommand=(contactvc, "%P"))
        ent_RoomNo.grid(row=1,column=1,stick=W)

        #====room type
        lbl_RoomType=Label(labeframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_roomtype=StringVar()
        ent_RoomType=ttk.Entry(labeframeleft,textvariable=self.var_roomtype,width=20,font=("arial",13,"bold"))
        ent_RoomType.grid(row=2,column=1,sticky=W)

#==========btns===========
        btn_frame=Frame(labeframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #==Frame========
        Tabel_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2)
        Tabel_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Tabel_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Tabel_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Tabel_Frame,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="RoomNo")
        self.room_table.heading("roomtype",text="RoomType")
       
        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
     
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into  details values(%s,%s,%s)",(
                                                                      self.var_floor.get(),
                                                                      self.var_roomno.get(),
                                                                      self.var_roomtype.get(),
                                                                    
                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","New Room Added Succesfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)



 #======fetch data=====
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
        my_cursor=conn.cursor()    
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close() 

        #=========get cursor======
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])

    #====update=======
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("error","Please Enter Floor Number",parent=self.root)
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
            my_cursor=conn.cursor()    
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                                
                                                                       
                                                                       self.var_floor.get(),
                                                                       self.var_roomtype.get(),
                                                                       self.var_roomno.get()
                                                                                  ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated successfully",parent=self.root)       
    
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this Room Details",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
            my_cursor=conn.cursor() 
            query="delete from details where RoomNo=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value) 
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("")


