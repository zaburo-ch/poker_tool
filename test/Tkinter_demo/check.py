#! /usr/bin/env python

"""
check.py --

This demonstration script creates a toplevel window containing
several checkbuttons.

June 15, 2005
"""


import Tkinter as Tk
import template as A

class Demo(A.Demo):
    """
    a demo for check buttons
    """
    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("Checkbutton Demonstration")
        self.demo_main_frame.master.geometry('+50+50')
        
        A.Label(self.demo_main_frame, text=
        "Three checkbuttons are displayed below.  " 
        "If you click on a button, it will toggle the button's selection state " 
        "and set a Tcl variable to a value indicating the state of the checkbutton.  " 
        "Click the \"See Variables\" button to see the current values of the variables."
        , width=40, wraplength='9c')

        self.wipers = Tk.IntVar()
        self.brakes = Tk.IntVar()
        self.sober = Tk.IntVar()

        for txt, var in [('Wipers OK', self.wipers), ('Brakes OK', self.brakes), ('Driver Sober', self.sober)]:
            c = Tk.Checkbutton(self.demo_frame, text=txt, variable=var, relief=Tk.FLAT, justify = Tk.LEFT)
                               
            c.pack(pady=5, anchor=Tk.W)

        self.bv = Tk.Button(self.demo_buttons, text='See Variables', width=20,
                            command=A.ShowVars(self.demo_main_frame.master, 0,
                            ('wipers:', str(self.wipers)), ('brakes:', str(self.brakes)), ('sober:', str(self.sober))))
        self.bv.pack(side=Tk.RIGHT, padx=10, pady=5)



        
##-----------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()
