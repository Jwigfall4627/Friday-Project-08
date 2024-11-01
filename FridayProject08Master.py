import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3


# Function to create the database and table if they do not exist
def create_database():
    connection = sqlite3.connect("SampleDatabase1.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()


class FeedBackApp:
    def __init__ (self,root):
        #Main Window
        self.root = root
        self. root.title("Customer Feedback App")
        #Creating my labels
        self.Label1= tk.Label(root, text="Hello, We Value Your Feedback. Please submit your feedback down below")
        self.Label1.pack()

        self.Label2=tk.Label(root, text="Please enter your first Name and Last Name")
        self.Label2.pack()

        self.firstLastName = tk.Entry(root,)
        self.firstLastName.pack()

        self.Label3 = tk.Label(root, text="Please Enter your email")
        self.Label3.pack()

        self.email = tk.Entry(root,)
        self.email.pack()

        self.label4 = tk.Label(root, text="Please Enter your feedback")
        self.label4.pack()

        self.feedback = tk.Entry(root,)
        self.feedback.pack()

        self.Button1 = tk.Button(root, text="Please Submit", command=self.DisplaysUserData)
        self.Button1.pack()

        self.view_feedback_btn = tk.Button(root, text="View All Feedback (Admin)", command=self.adminacess)
        self.view_feedback_btn.pack(pady=5)

    def DisplaysUserData(self):
        username = self.firstLastName.get().strip()
        email = self.email.get().strip()
        feedback = self.feedback.get().strip()

         # Save feedback to the database
        self.saveToDatabase(username, email, feedback)
        # Show feedback in a message box
        messagebox.showinfo("User Feedback", f"Name: {username}\nEmail: {email}\nFeedback: {feedback}")
        # Clear input fields after submission
        self.firstLastName.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.feedback.delete(0, tk.END)

    def saveToDatabase(self , name, email, feedback):
        connection = sqlite3.connect("SampleDatabase1.db")
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)
        ''', (name, email, feedback))
        connection.commit()
        connection.close()
        print(f"Saved Feedback: Name: {name}, Email: {email}, Feedback: {feedback}")


    def show_all_feedback(self):
        # Retrieve and display all feedback entries
        connection = sqlite3.connect("SampleDatabase1.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM feedback")
        rows = cursor.fetchall()
        connection.close()

        print("\n--- All Feedback Entries ---")
        for row in rows:
            print(f"ID: {row[0]}, username: {row[1]}, Email: {row[2]}, Feedback: {row[3]}")
        print("\n--- End of Entries ---")
    def adminacess (self):
        password = simpledialog.askstring("Admin Access", "Enter Admin Password:", show='*')
        if password == "admin123":  # Password check for simplicity (use a secure method in production)
            self.show_all_feedback()
        else:
            messagebox.showerror("Access Denied", "Incorrect password!")





#connect_to_db()
create_database()
root = tk.Tk()
app = FeedBackApp(root)
root.mainloop()




#label2.input("")

# width=30, height=5 line 10
# Line 9 padx=2, pady=2