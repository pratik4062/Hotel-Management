from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class UserPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500+350+150")
        self.root.title("User Information & Feedback")

        self.var_ref = StringVar()
        self.var_feedback = StringVar()

        # Title
        lbl_title = Label(self.root, text="USER INFORMATION", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X)

        # Reference Number Entry
        lbl_ref = Label(self.root, text="Enter Reference Number:", font=("arial", 12, "bold"))
        lbl_ref.place(x=50, y=60)
        
        entry_ref = Entry(self.root, textvariable=self.var_ref, font=("arial", 12))
        entry_ref.place(x=250, y=60, width=150)

        btn_fetch = Button(self.root, text="Fetch Details", font=("arial", 12, "bold"), bg="black", fg="gold", command=self.fetch_details)
        btn_fetch.place(x=420, y=58, width=120)

        # Frame for Displaying User & Room Details
        self.details_frame = LabelFrame(self.root, text="User & Room Details", font=("arial", 12, "bold"))
        self.details_frame.place(x=50, y=100, width=700, height=200)

        self.details_text = Text(self.details_frame, font=("arial", 12), width=80, height=8)
        self.details_text.pack(padx=10, pady=10)

        # Feedback Section
        lbl_feedback = Label(self.root, text="Your Feedback:", font=("arial", 12, "bold"))
        lbl_feedback.place(x=50, y=320)

        self.txt_feedback = Entry(self.root, textvariable=self.var_feedback, font=("arial", 12), width=50)
        self.txt_feedback.place(x=180, y=320)

        btn_submit = Button(self.root, text="Submit Feedback", font=("arial", 12, "bold"), bg="black", fg="gold", command=self.submit_feedback)
        btn_submit.place(x=350, y=360, width=150)

    def fetch_details(self):
        ref_number = self.var_ref.get()

        if ref_number == "":
            messagebox.showerror("Error", "Please enter a reference number", parent=self.root)
            return

        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        cursor = conn.cursor()

        # Fetch user details
        cursor.execute("SELECT Name, Email, Mobile, Gender, PostCode, Mobile, Nationality, Idproof, Idnumber, Address FROM customer WHERE Ref=%s", (ref_number,))
        user_data = cursor.fetchone()

        # Fetch room details

        conn.close()

        if user_data:
            details_text = f"""
            Name: {user_data[0]}
            Email: {user_data[1]}
            Mobile: {user_data[2]}
            Gender: {user_data[3]}
            PostCode: {user_data[4]}
            Mobile: {user_data[5]}
            Nationality: {user_data[6]}
            Idproof: {user_data[7]}
            Idnumber: {user_data[8]}
            Address: {user_data[9]}
          
            """
            self.details_text.delete("1.0", END)
            self.details_text.insert(END, details_text)
        else:
            messagebox.showerror("Error", "No records found for this reference number", parent=self.root)

    def submit_feedback(self):
        ref_number = self.var_ref.get()
        feedback_text = self.var_feedback.get()

        if ref_number == "" or feedback_text == "":
            messagebox.showerror("Error", "Please enter reference number and feedback", parent=self.root)
            return

        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        cursor = conn.cursor()

        # Insert feedback into a feedback table (create table if not exists)
        cursor.execute("CREATE TABLE IF NOT EXISTS feedback (Ref VARCHAR(20), Feedback TEXT)")
        cursor.execute("INSERT INTO feedback (Ref, Feedback) VALUES (%s, %s)", (ref_number, feedback_text))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Feedback submitted successfully!", parent=self.root)
        self.var_feedback.set("")

# Run the User Page
if __name__ == "__main__":
    root = Tk()
    obj = UserPage(root)
    root.mainloop()
