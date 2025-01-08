import tkinter as tk
from tkinter import ttk
from database_handler import DatabaseHandler as db

class StudentListing(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.table = ttk.Treeview(self, columns=('ID','Name', 'Email', 'Age', 'Gender'), show='headings')

        # Creating the column headings
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Email', text='Email')
        self.table.heading('Age', text='Age')
        self.table.heading('Gender', text='Gender')
        self.table.pack(fill=tk.BOTH, expand=True)
        
        self.load_students()


    def load_students(self):
        self.table.delete(*self.table.get_children())
        students = db.read_students()
        for student in students:
            self.table.insert('', tk.END, values=student)
