import tkinter

class MainApplication(tkinter.Tk): # Now, our main class inherits the TK class from tkinter library
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        self.geometry("900x600")
        self.create_widgets()

    def create_widgets(self):
        title_label = tkinter.Label(self, text = 'School Regestration System', font = ('Helvetica', 16))
        title_label.pack(side = 'top', fill='x')



if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()