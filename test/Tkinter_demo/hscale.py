#! /usr/bin/env python

"""
hscale.py

This demonstration script shows an example with a horizontal scale.

June 16, 2005
"""

import Tkinter as Tk
import template as A

class Demo(A.Demo):
    """ a demo for simple labels """


    def __init__(self, cmain):                              #cmain = __name== '__main__'
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_frame(self):
        self.demo_main_frame.master.title("Horizontal Scale Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_main_frame, text=
        "An arrow and a horizontal scale are displayed below.  "
        "If you click or drag mouse button 1 in the scale, you can change the length of the arrow."
        , width=35, wraplength='8c')

        self.cvs = Tk.Canvas(self.demo_frame, width=50, height=50, bd=0, highlightthickness=0)
        self.poly = self.cvs.create_polygon(0,0,1,1,2,2, fill='DeepSkyBlue3', tags='poly')
        self.line = self.cvs.create_line(0,0,1,1,2,2,0,0, fill='black', tags='line')
        self.scale =Tk.Scale(self.demo_frame, orient=Tk.HORIZONTAL, length=284, from_=0, to=250,
                             command=self.scale_arrow, tickinterval=50)
        self.cvs.pack(anchor=Tk.NW, fill=Tk.X, expand=1, padx=15)
        self.scale.pack(side=Tk.BOTTOM, expand=1, anchor=Tk.SW, padx=15)
        self.scale.set(75)

    def scale_arrow(self, event):
        width= self.scale.get() + 21
        x2 = A.i_range(width -30, 21, None)
        self.cvs.coords(self.poly, 20, 15, 20, 35, x2, 35, x2, 45, width, 25, x2, 5, x2, 15, 20, 15)
        self.cvs.coords(self.line, 20, 15, 20, 35, x2, 35, x2, 45, width, 25, x2, 5, x2, 15, 20, 15)

 
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


