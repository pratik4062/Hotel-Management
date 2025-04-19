from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
import re




def validate_number(input_text):
    return input_text.isdigit() and len(input_text) <= 10



def validate_email(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(email_pattern, email):
        return True
    return False

def validate_name(input_text):
    
    pattern = r'^[A-Za-z ]*$'  # Only alphabets and spaces allowed
    return re.match(pattern, input_text) is not None


class Cust_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1295x550+226+195")
        self.root.title('Hotel Management System')


        #========variable=====
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_adderss=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()



        #=====title=========
        lbl_titel=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_titel.place(x=0,y=0,width=1295,height=50)

        #=============logo=============
        img2=Image.open(r"C:\Users\Ramesh Potekar\Desktop\EMS\pi\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #============labelframe
        labeframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labeframeleft.place(x=5,y=50,width=425,height=490)

        name_vc = self.root.register(validate_name)

        #======label & entries===========
        lbl_cust_ref=Label(labeframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)


        ent_ref=ttk.Entry(labeframeleft,textvariable=self.var_ref,width=29,font=("arial",12,"bold"),state="readonly")
        ent_ref.grid(row=0,column=1)


        #======cust_name======
        cname=Label(labeframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname = ttk.Entry(labeframeleft, textvariable=self.var_cust_name, width=29, font=("arial", 12, "bold"),
                     validate="key", validatecommand=(name_vc, "%P"))
        txtcname.grid(row=1, column=1)

        

        #mothername
        lblmname=Label(labeframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname = ttk.Entry(labeframeleft, textvariable=self.var_mother, width=29, font=("arial", 12, "bold"),
                     validate="key", validatecommand=(name_vc, "%P"))
        txtmname.grid(row=2, column=1)

        #gender combobox
        label_gender=Label(labeframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labeframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #Postcode
        contactvc = labeframeleft.register(validate_number)

        lblPostCode=Label(labeframeleft,font=("arial",12,"bold"),text="PostCode:",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labeframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width=29,validate="all", validatecommand=(contactvc, "%P"))
        txtPostCode.grid(row=4,column=1)

        #mobilenumber
        mobile_vc = self.root.register(validate_number) 

        # Mobile Number Label
        lblMobile = Label(labeframeleft, font=("arial", 12, "bold"), text="Mobile:", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

# Mobile Number Entry with 10-digit validation
        txtMobile = ttk.Entry(labeframeleft, textvariable=self.var_mobile, font=("arial", 13, "bold"), width=29,
                      validate="key", validatecommand=(mobile_vc, "%P"))
        txtMobile.grid(row=5, column=1)


        #email
        lblEmail=Label(labeframeleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labeframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

        #Nationality
        lblNationality=Label(labeframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labeframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Indian","American","Canadian","Australian")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        #id proof type
        lblIdProof=Label(labeframeleft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labeframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Aadhaar Card","Pan Card","Passport","Driving Licence")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        #idnumber
        lblIdNumber=Label(labeframeleft,font=("arial",12,"bold"),text="Id Number:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labeframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        #Address
        lblAddress=Label(labeframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labeframeleft,textvariable=self.var_adderss,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=10,column=1)

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
        
        #tabel frame serach system

        Tabel_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Deatils And Search System",font=("arial",12,"bold"),padx=2)
        Tabel_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Tabel_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Tabel_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Tabel_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Tabel_Frame,command=self.search,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Tabel_Frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)


        #===show data table===========

        details_table=Frame(Tabel_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile",
                                             "email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif not validate_email(self.var_email.get()):
            messagebox.showerror("Invalid Input", "Email must contain '@' and '.' characters.",parent=self.root)
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into  customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                       self.var_ref.get(),
                                                                       self.var_cust_name.get(),
                                                                       self.var_mother.get(),
                                                                       self.var_gender.get(),
                                                                       self.var_post.get(),
                                                                       self.var_mobile.get(),
                                                                       self.var_email.get(),
                                                                       self.var_nationality.get(),
                                                                       self.var_id_proof.get(),
                                                                       self.var_id_number.get(),
                                                                       self.var_adderss.get()
                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
        my_cursor=conn.cursor()    
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()   

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]


        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_adderss.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("error","Please enter mobile number",parent=self.root)
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
            my_cursor=conn.cursor()    
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                
                                                                       
                                                                       self.var_cust_name.get(),
                                                                       self.var_mother.get(),
                                                                       self.var_gender.get(),
                                                                       self.var_post.get(),
                                                                       self.var_mobile.get(),
                                                                       self.var_email.get(),
                                                                       self.var_nationality.get(),
                                                                       self.var_id_proof.get(),
                                                                       self.var_id_number.get(),
                                                                       self.var_adderss.get(),
                                                                       self.var_ref.get()
                                                                                                      ))
            

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)
                
        
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
            my_cursor=conn.cursor() 
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value) 
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()  


    def reset(self):
       # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_adderss.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self): 
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="management")
        my_cursor=conn.cursor()  

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")  
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()







if __name__=="__main__":
    root=Tk()
    obj=Cust_Window(root)
    root.mainloop()