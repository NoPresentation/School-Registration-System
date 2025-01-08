import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib import pyplot as pl 
from database_handler import DatabaseHandler as db

class RegestrationForm(tk.Frame):
    
    def __init__(self, parent, refresh_callback):
        super().__init__(parent, padx=10, pady=10)

        self.refresh_callback = refresh_callback

        # Creating regestration form fields
        tk.Label(self, text = 'Full Name', ).pack(fill='x')
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text = 'Email').pack(fill='x')
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text = 'Age', ).pack(fill='x')
        self.age_box = ttk.Spinbox(self, from_= 6, to=20)
        self.age_box.pack()

        tk.Label(self, text = 'Gender', ).pack(fill = 'x')
        self.gender = tk.StringVar()
        tk.Radiobutton(self,text = 'Male' ,variable = self.gender ,value= 'Male').pack(anchor='w')
        tk.Radiobutton(self,text = 'Female' ,variable = self.gender ,value= 'Female').pack(anchor='w')
        
        #Creating regestration form buttons
        self.submit_button = tk.Button(self, text='Submit', command = self.submit_data).pack() # Submit button

        self.chart = tk.Button(self, text='Visualize gender statistis', command=self.show_chart).pack(side='left') # Visualization button


    def show_chart(self):
        stats = [db.get_male(), db.get_female()]

        # Error handling in case there is no data to visualize
        if stats[0] == 0 and stats[1] == 0:
            self.no_date = messagebox.showerror(title='NO DATA FOUND!', message = 'Please enter students data first to view the statistics.')
            return
        
        self.pie_chart = pl.pie(stats, labels=('Male Students', 'Female Students'), autopct='%1.1f%%')
        pl.show(block = False)

    def submit_data(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_box.get()
        gender = self.gender.get()

        # Error handling in case one of the fields is empty
        if name and email and age and gender:
            db.insert_student(name, email, age, gender)
            self.clear_form()
            self.refresh_callback()
        else:
            messagebox.showwarning(title = 'Uncomplete Data', message = 'You should enter all data before submitting.')

    # Making the form ready for re-use
    def clear_form(self):
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.age_box.set(10)
        self.gender.set('')