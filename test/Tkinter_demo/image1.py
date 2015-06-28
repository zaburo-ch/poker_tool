#! /usr/bin/env python

"""
image1.py

This demonstration script displays two image widgets.

June 15, 2005
"""


import Tkinter as Tk
import template as A



class Demo(A.Demo):
    """ demo class """
    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("Image Demonstration #1")
        self.demo_main_frame.master.geometry('+50+50')
        
        A.Label(self.demo_main_frame, text=
        "This demonstration displays two images, each in a separate label widget."
        , width=40, wraplength='9c')

        self.images = A.newlist(2)

        for i, img in enumerate(('earth.gif', 'earthris.gif')):
            self.images[i] = Tk.PhotoImage(file=img)
            label = Tk.Label(self.demo_frame, image=self.images[i], bd=1, relief=Tk.SUNKEN)
            label.pack(pady=5)



def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()
