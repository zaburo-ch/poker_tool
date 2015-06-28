#! /usr/bin/env python

"""
cscroll.py

This demonstration script creates a simple canvas that can be
scrolled in two dimensions.

June 17, 2005
"""

import Tkinter as Tk
import template as A



def i2c (i):
    return (str(i) + 'c')

class Box:
    def __init__(self, master, cvs, i, j):
        self.master = master
        self.cvs = cvs
        x = i*3 - 10
        y = j*3 - 10
        self.text = '%d,%d' % (i, j)
        self.id_box = self.cvs.create_rectangle(i2c(x), i2c(y), i2c(x+2), i2c(y+2), outline='black',
                                                        fill=self.master.bg, tags='box')
        self.id_text = self.cvs.create_text(i2c(x+1), i2c(y+1), text= self.text, anchor=Tk.CENTER, tags='text')
        self.cvs.tag_bind(self.id_box, '<Enter>', self.on_enter)
        self.cvs.tag_bind(self.id_box, '<Leave>', self.on_leave)
        self.cvs.tag_bind(self.id_text, '<Enter>', self.on_enter)
        self.cvs.tag_bind(self.id_box, '<1>', self.on_click)
        self.cvs.tag_bind(self.id_text, '<1>', self.on_click)


    def on_enter(self, event):
        self.cvs.itemconfigure(self.id_box, fill='SeaGreen1')

    def on_leave(self, event):
        self.cvs.itemconfigure(self.id_box, fill=self.master.bg)

    def on_click(self, event):
        self.master.echo.set(self.text)


        
class Demo(A.Demo):
    """  a demo class """

    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_frame(self):
        self.demo_main_frame.master.title("Form Demonstration")
        self.demo_main_frame.master.minsize(width=400, height=170) 
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_frame, text=
        "This window displays a canvas widget that can be scrolled "
        "either using the scrollbars or by dragging with button 2 in the canvas.  "
        "If you click button 1 on one of the rectangles, its indices will be printed on the lavel."
        , width=40,  wraplength='9c')

        fa = Tk.Frame(self.demo_frame)
        fa.pack(fill=Tk.BOTH, expand=1, padx=1, pady=1)
        self.cvs = Tk.Canvas(fa, scrollregion=("-11c", "-11c",  "50c",  "20c"), 
                                   relief=Tk.SUNKEN, borderwidth=2)  
        self.cvs.grid(row=0, column=0, sticky= Tk.N+Tk.E+Tk.W+Tk.S)
        
        xscroll = Tk.Scrollbar(fa, orient=Tk.HORIZONTAL, command=self.cvs.xview)
        xscroll.grid(row=1, column=0, sticky=Tk.E+Tk.W)

        yscroll = Tk.Scrollbar(fa, orient=Tk.VERTICAL, command=self.cvs.yview)
        yscroll.grid(row=0, column=1, sticky=Tk.N+Tk.S)
        
        self.cvs.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        fa.grid_rowconfigure(0, weight=1, minsize=0)     
        fa.grid_columnconfigure(0, weight=1, minsize=0)  

        self.bg = self.cvs.cget('bg')
        self.echo = Tk.StringVar()

        for i in range(25):
            for j in range(10):
                Box(self, self.cvs, i, j)

        self.cvs.bind('<Button2-Motion>', self.on_motion)
        self.cvs.bind('<2>', self.on_press2)
        

        label = Tk.Label(self.demo_frame, textvariable=self.echo, width=12, relief=Tk.SUNKEN, borderwidth=2)
        label.pack(padx=10, pady=20)

        
        
    def on_press2(self, event):
        self.cvs.scan_mark(event.x, event.y)

    def on_motion(self, event):
        self.cvs.scan_dragto(event.x, event.y)




##------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()

