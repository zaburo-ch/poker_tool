#! /usr/bin/env python

"""
entry2.py

This demonstration script is the same as the entry1.tcl script
except that it creates scrollbars for the entries.

June 14, 2005
"""


import Tkinter as Tk
import template as A


class Entry_with_Scrollbar(Tk.Entry):
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        Tk.Entry.__init__(self, self.frame)
        self.xbar  = Tk.Scrollbar (self.frame, orient=Tk.HORIZONTAL, command=self.__scrollHandler)
        self.xbar.pack(side=Tk.BOTTOM, fill=Tk.X)
        self.config(xscrollcommand=self.xbar.set)
        self.pack(fill=Tk.X)


    def __scrollHandler(self, *av):
        op, magnitude = av[0], av[1]
        if op== "scroll":
            units = av[2]
            self.xview_scroll( magnitude, units)
        elif op == "moveto":
            self.xview_moveto (magnitude)

class Demo(A.Demo):
    """
    a demo for entries with scrolled bar
    """
    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

        
    def ini_frame(self):
        self.demo_main_frame.master.title("Entry Demonstration (with scrollbars)")
        self.demo_main_frame.master.geometry("+50+50")
        
        A.Label(self.demo_main_frame, text=
        "Three different entries are displayed below, with a scrollbar for each entry.  " 
        "You can add characters by pointing, clicking and typing.  " 
        "The normal Motif editing characters are supported, along with many Emacs bindings.  " 
        "For example, Backspace and Control-h delete the character to the left of the insertion cursor " 
        "and Delete and Control-d delete the chararacter to the right of the insertion cursor.  " 
        "For entries that are too large to fit in the window all at once, " 
        "you can scan through the entries with the scrollbars, or by dragging with mouse button2 pressed."
        ,width=50,  wraplength='11c')

        es=[]
        for i in range(3):
            e = Entry_with_Scrollbar(self.demo_frame)
            e.frame.pack(fill=Tk.X, expand=1, padx=7, pady=5)
            es.append(e)

        es[0].insert(0, "Initial value")
        es[1].insert(Tk.END, "This entry contains a long value, much too long ")
        es[1].insert(Tk.END, "to fit in the window at one time, so long in fact ")
        es[1].insert(Tk.END, "that you'll have to scan or scroll to see the end.")
        

def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


