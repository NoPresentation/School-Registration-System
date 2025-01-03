import tkinter
import regestration_form as rf
from student_listing import StudentListing

class MainApplication(tkinter.Tk): # Now, our main class inherits the TK class from tkinter library
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        self.geometry("900x600")
        self.create_widgets()

    def create_widgets(self):
        title_label = tkinter.Label(self, text = 'School Regestration System', font = ('Helvetica', 16))
        title_label.pack(side = 'top', fill='x')


        self.regestration_form = rf.RegestrationForm(self, self.refresh_students)
        self.regestration_form.pack(side='left', fill='y', padx=10, pady=10)

        self.student_listing = StudentListing(self)
        self.student_listing.pack(side='right', fill='both', padx=10, pady=10, expand=True)

    def refresh_students(self):
        self.student_listing.load_students()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()