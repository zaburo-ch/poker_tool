#! /usr/bin/env python

"""
labelframe.py

This demonstration script creates a toplevel window containing
several labelframe widgets.

June 16, 2005
"""


import Tkinter as Tk
import template as A



class Demo(A.Demo):
    """ a demo class """
    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("Labelframe Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        
        A.Label(self.demo_main_frame, text=
        "Labelframes are used to group related widgets together.  " 
        "The label may be either plain text or another widget."
        , width=40, wraplength='8.5c')

        f = Tk.Frame(self.demo_frame)
        f.pack()
        f1 = Tk.LabelFrame(f, text='Value', padx=2, pady=2)
        self.dummy = Tk.IntVar()
        for i in range(4):
            rb = Tk.Radiobutton(f1, text = 'This is value %d' % (i+1), variable = self.dummy, value = i+1)
            rb.pack(fill=Tk.X, pady=2)

        f1.pack(side=Tk.LEFT, pady='2m', padx=20)

        self.ifdummy = Tk.IntVar()
        f2 = Tk.LabelFrame(f, pady=2, padx=2)
        cb =Tk.Checkbutton(f2, text='Use this option', variable = self.ifdummy,
                                 command=self.toggle, padx=0)
        f2.configure(labelwidget=cb)
        f2.pack(side=Tk.RIGHT, pady='2m', padx=20)
        
        self.active = False
        self.cbs = []
        for i in range(3):
            obj = Tk.Checkbutton(f2, text='Option %d' % (i+1), state=Tk.DISABLED)
            obj.pack(fill=Tk.X, pady=2)
            self.cbs.append(obj)


    def toggle(self):
        state = self.active and Tk.DISABLED or Tk.NORMAL
        self.active = not self.active
        for i in range(3):
            self.cbs[i].configure(state=state)


##--------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()
