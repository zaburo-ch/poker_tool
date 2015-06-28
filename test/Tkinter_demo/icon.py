#! /usr/bin/env python

"""
icon.py

This demonstration script creates a toplevel window containing
buttons that display bitmaps instead of text.

June 15, 2005
"""


import Tkinter as Tk
import template as A




class Demo(A.Demo):
    """
    a demo for buttons with images
    """
    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("Radiobutton Demonstration")
        self.demo_main_frame.master.geometry('+50+50')
        
        A.Label(self.demo_main_frame, text=
        "This window shows three ways of using bitmaps or images in radiobuttons and checkbuttons.  " 
        "On the left are two radiobuttons, each of which displays a bitmap and an indicator.  " 
        "In the middle is a checkbutton that displays a different image depending on whether it is selected or not.  " 
        "On the right is a checkbutton that displays a single bitmap " 
        "but changes its background color to indicate whether or not it is selected."
        , width=50, wraplength='9.5c')

        f0 = Tk.Frame(self.demo_frame)
        f0.pack(pady=35)

        self.flagup   = Tk.Image('bitmap', file='flagup.bmp', maskfile='flagup.bmp') 
        self.flagdown = Tk.Image('bitmap', file='flagdown.bmp', maskfile='flagdown.bmp') 

        check_1 = Tk.Checkbutton(f0, image=self.flagdown, selectimage=self.flagup, indicatoron=0)
        check_1.configure(selectcolor=check_1.cget('bg'))
        check_2 = Tk.Checkbutton(f0, bitmap='@letters.bmp', indicatoron=0, selectcolor='SeaGreen1')

        fl = Tk.Frame(f0)
        fl.pack(side=Tk.LEFT, padx=20)
        check_1.pack(side=Tk.LEFT, padx=20)
        check_2.pack(side=Tk.LEFT, padx=20)

        self.letters = Tk.StringVar()
        rd1 = Tk.Radiobutton(fl, bitmap='@letters.bmp', variable=self.letters, value='full')
        rd2 = Tk.Radiobutton(fl, bitmap='@noletter.bmp', variable=self.letters, value='empty')
        rd1.pack()
        rd2.pack()
                                      



def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()
