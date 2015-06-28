#! /usr/bin/env python

"""
paned1.py

This demonstration script creates a toplevel window containing
a paned window that separates two windows horizontally.

June 16, 2005
"""

import Tkinter as Tk
import template as A

class Demo(A.Demo):
    """a demo class """



    def __init__(self, cmain):                              #cmain = __name== '__main__'
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_frame(self):
        self.demo_main_frame.master.title("Horizontal Paned Window Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_main_frame, text=
        "The sash between the two coloured windows below can be used to divide the area between them.  "
        "Use the left mouse button to resize without redrawing by just moving the sash, "
        "and use the middle mouse button to resize opaquely (always redrawing the windows in each position.)"
        , width=40, wraplength='8.5c')

        pwin = Tk.PanedWindow(self.demo_frame)
        pwin.pack(fill=Tk.BOTH, expand=1, pady=2, padx=10)
        lb_l = Tk.Label(pwin, text="This is the\nleft side", bg='yellow')
        lb_r = Tk.Label(pwin, text="This is the\nright side", bg='cyan')

        pwin.add(lb_l)
        pwin.add(lb_r)



##-----------------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


