#! /usr/bin/env python

"""
label.py

This demonstration script creates a toplevel window containing
several label widgets.

June 14, 2005
"""

import Tkinter as Tk
import template as A

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
        self.demo_main_frame.master.title("Label Demonstration")
        A.Label(self.demo_main_frame, text=
        "Five labels are displayed below: " 
        "three textual ones on the left, and a bitmap label and a text label on the right. " 
        "Labels are pretty boring because you can't do anything with them."
        , width=40, wraplength='8.5c')
        self.fleft = Tk.Frame(self.demo_frame)
        self.fleft.pack(side=Tk.LEFT)
        self.fright = Tk.Frame(self.demo_frame)
        self.fright.pack(side=Tk.RIGHT, fill=Tk.X, expand=1)
        label = Tk.Label(self.fleft, text="first label", font=("Helvetica", "10"))
        label.pack(padx=10, pady=10)
        label = Tk.Label(self.fleft, text="second label, raised", relief=Tk.RAISED, font=("Helvetica", "10"))
        label.pack(padx=10, pady=10)
        label = Tk.Label(self.fleft, text="third label, sunken", relief=Tk.SUNKEN, font=("Helvetica", "10"))
        label.pack(padx=10, pady=10)
        self.py = Tk.PhotoImage(file="py.gif")
        label = Tk.Label(self.fright, image=self.py)  # image should be `self.' parameter
        label.pack(padx=10, pady=10)


def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


