import tkinter as tk
from tkinter import ttk
import database_handler as db

class RegestrationForm(tk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text = 'Full Name', ).pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text = 'Email').pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text = 'Age', ).pack()
        self.age_box = ttk.Spinbox(self, from_= 6, to=20)
        self.age_box.pack()

        tk.Label(self, text = 'Gender', ).pack()
        self.gender = tk.StringVar()
        tk.Radiobutton(self,text = 'Male' ,variable = self.gender ,value= 'Male').pack()
        tk.Radiobutton(self, text = 'Female', variable = self.gender, value = 'Female' ).pack()

        self.submit_button = tk.Button(self, text='Submit', command = self.submit_data).pack()


    def submit_data(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_box.get()
        gender = self.gender.get()

        if name and email and age and gender:
            db.DatabaseHandler.insert_student(name, email, age, gender)
            self.clear_form()


    def clear_form(self):
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.age_box.set(10)
        self.gender.set(None)