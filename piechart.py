import tkinter as tk
from tkinter import messagebox
from matplotlib import pyplot as pl
from database_handler import DatabaseHandler as db

tk.Message

class Pie(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.show_chart = tk.Button(self, text='Show gender statistis', command=self.chart)
        self.show_chart.pack(side='left')


    def chart(self):
        stats = [db.get_male(), db.get_female()]
        if stats[0] == 0 and stats[1] == 0:
            self.no_date = messagebox.showerror(title='NO DATA FOUND!', message = 'Please enter students data first to view the statistics.')
            return
        self.pie_chart = pl.pie(stats, labels=('male', 'female'))
        pl.show(block = False)
        
            