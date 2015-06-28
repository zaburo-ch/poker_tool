#! /usr/bin/env python

"""
filebox.py

This demonstration script prompts the user to select a file.

June 17, 2005
"""

import Tkinter as Tk
import tkFileDialog as Fd
import template as A

class File_Selector(Tk.Frame):
    def __init__(self, master, open_save):
        Tk.Frame.__init__(self, master)
        self.master=master
        label = Tk.Label(self, text='Select a file to %s: ' % open_save)
        label.pack(side=Tk.LEFT, padx=3)
        self.entry = Tk.Entry(self, width=40)
        self.entry.pack(side=Tk.LEFT, padx=3)
        button=Tk.Button(self, text='Browse...', command = (open_save == 'open' and self.open or self.save))
        button.pack(side=Tk.LEFT, padx=3)

    def open(self):
        self.open_or_save(Fd.askopenfilename)
        

    def save(self):
        self.open_or_save(Fd.asksaveasfilename)
        

    def open_or_save(self, fun):
        fname = fun(filetypes=[('Text files',('*.txt', '*.doc')),
                                             ('Python script', ('*.py')),
                                             ('Image Files', ('*.gif', '*.jpeg', '*.jpg')),
                                             ('All Files', ('*'))
                                             ])
        if fname:
            self.entry.delete(0, Tk.END)
            self.entry.insert(Tk.END, fname)
            self.master.winfo_toplevel().focus_set()

class Demo(A.Demo):
    """
     a demo for simple labels
    """
    def __init__(self, cmain):                              #cmain = __name== '__main__'
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_frame(self):
        self.demo_main_frame.master.title("File Selection Dialogs")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_main_frame, text=
        "Enter a file name in the entry box or click on the \"Browse\" buttons to "
        "select a file name using the file selection dialog."
        , width=55, wraplength='12c')
        s_open=File_Selector(self.demo_frame, 'open')
        s_open.pack(pady=5,padx=10)
        s_save=File_Selector(self.demo_frame, 'save')
        s_save.pack(pady=5,padx=10)




##--------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


