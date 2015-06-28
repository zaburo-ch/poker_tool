#! /usr/bin/env python

"""
plot.py

This demonstration script creates a canvas widget showing a 2-D
plot with data points that can be dragged with the mouse.

June 14, 2005
"""



import Tkinter as Tk
import template as A


XY_DATA = [(12,55),(21,95),(33,130),(35,100),(62,190),(73,160),(95,240)]

    
class Point:
    """ class of plotting data points """
    id = None
    plot = None
    color0 = 'SkyBlue2'
    color1 = 'red'
    r = 6
    
    def __init__(self, plot, x, y):
        self.plot = plot
        cx = self.plot.cx0 + x * self.plot.cx_range / self.plot.vx_range 
        cy = self.plot.cy0 - y * self.plot.cy_range / self.plot.vy_range  
        self.id = self.plot.create_oval(cx-self.r, cy-self.r, cx+self.r, cy+self.r,
                             width=1, outline='black', fill=self.color0)
        self.plot.tag_bind(self.id, '<1>', self.drag_start)
        self.plot.tag_bind(self.id, '<Button1-Motion>', self.dragging)
        self.plot.tag_bind(self.id, '<Enter>', self.color_change)
        self.plot.tag_bind(self.id, '<Leave>', self.color_original)

    def drag_start(self, event):
        self.x = event.x
        self.y = event.y

    def dragging(self, event):
        x1 = event.x
        y1 = event.y
        self.plot.move(self.id, x1-self.x, y1-self.y)
        self.x = x1
        self.y = y1

    def color_original(self,event):
        self.plot.itemconfigure(self.id, fill=self.color0)

    def color_change(self,event):
        self.plot.itemconfigure(self.id, fill=self.color1)

class Plot (Tk.Canvas):
    """ Simple 2D plot class """
    cx0 = 100
    cy0 = 250
    cx_range = 300
    cy_range = 200
    font = ('Helvetica', '18')
    
    def __init__(self, master, xy_data, title, xrange, yrange, xtics, ytics):
        self.vx_range = xrange[1] - xrange[0]
        self.vy_range = yrange[1] - yrange[0]
        
        Tk.Canvas.__init__(self, master, relief=Tk.RAISED, width=450, height=300)
        self.pack(fill=Tk.X)
        self.create_text(225, 20, text=title, font=self.font, fill='brown')
        self.create_line(self.cx0, self.cy0, self.cx0+self.cx_range, self.cy0, width=2)   # x axis
        self.create_line(self.cx0, self.cy0, self.cx0,  self.cy0-self.cy_range, width=2)   # y axis
        for t in xtics:
            xt = self.cx0 + t * self.cx_range /self.vx_range
            self.create_line(xt, 250, xt, 245, width=2)
            self.create_text(xt, 254, text=str(t), anchor = Tk.N, font= self.font)

        for t in ytics:
            yt = self.cy0 - t * self.cy_range /self.vy_range
            self.create_line(100, yt, 105, yt, width=2)
            self.create_text(96, yt, text='%.1f' % (t), anchor = Tk.E, font= self.font)

        for x,y in xy_data:
            self.add_data(x,y)

    def add_data(self, x, y):
        Point(self, x, y)



class Demo(A.Demo):
    """
    a demo for plot
    """

    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()
    
    def ini_frame(self):
        
        self.demo_main_frame.master.title("Plot Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_frame, text=
                     "This window displays a canvas widget containing a simple 2-dimensional plot.  " 
                     "You can doctor the data by dragging any of the points with mouse button 1."
                    , width=45,  wraplength='11c')
        Plot(self.demo_frame, XY_DATA, "A Simple Plot",
                  (0, 100), (0, 250), range(0,105,10), range(0,255,50))



##---------------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()

