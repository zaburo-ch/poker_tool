#! /usr/bin/env python

"""
filebox.py

This demonstration script prompts the user to select a file.

June 17, 2005
"""

import Tkinter as Tk
import tkColorChooser as C
import template as A

def get_color(tup):
    return tup[1]


class Color_Selector(Tk.Button):
    def __init__(self, master, area, toplevel):
        self.toplevel = toplevel
        txt = 'Set %s color...' % (area=='fg' and 'foreground' or 'background')
        Tk.Button.__init__(self, master, text=txt, width=20, command=(area=='fg' and self.set_fg or self.set_bg))

    def set_bg(self):
        self.set_bg_rec(self.toplevel, get_color(C.askcolor()))
        self.toplevel.focus_set()

    def set_bg_rec(self, widget, color):
        for w in widget.winfo_children():
            w.configure(bg=color)
            self.set_bg_rec(w, color)
            
        
    def set_fg(self):
        self.set_fg_rec(self.toplevel, get_color(C.askcolor()))
        self.toplevel.focus_set()
        
    def set_fg_rec(self, widget, color):
        for w in widget.winfo_children():
            if w.winfo_class() != 'Frame':
                w.configure(fg=color)
            self.set_fg_rec(w, color)

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
        self.demo_main_frame.master.title("Color Selection Dialog")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_main_frame, text=
        "Press the buttons below to choose the foreground "
        "and background colors for the widgets in this window."
        , width=45, wraplength='10c')
        bg=Color_Selector(self.demo_frame, 'bg', self.demo_main_frame.master)
        bg.pack(pady=5,padx=10)
        fg=Color_Selector(self.demo_frame, 'fg', self.demo_main_frame.master)
        fg.pack(pady=5,padx=10)




##--------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


