#! /usr/bin/env python

import Tkinter as Tk
import bbr as B

class Frame(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.label=Tk.Label(self, text='click me!', width=32, height=2, font=('Helvetica', '8'), fg='white', bg='black')
        self.label.pack(fill=Tk.BOTH)
        self.bind_all('<1>', self.heating_start)

    def heating_start(self, event):
        self.temp=1000
        self.label.configure(width=12, height=1, text='Hello world!', font=('Helvetica', '24'), fg='black')
        self.after(100, self.heating)

    def heating(self):
         self.label.configure(fg=B.bbrcolor_rel(self.temp))
         self.temp += 50
         if self.temp < 8000:
             self.after(100, self.heating)
         else:
             self.label.configure(fg='black', bg='white')
    

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()

