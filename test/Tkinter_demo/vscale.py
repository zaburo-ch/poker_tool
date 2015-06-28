#! /usr/bin/env python

"""
vscale.py

This demonstration script shows an example with a vertical scale.

June 16, 2005
"""

import Tkinter as Tk
import template as A

class Demo(A.Demo):
    """ a demo class """


    def __init__(self, cmain):                              #cmain = __name== '__main__'
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_frame(self):
        self.demo_main_frame.master.title("Vertical Scale Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_frame, text=
        "An arrow and a vertical scale are displayed below.  "
        "If you click or drag mouse button 1 in the scale, you can change the size of the arrow."
        , width=40, wraplength='8.5c')

        self.cvs = Tk.Canvas(self.demo_frame, width=50, height=50, bd=0, highlightthickness=0)
        self.poly = self.cvs.create_polygon(0,0,1,1,2,2, fill='SeaGreen3', tags='poly')
        self.line = self.cvs.create_line(0,0,1,1,2,2,0,0, fill='black', tags='line')
        self.scale =Tk.Scale(self.demo_frame, orient=Tk.VERTICAL, length=284, from_=0, to=250,
                             command=self.scale_arrow, tickinterval=50)
        self.scale.pack(side=Tk.LEFT, anchor=Tk.NE, fill=Tk.Y, expand=1, pady=15)
        self.cvs.pack(side=Tk.RIGHT, anchor=Tk.NW, fill=Tk.Y, expand=1,  padx=15)
        self.scale.set(75)

    def scale_arrow(self, event):
        height= self.scale.get() + 31
        y2 = A.i_range(height-30, 31, None)
        self.cvs.coords(self.poly, 15, 30, 35, 30, 35, y2, 45, y2, 25, height, 5, y2, 15, y2, 15, 30)
        self.cvs.coords(self.line, 15, 30, 35, 30, 35, y2, 45, y2, 25, height, 5, y2, 15, y2, 15, 30)




##---------------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


