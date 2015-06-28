#! /usr/bin/env python

"""
spin.py

This demonstration script creates several spinbox widgets.

June 14, 2005
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
        self.demo_main_frame.master.title("Spinbox Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        
        A.Label(self.demo_frame, text=
        "Three different spin-boxes are displayed below.  " 
	"You can add characters by pointing, clicking and typing.  " 
	"The normal Motif editing characters are supported, along with many Emacs bindings.  " 
	"For example, Backspace " 
	"and Control-h delete the character to the left of the insertion " 
	"cursor and Delete and Control-d delete the chararacter to the right " 
	"of the insertion cursor.  For values that are too large to fit in the " 
	"window all at once, you can scan through the value by dragging with " 
	"mouse button2 pressed.  Note that the first spin-box will only permit " 
	"you to type in integers, and the third selects from a list of " 
	"Australian cities."
        , width=50,  wraplength='10.5c')

        f = Tk.Frame(self.demo_frame)
        f.pack(pady=10)
        sb1 = Tk.Spinbox(f, width=12, from_=1, to=10)
        sb2 = Tk.Spinbox(f,  width=12, from_=0.0, to=3.0, increment=0.5, format="%05.2f")
        sb3 = Tk.Spinbox(f,  width=12,
                              values=("Canberra", "Sydney", "Melbourne",  "Perth", "Adelaide",
                                      "Brisbane", "Hobart",  "Darwin", "Alice Springs"))
                                                        
        sb1.pack(pady=4)
        sb2.pack(pady=4)
        sb3.pack(pady=4)


 
##-------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


