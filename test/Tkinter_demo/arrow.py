#! /usr/bin/env python

"""
arrow.py

This demonstration script creates a canvas widget that displays a
large line with an arrowhead whose shape can be edited interactively.

June 14, 2005

"""


import Tkinter as Tk
import template as A




class Box:
    """
    This is a class of small boxes to change arrow shape.
    """
    def __init__(self, cvs, x, y, command, dragging):
        self.r = 5
        self.cvs = cvs
        self.command = command
        self.dragging = dragging
        self.id = self.cvs.create_rectangle(x-self.r, y-self.r, x+self.r, y+self.r, tags='box')
        self.make_binds()

    def make_binds(self):
        self.cvs.tag_bind(self.id, '<Enter>', self.red)
        self.cvs.tag_bind(self.id, '<Leave>', self.trans)
        self.cvs.tag_bind(self.id, '<1>', self.where)
        self.cvs.tag_bind(self.id, '<Button1-Motion>', self.dragging)
        self.cvs.tag_bind(self.id, '<ButtonRelease-1>', self.command)

    def red(self, event):
        self.cvs.itemconfigure(self.id, fill='red')

    def trans(self, event):
        self.cvs.itemconfigure(self.id, fill='')
        
    def where(self, event):
        self.x0 = event.x
        self.y0 = event.y

    def renew(self, x, y):
        self.cvs.delete(self.id)
        self.id = self.cvs.create_rectangle(x-self.r, y-self.r, x+self.r, y+self.r, tags='box')
        self.make_binds()




class Demo(A.Demo):
    """ a demo for configuring arrow """


    tselected=False

    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        
        self.demo_main_frame.master.title("Arrowhead Editor Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_main_frame, text=
  "This widget allows you to experiment with different widths and arrowhead shapes for lines in canvases. " 
  "To change the line width or the shape of the arrowhead, drag any of the three boxes attached to the oversized arrow.  " 
  "The arrows on the right give examples at normal scale.  " 
  "The text at the bottom shows the configuration options as you'd enter them for a canvas line item."
  , width=60, wraplength='13.5c')
        self.cvs=Tk.Canvas(self.demo_frame, relief=Tk.SUNKEN, borderwidth=2, width=500, height=350)
        self.cvs.pack(expand=1, fill=Tk.BOTH)

        # arrow info
        self.a = 8
        self.b = 10
        self.c = 3
        self.width = 2
        self.x1 = 40
        self.x2 = 350
        self.y = 150
        
        # the separator
        self.cvs.create_line(self.x2+50, 0, self.x2+50, 1000, width=2)   # separate line

        # dragging boxes
        self.box1 = Box(self.cvs, self.x2-10*self.a, self.y, self.arrow_move1, self.b1_move)
        self.box2 = Box(self.cvs, self.x2-10*self.b, self.y-(10*self.c+5*self.width), self.arrow_move2, self.b2_move)
        self.box3 = Box(self.cvs, self.x1, self.y-5*self.width, self.arrow_move3, self.b3_move)
                            
        # draw arrows
        self.arrow_setup()




    def b1_move(self, event):
        x = A.i_range(event.x, 100, self.x2)
        self.cvs.move(self.box1.id, x - self.box1.x0, 0)
        self.box1.x0 = x

        
    def b2_move(self, event):
        x = A.i_range(event.x, 100, self.x2)
        y = A.i_range(event.y, self.y-100-5*self.width, self.y-self.width*5)
        self.cvs.move(self.box2.id, x - self.box2.x0, y-self.box2.y0)
        self.box2.x0 = x
        self.box2.y0 = y


    def b3_move(self, event):
        y = A.i_range(event.y, 50, self.y)
        self.cvs.move(self.box3.id, 0, y-self.box3.y0)
        self.box3.y0 = y



    def arrow_setup(self):
        """
arrowSetup --
This procedure regenerates all the text and graphics in the canvas
window.  It's called when the canvas is initially created, and also
whenever any of the parameters of the arrow head are changed
interactively.
"""
        small_tips = (5,5,2)

        self.cvs.delete('arrow')
        self.big_arrow = self.cvs.create_line(self.x1, self.y, self.x2, self.y,
                                              arrow=Tk.LAST, width=10*self.width,
                                              arrowshape=(10*self.a, 10*self.b, 10*self.c),
                                              fill= 'SkyBlue1', tags='arrow')
        xtip = self.x2-10*self.b
        dy  = 10*self.c+5*self.width
        self.cvs.create_line(self.x2, self.y, xtip, self.y + dy, self.x2-10*self.a, self.y, xtip,
                             self.y-dy, self.x2, self.y,
                             width=2, capstyle=Tk.ROUND, joinstyle=Tk.ROUND, tags='arrow') ##??


       # Create three arrows in actual size with the same parameters

        x2a = self.x2+100
        self.cvs.create_line(x2a, self.y-125, x2a, self.y-75, width=self.width, arrow=Tk.BOTH,
                            arrowshape=(self.a, self.b, self.c), tags='arrow')   # sample line 1
        self.cvs.create_line(x2a-25, self.y, x2a+25, self.y, width=self.width, arrow=Tk.BOTH,
                            arrowshape=(self.a, self.b, self.c), tags='arrow')   # sample line 2
        self.cvs.create_line(x2a-25, self.y+75, x2a+25, self.y+125, width=self.width, arrow=Tk.BOTH,
                            arrowshape=(self.a, self.b, self.c), tags='arrow')   # sample line 3
       
      # Create a bunch of other arrows and text items showing the
      # current dimensions.

        x2a=self.x2+10
        self.cvs.create_line(x2a, self.y-5*self.width, x2a, self.y-dy, arrow=Tk.BOTH, arrowshape=small_tips, tags='arrow')
        self.cvs.create_text(self.x2+15, self.y-dy+5*self.c, text=str(self.c), anchor=Tk.W, tags='arrow')

        x1a= self.x1-10
        self.cvs.create_line(x1a, self.y-5*self.width, x1a, self.y+5*self.width,
                             arrow=Tk.BOTH, arrowshape=small_tips, tags='arrow')
        self.cvs.create_text(self.x1-15, self.y, text=str(self.width), anchor=Tk.E, tags='arrow')

        ya =self.y+5*self.width+10*self.c+10
        self.cvs.create_line(self.x2-10*self.a, ya, self.x2, ya, arrow=Tk.BOTH, arrowshape=small_tips, tags='arrow')
        self.cvs.create_text(self.x2-5*self.a, ya+5, text=str(self.a), anchor=Tk.N, tags='arrow')

        ya += 25
        self.cvs.create_line(self.x2-10*self.b, ya, self.x2, ya, arrow=Tk.BOTH, arrowshape=small_tips, tags='arrow')
        self.cvs.create_text(self.x2-5*self.b, ya+5, text=str(self.b), anchor=Tk.N, tags='arrow')

        self.cvs.create_text(self.x1, 310, text='width = %d' % (self.width),
                             anchor=Tk.W, font=('Helvetica', '18'), tags='arrow')
        self.cvs.create_text(self.x1, 330, text='arrowshape = (%d, %d, %d)' % (self.a, self.b, self.c),
                           anchor=Tk.W, font=('Helvetica', '18'), tags='arrow')

        self.box1.renew(self.x2-10*self.a, self.y)
        self.box2.renew(self.x2-10*self.b, self.y-(10*self.c+5*self.width))
        self.box3.renew(self.x1, self.y-5*self.width)


    def arrow_move1(self, event):
        """
arrow_move1 --
This procedure is called for each mouse motion event on box1 (the
 one at the vertex of the arrow).  It updates the controlling parameters
 for the line and arrowhead.
"""
        a1 = A.i_range((self.x2+5-event.x)/10, 0, 25)
        if(a1 != self.a):
            self.cvs.move(self.box1.id, 10*(self.a-a1), 0)
            self.a = a1
            self.arrow_setup()


    def arrow_move2(self, event):
        """
arrow_move2 --
This procedure is called for each mouse motion event on box2 (the
one at the trailing tip of the arrowhead).  It updates the controlling
parameters for the line and arrowhead.
"""
        b1 = A.i_range((self.x2+5-event.x)/10, 0, 25)
        c1 = A.i_range((self.y+5-event.y-5*self.width)/10, 0, 10)
        if not (self.b == b1 and  self.c == c1):
            self.cvs.move(self.box2.id, 10*(self.b-b1), 10*(self.c-c1))
            self.b = b1
            self.c = c1
            self.arrow_setup()


    def arrow_move3(self, event):
        """
arrowMove3 --
This procedure is called for each mouse motion event on box3 (the
one that controls the thickness of the line).  It updates the
controlling parameters for the line and arrowhead.
"""
        w1 = A.i_range((self.y+2-event.y)/5, 0, 20)
        if(w1 != self.width):
            self.cvs.move(self.box3.id, 0, 5*(self.width-w1))
            self.width=w1
            self.arrow_setup()




##----------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


