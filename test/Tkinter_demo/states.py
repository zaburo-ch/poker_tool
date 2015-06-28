#! /usr/bin/env python

"""
states.py

This demonstration script creates a listbox widget that displays
the names of the 50 states in the United States of America

June 14, 2005
"""


import Tkinter as Tk
import template as A

STATES = ["Alabama",  "Alaska",  "Arizona",  "Arkansas",  "California", 
          "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", 
          "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", 
          "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", 
          "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", 
          "New York", "North Carolina", "North Dakota", 
          "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", 
          "South Carolina", "South Dakota", 
          "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
          "West Virginia", "Wisconsin", "Wyoming"]

          
class ScrolledListbox(Tk.Listbox):
    """
Listbox with vertical scroll bar
self.frame : frame of this listbox
to pack or grid this widget you should do like 'self.frame.pack()'
"""

    
    def __init__(self, master, **key):
        self.frame = Tk.Frame(master)
        self.yscroll = Tk.Scrollbar (self.frame, orient=Tk.VERTICAL)
        self.yscroll.pack(side=Tk.RIGHT, fill=Tk.BOTH)
        key['yscrollcommand']=self.yscroll.set
        Tk.Listbox.__init__(self, self.frame, **key)
        self.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.yscroll.config(command=self.yview)

        # Copy geometry methods of self.frame -- hack!
        for m in (Tk.Pack.__dict__.keys() + Tk.Grid.__dict__.keys() + Tk.Place.__dict__.keys()):
            m[0] == '_' or m == 'config' or m == 'configure' or \
                setattr(self, m, getattr(self.frame, m))



class Demo(A.Demo):

    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("Listbox Demonstration (50 states)")
        self.demo_main_frame.master.geometry("+50+50")
        
        A.Label(self.demo_main_frame, text=
        "A listbox containing the 50 states is displayed below, along with a scrollbar. " 
        "You can scan the list either using the scrollbar or by scanning.  " 
        "To scan, press button 2 in the widget and drag up or down."
        , width=40, wraplength='8.5c')

        lbox=ScrolledListbox(self.demo_frame)
        
        lbox.insert(Tk.END, *STATES)

        lbox.pack()


def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()

