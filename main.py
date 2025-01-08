import tkinter as tk
from tkinter import messagebox
import matplotlib as mpl

import regestration_form as rf
from student_listing import StudentListing

class MainApplication(tk.Tk): # Our main class inherits the TK class from tkinter library
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        self.geometry("900x600")
        self.create_widgets() 
        messagebox.showinfo(title='Hint', message='Use the program in full-screen mode :)')

    def create_widgets(self):
        # First widget: The title widget for displaying the application name
        title_label = tk.Label(self, text = 'School Regestration System', font = ('Helvetica', 16))
        title_label.pack(side = 'top', fill='x')

        # Second widget: The regestraton form to enter and visualize data
        self.regestration_form = rf.RegestrationForm(self, self.refresh_students)
        self.regestration_form.pack(side='left', fill='y', padx=10, pady=10)

        # Third widget: To view students' table
        self.student_listing = StudentListing(self)
        self.student_listing.pack(side='right', fill='both', padx=10, pady=10, expand=True)

        
    

    def refresh_students(self):
        self.student_listing.load_students()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()