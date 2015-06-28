#! /usr/bin/env python

"""
ruler.py 

This demonstration script creates a canvas widget that displays a ruler
with tab stops that can be set, moved, and deleted.

June 16, 2005
"""

import Tkinter as Tk
import template as A


def d2c(i, j):
    return '%d.%dc' % (i, j)

def j2c(j):
    if j == 0:
        return '0.6c'
    elif(j == 50):
        return '0.7c'
    else:
        return '0.8c'


class Tab:
    """ Tabs on the ruler """

    cvs = None     # Canvas
    master = None  # Demo
    
    def __init__(self):
        self.activate=True                                    # turn red at initial
        self.id = Tab.cvs.create_polygon('13c', '0.5c', '12.8c', '0.7c', '13.2c', '0.7c')
        self.masked()                                         # mask it by gray25
        self.x = Tab.cvs.winfo_fpixels('13c')
        self.y = Tab.cvs.winfo_fpixels('0.5c')
        
        ## key bindings
        Tab.cvs.tag_bind(self.id, '<1>', self.on_press)
        Tab.cvs.tag_bind(self.id, '<ButtonRelease-1>', self.on_release)
        Tab.cvs.tag_bind(self.id, '<Motion>', self.on_move)

    def on_press(self, event):
        self.activate=True
        self.active()

    def on_release(self, event):
        self.activate=False
        if self.y == Tab.master.top + 2:
            self.normal()
        else:
            Tab.cvs.delete(self.id)
            
    def masked(self):
        """ mask the tab by gray25"""
        Tab.cvs.itemconfigure(self.id, fill='red', stipple='@gray25.bmp')

    def normal(self):
        """ normal stage, the color is black """
        Tab.cvs.itemconfigure(self.id, fill='black', stipple='')
        
    def active(self):
        """ activated stage, red """
        Tab.cvs.itemconfigure(self.id, fill='red', stipple='')

    def on_move(self, event):
        """the motion of tab rectangular"""
        
        cx = A.i_range(Tab.cvs.canvasx(event.x, Tab.master.size), Tab.master.left, Tab.master.right) 
        cy = self.cvs.canvasy(event.y)
        if self.activate:
            if(self.master.top <= cy <= self.master.bottom):                   
                cy = self.master.top + 2
                self.active()
            else:
                cy -= self.master.size + 2
                self.masked()

            Tab.cvs.move(self.id, cx - self.x, cy - self.y)
            self.x = cx
            self.y = cy



class TabMaker:
    """ Tab making Box: A black tab in the box at the right side of the ruler, which creates new tabs. """
        
    def __init__(self, cvs):
        self.newtab=None
        cvs.create_rectangle('13.2c', '1c', '13.8c', '0.5c', outline='black', fill = cvs.cget('bg'), tags='maker')
        cvs.create_polygon('13.5c', '0.65c', '13.3c', '0.85c', '13.7c', '0.85c', fill='black', tags='maker')
        ## bindings
        cvs.tag_bind('maker', '<1>', self.on_press)
        cvs.tag_bind('maker', '<ButtonRelease-1>', self.on_release)
        cvs.tag_bind('maker', '<Motion>', self.on_move)

    def on_press(self, event):
        self.newtab = Tab()

    def on_release(self, event):
        self.newtab.on_release(event)

    def on_move(self, event):
        if self.newtab:
            self.newtab.on_move(event)



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
        self.demo_main_frame.master.title("Ruler Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_frame, text=
        "This canvas widget shows a mock-up of a ruler.  "
        "You can create tab stops by dragging them out of the well to the right of the ruler.  "
        "You can also drag existing tab stops.  "
        "If you drag a tab stop far enough up or down so that it turns dim, "
        "it will be deleted when you release the mouse button."
        , width=60, wraplength='12c')

        self.cvs = Tk.Canvas(self.demo_frame, width='14.8c', height='2.5c')
        self.cvs.pack(fill=Tk.X)

        # parameters
        self.grid_size = '0.25c'
        self.left = self.cvs.winfo_fpixels('1c')
        self.right = self.cvs.winfo_fpixels('13c')
        self.top = self.cvs.winfo_fpixels('1c')
        self.bottom = self.cvs.winfo_fpixels('1.5c')
        self.size = self.cvs.winfo_fpixels('0.25c')

        # setting Tab class parameters
        Tab.master = self
        Tab.cvs = self.cvs

        # making a ruler on the canvas
        self.cvs.create_line('1c', '0.5c', '1c', '1c', '13c', '1c', '13c', '0.5c', width=1)

        for i0 in range(12):
            i=i0+1
            self.cvs.create_text(d2c(i,15), '0.75c', text=str(i0), anchor = Tk.SW)
            for j in range(0,80,25):
                self.cvs.create_line(d2c(i,j), '1c', d2c(i,j), j2c(j), width=1) 

        TabMaker(self.cvs)


##-----------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


