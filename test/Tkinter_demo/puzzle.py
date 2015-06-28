#! /usr/bin/env python

"""
puzzle.py

This demonstration script creates a 15-puzzle game using a collection
of buttons.

June 15, 2005
"""


import Tkinter as Tk
import template as A



def next_to(i, j):
    k = abs(i-j)
    return (k == 1 or k == 4)


class PButton(Tk.Button):
    def __init__(self, master, i, num):
        self.master = master
        self.i = i
        self.num = num
        Tk.Button.__init__(self, master, relief=Tk.RAISED, text=str(num), width=4, height=2,
                           highlightthickness=0, command=self.command)
        self.grid(row=i/4, column=i%4)

    def command(self):
        if (next_to(self.i, self.master.empty)):
            PButton(self.master, self.master.empty, self.num)
            self.master.empty=self.i
            self.destroy()


class Puzzle(Tk.Frame):
    def __init__(self, master):
        order = [3, 1, 6, 2, 5, 7, 15, 13, 4, 11, 8, 9, 14, 10, 12]
        self.empty=15
        Tk.Frame.__init__(self, master, width= 120, height=120, borderwidth=2, relief=Tk.SUNKEN)
        self.pack(padx=10, pady=40)
        for i in range(15):
            PButton(self, i, order[i])


class Demo(A.Demo):
    """
    the 15-puzzle using Tk.Button's
    """
    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("15-Puzzle Demonstration")
        self.demo_main_frame.master.geometry('+50+50')
        
        A.Label(self.demo_main_frame, text=
        "A 15-puzzle appears below as a collection of buttons.  " 
        "Click on any of the pieces next to the space, and that piece will slide over the space.  " 
        "Continue this until the pieces are arranged in numerical order from upper-left to lower-right."
        , width=45, wraplength='9c')

        Puzzle(self.demo_frame)


def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()
