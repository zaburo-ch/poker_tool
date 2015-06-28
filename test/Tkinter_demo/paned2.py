#! /usr/bin/env python

"""
paned2.py

This demonstration script creates a toplevel window containing
a paned window that separates two windows vertically.

June 16, 2005
"""

import Tkinter as Tk
import template as A
from states import ScrolledListbox
from ScrolledText import ScrolledText



class Demo(A.Demo):
    """a demo class """

    items = [
               'List of Tk Widgets',
               'button',
               'canvas',
               'checkbutton',
               'entry',
               'frame',
               'label',
               'labelframe',
               'listbox',
               'menu',
               'menubutton',
               'message',
               'panedwindow',
               'radiobutton',
               'scale',
               'scrollbar',
               'spinbox',
               'text',
               'toplevel'
             ]
    
    def __init__(self, cmain):                              #cmain = __name== '__main__'
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_frame(self):
        self.demo_main_frame.master.title("Vertical Paned Window Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_main_frame, text=
        "The sash between the two scrolled windows below can be used to divide the area between them.  "
        "Use the left mouse button to resize without redrawing by just moving the sash, "
        "and use the middle mouse button to resize opaquely (always redrawing the windows in each position.)"
        , width=40, wraplength='8.5c')

        pwin = Tk.PanedWindow(self.demo_frame, orient=Tk.VERTICAL)
        pwin.pack(fill=Tk.BOTH, expand=1, pady=2, padx=10)
        upper = ScrolledListbox(pwin)
        for item in self.items:
            upper.insert(Tk.END, item)
            
        upper.itemconfigure(0, bg = upper.cget('fg'), fg=upper.cget('bg'))

        lower = ScrolledText(pwin, width=30)
        lower.insert(Tk.END, "This is just a normal text widget")

        pwin.add(upper.frame)
        pwin.add(lower.frame)



##-----------------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()

