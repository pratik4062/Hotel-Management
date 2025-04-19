from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox



class StaffPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1295x550+226+195")
        self.root.title("Staff Management")

        # Title
        lbl_title = Label(self.root, text="STAFF MANAGEMENT", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X)

        # Frame for table
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Registered Users", font=("arial", 12, "bold"))
        Table_Frame.place(x=10, y=50, width=780, height=400)

        # Scrollbars
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.staff_table = ttk.Treeview(Table_Frame, columns=("fname", "lname", "contact", "email","password"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)

        # Define Table Headings
        self.staff_table.heading("fname", text="First Name")
        self.staff_table.heading("lname", text="Last Name")
        self.staff_table.heading("contact", text="Contact")
        self.staff_table.heading("email", text="Email")
        self.staff_table.heading("password", text="Password")
        
        
        self.staff_table["show"] = "headings"

        # Define Column Widths
        self.staff_table.column("fname", width=100)
        self.staff_table.column("lname", width=100)
        self.staff_table.column("contact", width=120)
        self.staff_table.column("email", width=120)
        self.staff_table.column("password", width=100)

        self.staff_table.pack(fill=BOTH, expand=1)
        self.staff_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT fname, lname, contact, email, password FROM register")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:
                self.staff_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.staff_table.focus()
        content = self.staff_table.item(cursor_row)
        row = content["values"]
        print("Selected Row:", row)  # Optional: Debugging
