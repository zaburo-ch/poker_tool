#! /usr/bin/env python

"""
bitmap.py

This demonstration script creates a toplevel window that displays
all of Tk's built-in bitmaps.

June 17, 2005
"""

import Tkinter as Tk
import template as A

class BFrame(Tk.Frame):
    def __init__(self, master, bitmap):
        Tk.Frame.__init__(self, master)
        self.lbit = Tk.Label(self, bitmap = bitmap)
        self.lbit.pack()

        self.ltxt = Tk.Label(self, text = bitmap)
        self.ltxt.pack()


class Demo(A.Demo):

    def __init__(self, cmain):                              #cmain = __name== '__main__'
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_frame(self):
        self.demo_main_frame.master.title("Bitmap Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_main_frame, text=
        "This window displays all of Tk's built-in bitmaps, along with the names you can use for them in Tkinter scripts."
        , width=40, wraplength='9c')

        self.f = Tk.Frame(self.demo_frame)
        self.frames = A.newlist(10)
        for i, bitmap in enumerate(('error', 'gray12', 'gray25', 'gray50', 'gray75', 'hourglass',
                                    'info', 'question', 'questhead', 'warning')):
            self.frames[i] = BFrame(self.f, bitmap)
            self.frames[i].grid(row=i/5, column=i%5, padx=10, pady=10)
        self.f.pack()

            

def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


