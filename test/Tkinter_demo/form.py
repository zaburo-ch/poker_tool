#! /usr/bin/env python

# SpinBox
#

import Tkinter as Tk
import template as A



class Demo(A.Demo):
    """  a demo class """

    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("Form Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        
        A.Label(self.demo_main_frame, text=
        "This window contains a simple form " 
        "where you can type in the various entries and use tabs to move circularly between the entries."
        , width=40,  wraplength='8.5c')

        f=Tk.Frame(self.demo_frame)
        f.pack(fill=Tk.X, expand=1, padx=5, pady=5)

        label_name = Tk.Label(f, width=15, text="Name:",  justify=Tk.LEFT, anchor=Tk.W)
        label_address = Tk.Label(f, width=15, text="Address:",  justify=Tk.LEFT, anchor=Tk.W)
        label_phone = Tk.Label(f, width=15, text="Phone:", justify=Tk.LEFT, anchor=Tk.W)

        label_name.grid(row=0, column=0)
        label_address.grid(row=1, column=0)
        label_phone.grid(row=4, column=0)

        for i in range(5):
            e = Tk.Entry(f, width=40)
            e.grid(row=i, column=1, pady=2)



 
##----------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()

