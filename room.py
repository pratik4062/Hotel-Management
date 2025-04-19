from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from tkcalendar import Calendar
from reportlab.pdfgen import canvas
from tkinter.filedialog import asksaveasfilename



class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1295x550+226+195")
        self.root.title('Hotel Management System')

        #======variables=======
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_noofpeoples=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

         #=====title=========
        lbl_titel=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_titel.place(x=0,y=0,width=1295,height=50)


        #=============logo=============
        img2=Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

      #============labelframe
        labeframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("times new roman",12,"bold"),padx=2)
        labeframeleft.place(x=5,y=50,width=425,height=490)

      #======label & entries===========
        lbl_cust_contact=Label(labeframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)


        ent_contact=ttk.Entry(labeframeleft,textvariable=self.var_contact,width=20,font=("arial",12,"bold"))
        ent_contact.grid(row=0,column=1,sticky=W)

        #fetch data button
        btnFetchData=Button(labeframeleft,command=self.Fetch_Contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)

        #check in date
        check_in_date=Label(labeframeleft,font=("arial",12,"bold"),text="Check In Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labeframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=20)
        txtcheck_in_date.grid(row=1,column=1,sticky=W)

        btn_checkin = Button(labeframeleft, text="Select Date", command=lambda: self.open_calendar(self.var_checkin, is_checkin=True),
                     font=("arial", 8, "bold"), bg="black", fg="gold", width=10)
        btn_checkin.place(x=345, y=40)

        #check out date
        lbl_check_out=Label(labeframeleft,font=("arial",12,"bold"),text="Check Out Date:",padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        txt_check_out=ttk.Entry(labeframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=20)
        txt_check_out.grid(row=2,column=1,sticky=W)

        btn_checkout = Button(labeframeleft, text="Select Date", command=lambda: self.open_calendar(self.var_checkout, is_checkin=False),
                      font=("arial", 8, "bold"), bg="black", fg="gold", width=10)
        btn_checkout.place(x=345, y=75)

        #room type
        label_RoomType=Label(labeframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
        my_cursor=conn.cursor()    
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labeframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=25,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Available Room
        lblRoomAvailable=Label(labeframeleft,font=("arial",12,"bold"),text="Available Room:",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        #txtRoomAvailable=ttk.Entry(labeframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        #txtRoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
        my_cursor=conn.cursor()    
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labeframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=25,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        #No Of peoples
        lblNoOfpeoples=Label(labeframeleft,font=("arial",12,"bold"),text="No Of Peoples:",padx=2,pady=6)
        lblNoOfpeoples.grid(row=5,column=0,sticky=W)
        txtNoOfpeople=ttk.Entry(labeframeleft,textvariable=self.var_noofpeoples,font=("arial",13,"bold"),width=29)
        txtNoOfpeople.grid(row=5,column=1)

        #No Of Days
        lblNoOfDays=Label(labeframeleft,font=("arial",12,"bold"),text="No Of Days:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labeframeleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        #paid tax
        lblNoOfDays=Label(labeframeleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNlblNoOfDays=ttk.Entry(labeframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtNlblNoOfDays.grid(row=7,column=1)

        #Sub Total
        lblNoOfDays=Label(labeframeleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNlblNoOfDays=ttk.Entry(labeframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtNlblNoOfDays.grid(row=8,column=1)

        #Total Cost
        lblIdNumber=Label(labeframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labeframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        #=====bill button====
        btnBil=Button(labeframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBil.grid(row=10,column=0,padx=1,sticky=W)

        btnPrintBill = Button(labeframeleft, text="Print Bill", command=self.generate_bill, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnPrintBill.grid(row=10, column=1, padx=1, sticky=W)

   



        #======btns======
        btn_frame=Frame(labeframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #====rightside image======
        img3=Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\bed.jpg")
        img3 = img3.resize((520, 220), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=220)


        #tabel frame serach system

        Tabel_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Deatils And Search System",font=("arial",12,"bold"),padx=2)
        Tabel_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Tabel_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Tabel_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Tabel_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Tabel_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Tabel_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #===show data table===========

        details_table=Frame(Tabel_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","noofpeoples",
                                             "noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check In")
        self.room_table.heading("checkout",text="Check Out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("noofpeoples",text="noofpeoples")
        self.room_table.heading("noofdays",text="NoOfDays")
        
        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("noofpeoples",width=100)
        self.room_table.column("noofdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    def open_calendar(self, date_var, is_checkin=False):
      top = Toplevel(self.root)  # Define the Toplevel window
      top.title("Select Date")
      top.geometry("250x250+550+300")

    # Get today's date
      today = datetime.now()

    # Create a calendar widget
      cal = Calendar(top, selectmode='day', year=today.year, month=today.month, day=today.day, date_pattern="dd/mm/yy")
      cal.pack(pady=20)

      def grab_date():
        selected_date = cal.get_date()
        selected_date_obj = datetime.strptime(selected_date, "%d/%m/%y")

        # Validation for Check-In date (cannot select past dates)
        if is_checkin and selected_date_obj < today.replace(hour=0, minute=0, second=0, microsecond=0):
            messagebox.showerror("Error", "Check-In date cannot be in the past.", parent=top)
            return

        # Validation for Check-Out date (must be after Check-In date)
        if not is_checkin and self.var_checkin.get():
            checkin_date_obj = datetime.strptime(self.var_checkin.get(), "%d/%m/%y")
            if selected_date_obj <= checkin_date_obj:
                messagebox.showerror("Error", "Check-Out date must be after Check-In date.", parent=top)
                return

        # Update the date variable
        date_var.set(selected_date)
        top.destroy()

      btn_select = Button(top, text="Select", command=grab_date)
      btn_select.pack(pady=10)

#===========Add Data=========
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into  room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                      self.var_contact.get(),
                                                                      self.var_checkin.get(),
                                                                      self.var_checkout.get(),
                                                                      self.var_roomtype.get(),
                                                                      self.var_roomavailable.get(),
                                                                      self.var_noofpeoples.get(),
                                                                      self.var_noofdays.get()
                                                                    
                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)

   
   #======fetch data=====
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
        my_cursor=conn.cursor()    
        my_cursor.execute("select * from room")
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

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_noofpeoples.set(row[5])
        self.var_noofdays.set(row[6])


 #====update=======
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","Please enter mobile number",parent=self.root)
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
            my_cursor=conn.cursor()    
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,noofpeoples=%s,noofdays=%s where Contact=%s",(
                                                                                                                
                                                                       
                                                                       self.var_checkin.get(),
                                                                       self.var_checkout.get(),
                                                                       self.var_roomtype.get(),
                                                                       self.var_roomavailable.get(),
                                                                       self.var_noofpeoples.get(),
                                                                       self.var_noofdays.get(),
                                                                       self.var_contact.get()
                                                                                  ))
            

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)       


#=======delete======
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
            my_cursor=conn.cursor() 
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value) 
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

        #=====reset======
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_noofpeoples.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

        #=======all data fetch==========

    def Fetch_Contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Customer Ref",parent=self.root)    
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
            my_cursor=conn.cursor()
            query=("Select Name from customer where Ref=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Ref Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("Select Gender from customer where Ref=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #======email===========
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("Select Email from customer where Ref=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)

                #nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("Select Nationality from customer where Ref=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                #Address
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("Select Address from customer where Ref=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)

                lbl5=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)


    
    #=====search system======
    
    def search(self): 
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
        my_cursor=conn.cursor()  

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")  
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()



   

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%y")
        outDate = datetime.strptime(outDate, "%d/%m/%y")
        no_of_days = (outDate - inDate).days
        self.var_noofdays.set(abs(no_of_days))

        if (self.var_roomtype.get()=="Single"):
            q1=float(500)
            q2=float(self.var_noofpeoples.get())
            q3=float(self.var_noofdays.get())
            q5=float(q1*q2*q3)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_roomtype.get()=="Double"):
            q1=float(1000)
            q2=float(self.var_noofpeoples.get())
            q3=float(self.var_noofdays.get())
            q5=float(q1*q2*q3)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 

        elif (self.var_roomtype.get()=="Luxary"):
            q1=float(1500)
            q2=float(self.var_noofpeoples.get())
            q3=float(self.var_noofdays.get())
            q5=float(q1*q2*q3)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)  

    def generate_bill(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter a contact number", parent=self.root)
            return

    # Ask user where to save the PDF
        filename = asksaveasfilename(defaultextension=".pdf", 
                                 filetypes=[("PDF files", "*.pdf")],
                                 title="Save Bill As",
                                 parent=self.root)

        if not filename:  # If user cancels the save dialog, return
           return

    # Create a PDF file
        pdf = canvas.Canvas(filename)
        pdf.setFont("Helvetica", 14)

        pdf.drawString(100, 750, "Hotel Management System")
        pdf.drawString(100, 730, "Billing Details")
        pdf.drawString(100, 710, f"Customer Contact: {self.var_contact.get()}")
        pdf.drawString(100, 690, f"Check-in Date: {self.var_checkin.get()}")
        pdf.drawString(100, 670, f"Check-out Date: {self.var_checkout.get()}")
        pdf.drawString(100, 650, f"Room Type: {self.var_roomtype.get()}")
        pdf.drawString(100, 630, f"Total Amount: {self.var_total.get()}")

        pdf.save()  # Save the PDF file
        messagebox.showinfo("Success", "Bill Generated & Saved Successfully!", parent=self.root)

     










if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
