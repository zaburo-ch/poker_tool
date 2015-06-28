#! /usr/bin/env python

"""
sayings.py

This demonstration script creates a listbox that can be scrolled
both horizontally and vertically.  It displays a collection of
well-known sayings.

June 14, 2005
"""


import Tkinter as Tk
import template as A


SAYINGS = [
              "Waste not, want not",
              "Early to bed and early to rise makes a man healthy, wealthy, and wise",
              "Ask not what your country can do for you, ask what you can do for your country",
              "I shall return", "NOT", "A picture is worth a thousand words",
              "User interfaces are hard to build",
              "Thou shalt not steal",
              "A penny for your thoughts",
              "Fool me once, shame on you;  fool me twice, shame on me",
              "Every cloud has a silver lining",
              "Where there's smoke there's fire",
              "It takes one to know one",
              "Curiosity killed the cat",
              "Take this job and shove it",
              "Up a creek without a paddle",
              "I'm mad as hell and I'm not going to take it any more",
              "An apple a day keeps the doctor away",
              "Don't look a gift horse in the mouth"
          ]



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
        self.demo_main_frame.master.title("Listbox Demonstration (well-known sayings)")
        self.demo_main_frame.master.geometry("+50+50")
        
        A.Label(self.demo_main_frame, text=
        "The listbox below contains a collection of well-known sayings.  " 
        "You can scan the list using either of the scrollbars or by dragging " 
        "in the listbox window with button 2 pressed."
        , width=40, wraplength='8.5c')

        fmiddle = Tk.Frame(self.demo_frame)
        fmiddle.pack(pady=10)
        yscroll=Tk.Scrollbar (fmiddle, orient=Tk.VERTICAL)
        yscroll.pack(side=Tk.RIGHT, fill=Tk.Y)

        xscroll=Tk.Scrollbar (fmiddle, orient=Tk.HORIZONTAL)
        xscroll.pack(side=Tk.BOTTOM, fill=Tk.X)
        
        lbox= Tk.Listbox(fmiddle, height=15,
                              xscrollcommand=xscroll.set,
                              yscrollcommand=yscroll.set)
        xscroll.config(command=lbox.xview)
        yscroll.config(command=lbox.yview)

        lbox.insert(Tk.END, *SAYINGS)

        lbox.pack()

        

def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


