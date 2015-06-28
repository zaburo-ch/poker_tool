#! /usr/bin/env python

"""
bind.py

This demonstration script creates a text widget with bindings set
up for hypertext-like effects.

June 20, 2005
"""

import Tkinter as Tk
import template as A
from ScrolledText import ScrolledText

import items
import plot
import ctext
import arrow
import ruler
import cscroll


class Link:
    def __init__(self, master, text, tag, command):

        self.master = master
        self.tag = tag
        self.master.insert(Tk.END, text, tag)
        
        self.master.tag_bind(tag, "<1>", command)
        self.master.tag_bind(tag, "<Enter>", self.on_enter)
        self.master.tag_bind(tag, "<Leave>", self.on_leave)

    def on_leave(self, *rest):
        self.master.tag_config(self.tag, background='white', relief=Tk.FLAT)
        
    def on_enter(self, event):
        self.master.tag_config(self.tag, relief=Tk.RAISED, background='#43ce80', borderwidth=1)



class Demo(A.Demo):
    """  a simple text """


    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("Text Demonstration - Basic Facilities")
        self.demo_main_frame.master.geometry('+50+50')
        scrolled_text= ScrolledText(self.demo_frame, wrap=Tk.WORD, font=('Helvetica', '12'), width=60)
        scrolled_text.pack(fill=Tk.BOTH, expand=1)
        scrolled_text.insert(Tk.END,
        """The same tag mechanism that controls display styles in text widgets can also be used to associate Tcl commands with regions of text, so that mouse or keyboard actions on the text cause particular Tcl commands to be invoked.  For example, in the text below the descriptions of the canvas demonstrations have been tagged.  When you move the mouse over a demo description the description lights up, and when you press button 1 over a description then that particular demonstration is invoked.\n\n
""")

        for i, (txt, cmd) in enumerate (
                           [("Samples of all the different types of items that can be created in canvas widgets.",
                            items.demo),
                            ("A simple two-dimensional plot that allows you to adjust the positions of the data points.",
                            plot.demo),
                            ("Anchoring and justification modes for text items.", ctext.demo),
                            ("An editor for arrow-head shapes for line items.", arrow.demo),
                            ("A ruler with facilities for editing tab stops.", ruler.demo),
                            ("A grid that demonstrates how canvases can be scrolled.", cscroll.demo)]):
            Link(scrolled_text, str(i+1) + ". " + txt, str(i+1), cmd)
            scrolled_text.insert(Tk.END, "\n\n")
                            

##---------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()

