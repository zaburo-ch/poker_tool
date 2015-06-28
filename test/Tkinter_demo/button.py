#! /usr/bin/env python

"""
button.py 

This demonstration script creates a toplevel window containing
several button widgets.

June 14, 2005
"""


import Tkinter as Tk
import template as A


class Button(Tk.Button):
    """ Buttons to change bg of frames """
    def __init__(self, master, obj, color_name, color_id):
        Tk.Button.__init__(self, master, text=color_name, width=15, command=self.command)
        self.obj = obj
        self.color_id = color_id

    def command(self):
        self.obj.demo_frame.config(bg=self.color_id)
        self.obj.demo_buttons.config(bg=self.color_id)
        

class Demo(A.Demo):
    """a demo class """
    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_frame(self):
        self.demo_main_frame.master.title("Button Demonstration")
        self.demo_main_frame.master.geometry('+50+50')
        A.Label(self.demo_main_frame, text=
        "If you click on any of the four buttons below, " 
        "the background of the button area will change to the color indicated in the button."
        , width=35, wraplength='8c')
        for name, code in [('Deeppink', '#FF1493'), ('Cornflowerblue', '#6495ED'),
                             ('Springgreen', '#00FF7F'), ('Gold', '#FFD700')]:
            b = Button(self.demo_frame, self, name, code) 
            b.pack(padx=10, pady=5)


##------------------------------------------------ 
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()
