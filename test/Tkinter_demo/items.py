#! /usr/bin/env python

"""
items.py

This demonstration script creates a canvas that displays the
canvas item types.

June 14, 2005
"""
import Tkinter as Tk
import template as A
import re


class CanvasItem:
    id = None
    canvas = None
    color0 = None
    color1 = 'SteelBlue2'

    def __init__(self, cvs):
        self.canvas = cvs
    
    def make_binds(self):
        self.canvas.tag_bind(self.id, '<1>', self.drag_start)
        self.canvas.tag_bind(self.id, '<Button1-Motion>', self.dragging)
        self.canvas.tag_bind(self.id, '<Enter>', self.color_change)
        self.canvas.tag_bind(self.id, '<Leave>', self.color_original)

    def drag_start(self, event):
        self.x = event.x
        self.y = event.y

    def dragging(self, event):
        x1 = event.x
        y1 = event.y
        self.canvas.move(self.id, x1-self.x, y1-self.y)
        self.x = x1
        self.y = y1

    def color_original(self,event):
        str = self.canvas.itemcget(self.id, 'tags')
        tag = str.split().pop(0)                         # string " current" is added to the tag
                                                         # if the mouse pointer is on the object
        if(tag=='fill'):
            self.canvas.itemconfigure(self.id, fill=self.color0)
        elif(tag=='outline'):
            self.canvas.itemconfigure(self.id, outline=self.color0)
        elif(tag=='background'):
            self.canvas.itemconfigure(self.id, background=self.color0)

    def color_change(self,event):
        str = self.canvas.itemcget(self.id, 'tags')
        tag = str.split().pop(0)
        if(tag=='fill'):
            self.canvas.itemconfigure(self.id, fill=self.color1)
        elif(tag=='outline'):
            self.canvas.itemconfigure(self.id, outline=self.color1)
        elif(tag=='background'):
            self.canvas.itemconfigure(self.id, background=self.color1)


class CanvasArc(CanvasItem):
    def __init__(self, canvas, x0, y0, x1, y1, **key):
        CanvasItem.__init__(self, canvas)
        if ('stipple' in key) and (not 'fill' in key):
            key['fill'] = 'black'
        if (key['tags'] == 'fill') :
            self.color0 = key['fill']
        elif(key['tags'] == 'outline'):
            self.color0 = key['outline']
        self.id = self.canvas.create_arc(x0, y0, x1, y1, **key)
        self.make_binds()


class CanvasBitmap(CanvasItem):
    def __init__(self, canvas, x, y, **key):
        CanvasItem.__init__(self, canvas)
        if not 'backgound' in key:
            key['background'] = ''
        self.color0 = key['background']
        self.id = self.canvas.create_bitmap(x, y, **key)
        self.make_binds()

class CanvasLine(CanvasItem):
    def __init__(self, canvas, *pos, **key):
        CanvasItem.__init__(self, canvas)
        if not 'fill' in key:
            key['fill'] = 'black'
        self.color0 = key['fill']
        self.id = self.canvas.create_line(*pos, **key)
        self.make_binds()

class CanvasOval(CanvasItem):
    def __init__(self, canvas, x0, y0, x1, y1, **key):
        CanvasItem.__init__(self, canvas)
        if ('stipple' in key) and (not 'fill' in key):
            key['fill'] = 'black'
        if ((key['tags'] == 'fill') and ('fill' in key)) :
            self.color0 = key['fill']
        elif((key['tags'] == 'outline') and ('outline' in key)):
            self.color0 = key['outline']
        self.id = self.canvas.create_oval(x0, y0, x1, y1, **key)
        self.make_binds()
        

class CanvasPolygon(CanvasItem):
    def __init__(self, canvas, *pos, **key):
        CanvasItem.__init__(self, canvas)
        if ('stipple' in key) and (not 'fill' in key):
            key['fill'] = 'black'
        if (key['tags'] == 'fill') :
            if not 'fill' in key:
                key['fill'] = 'black'
            self.color0 = key['fill']
        elif(key['tags'] == 'outline'):
            if not 'outline' in key:
                key['outline'] = 'black'
            self.color0 = key['outline']
        self.id = self.canvas.create_polygon(*pos, **key)
        self.make_binds()



class CanvasRectangle(CanvasItem):
    def __init__(self, canvas, x0, y0, x1, y1, **key):
        CanvasItem.__init__(self, canvas)
        if ('stipple' in key) and (not 'fill' in key):
            key['fill'] = 'black'
        if (key['tags'] == 'fill') :
            if not 'fill' in key:
                key['fill'] = ''
            self.color0 = key['fill']
        elif(key['tags'] == 'outline'):
            if not 'outline' in key:
                key['outline']='black'
            self.color0 = key['outline']
        self.id = self.canvas.create_rectangle(x0, y0, x1, y1, **key)
        self.make_binds()


class CanvasText(CanvasItem):
    def __init__(self, canvas, *pos, **key):
        CanvasItem.__init__(self, canvas)
        if not 'fill' in key:
            key['fill'] = 'black'
        self.color0 = key['fill']
        self.id = self.canvas.create_text(*pos, **key)
        self.make_binds()




        
        
class Demo(A.Demo):
    """
    a demo for buttons
    """

    
    font1 = ("Helvetica", "12")
    font2 = ("Helvetica", "24", "bold")
    angle=None
    c_width=None
    c_height=None

    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()
        
        
    
    def ini_frame(self):
        
        self.demo_main_frame.master.title("Canvas Item Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_frame, text=
        "This window contains a canvas widget with examples of the various kinds of items supported by canvases. " 
        "The following operations are supported:\n  " 
        "Button-1 drag:\tmoves item under pointer.\n  " 
        "Button-2 drag:\trepositions view.\n  " 
        "Button-3 drag:\tstrokes out area.\n  " 
        "Ctrl+f:\t\tprints items under area."
        ,width=70,   wraplength='14.5c')

        fa = Tk.Frame(self.demo_frame, border=2)
        fa.pack(fill=Tk.BOTH, expand=1)
        self.cvs = Tk.Canvas(fa, scrollregion=("0c", "0c",  "30c",  "24c"), width="15c", height="10c",
                                   relief=Tk.SUNKEN, borderwidth=2)  # does not expand
        self.cvs.grid(row=0, column=0, sticky= Tk.N+Tk.E+Tk.W+Tk.S)
        
        xscroll = Tk.Scrollbar(fa, orient=Tk.HORIZONTAL, command=self.cvs.xview)
        xscroll.grid(row=1, column=0, sticky=Tk.E+Tk.W)

        yscroll = Tk.Scrollbar(fa, orient=Tk.VERTICAL, command=self.cvs.yview)
        yscroll.grid(row=0, column=1, sticky=Tk.N+Tk.S)
        
        self.cvs.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        fa.grid_rowconfigure(0, weight=1, minsize=0)     
        fa.grid_columnconfigure(0, weight=1, minsize=0)  


        # Display a 3x3 rectangular grid.
        self.cvs.create_rectangle('0c', '0c', '30c', '24c', width=2)
        self.cvs.create_line('0c', '8c', '30c', '8c', width=2)
        self.cvs.create_line('0c', '16c', '30c', '16c', width=2)
        self.cvs.create_line('10c', '0c', '10c', '24c', width=2)
        self.cvs.create_line('20c', '0c', '20c', '24c', width=2)

        if(self.cvs.winfo_depth() > 1):
            self.blue = "DeepSkyBlue3"
            self.red = "red"
            self.bisque = "bisque3"
            self.green = "SeaGreen3"
        else:
            self.blue = "black"
            self.red = "black"
            self.bisque = "black"
            self.green = "black"

        # Set up demos within each of the areas of the grid.
        self.cvs.create_text('5c', '.2c', text='Lines', anchor=Tk.N)
        CanvasLine(self.cvs, '1c', '1c', '3c', '1c', '1c', '4c', '3c', '4c', width='2m',
                   fill=self.blue, cap='butt', join='miter', tags='fill')
        CanvasLine(self.cvs, '4.67c', '1c', '4.67c', '4c',  arrow='last', tags='fill')
        CanvasLine(self.cvs, '6.33c', '1c', '6.33c', '4c', arrow='both', tags='fill')
        CanvasLine(self.cvs, '5c', '6c', '9c', '6c', '9c', '1c', '8c', '1c', '8c', '4.8c',
                    '8.8c', '4.8c', '8.8c', '1.2c', '8.2c', '1.2c', '8.2c', '4.6c',
                    '8.6c', '4.6c', '8.6c', '1.4c', '8.4c', '1.4c', '8.4c', '4.4c',
                     width=3, fill=self.red, tags='fill')
        CanvasLine(self.cvs, '1c', '5c', '7c', '5c', '7c', '7c', '9c', '7c', width='.5c',
                   stipple='@gray25.bmp', arrow='both',  arrowshape=(15, 15, 7), tags='fill')   
        CanvasLine(self.cvs, '1c', '7c', '1.75c', '5.8c', '2.5c', '7c', '3.25c', '5.8c', '4c', '7c',
                     width='.5c', cap='round', join='round', tags='fill')
        self.cvs.create_text('15c', '.2c', text='Curves, (smoothed lines)', anchor=Tk.N)
        CanvasLine(self.cvs,'11c', '4c', '11.5c', '1c', '13.5c', '1c', '14c', '4c', smooth=1,
                                     fill=self.blue, tags='fill')
        CanvasLine(self.cvs,'15.5c', '1c', '19.5c', '1.5c', '15.5c', '4.5c', '19.5c', '4c',
                                    smooth=1, arrow='both', width=3, tags='fill')
        CanvasLine(self.cvs, '12c', '6c', '13.5c', '4.5c', '16.5c', '7.5c', '18c', '6c', '16.5c',
                                   '4.5c', '13.5c', '7.5c', '12c', '6c', smooth='on', width='3m', cap='round',
                                    stipple='@gray25.bmp', fill=self.red, tags='fill')         
        self.cvs.create_text('25c', '.2c', text='Polygons', anchor=Tk.N)
        CanvasPolygon(self.cvs, '21c', '1.0c', '22.5c', '1.75c', '24c', '1.0c', '23.25c', '2.5c', '24c',
                      '4.0c', '22.5c', '3.25c', '21c', '4.0c', '21.75c', '2.5c',
                       fill=self.green, outline='black', width=4, tags='fill')
        CanvasPolygon(self.cvs, '25c', '4c', '25c', '4c', '25c', '1c', '26c', '1c', '27c',
                      '4c', '28c', '1c', '29c', '1c', '29c', '4c', '29c', '4c',
                      fill=self.red, smooth=1, tags='fill')
        CanvasPolygon(self.cvs, '22c', '4.5c', '25c', '4.5c', '25c', '6.75c', '28c', '6.75c',
                      '28c', '5.25c', '24c', '5.25c', '24c', '6.0c', '26c', '6c',  '26c', '7.5c', '22c', '7.5c',
                      stipple='@gray25.bmp', outline='black',  tags='fill')
        self.cvs.create_text('5c', '8.2c', text='Rectangles', anchor=Tk.N)
        CanvasRectangle(self.cvs, '1c', '9.5c', '4c', '12.5c', outline=self.red, width='3m', tags='outline')
        CanvasRectangle(self.cvs, '0.5c', '13.5c', '4.5c', '15.5c', fill=self.green, tags='fill')
        CanvasRectangle(self.cvs, '6c', '10c', '9c', '15c', outline='',
                             stipple='@gray25.bmp', fill=self.blue, tags='fill')
        self.cvs.create_text('15c', '8.2c', text='Ovals', anchor=Tk.N)
        CanvasOval(self.cvs, '11c', '9.5c', '14c', '12.5c', outline=self.red, width='3m', tags='outline')
        CanvasOval(self.cvs, '10.5c', '13.5c', '14.5c', '15.5c', fill=self.green, tags='fill')
        CanvasOval(self.cvs, '16c', '10c', '19c', '15c', outline='',
                                   stipple='@gray25.bmp', fill=self.blue, tags='fill')
        self.cvs.create_text('25c', '8.2c', text='Text', anchor=Tk.N)
        self.cvs.create_rectangle('22.4c', '8.9c', '22.6c', '9.1c')
        CanvasText(self.cvs, '22.5c', '9c', anchor=Tk.N, font=self.font1, width='4c',
                  text='A short string of text word-wrapped justified left and anchored north (at the top).' +
                  'The   rectangles show the anchor points for each piece of text.',  tags='fill')
        self.cvs.create_rectangle('25.4c', '10.9c', '25.6c', '11.1c')
        CanvasText(self.cvs, '25.5c', '11c', anchor=Tk.W, font=self.font1, fill=self.blue,
                  text='Several lines,\n each centered\nindividually\nand all anchored\nat the left edge.',
                  justify='center', tags='fill')
        self.cvs.create_rectangle('24.9c', '13.9c', '25.1c', '14.1c')
        CanvasText(self.cvs, '25c', '14c', font=self.font2, anchor=Tk.CENTER, fill=self.red,
                   stipple='gray50', text='Stippled characters', tags='fill')
        self.cvs.create_text('5c', '16.2c', text='Arcs', anchor=Tk.N)
        CanvasArc(self.cvs, '0.5c', '17c', '7c', '20c', fill=self.green, outline='black',
                  start=45, extent=270, style=Tk.PIESLICE, tags='fill')
        CanvasArc(self.cvs, '6.5c', '17c', '9.5c', '20c', width='4m', style=Tk.ARC,
                  outline=self.blue, start=-135, extent=270, tags='outline', outlinestipple='@gray25.bmp')
        CanvasArc(self.cvs, '0.5c', '20c', '9.5c', '24c', width='4m', style=Tk.PIESLICE, fill='',
                  outline=self.red, start=225, extent=-90, tags='outline')
        CanvasArc(self.cvs, '5.5c', '20.5c', '9.5c', '23.5c', width='4m', style=Tk.CHORD,
                                    fill=self.blue, outline='', start=45, extent=270, tags='fill')
        self.cvs.create_text('15c', '16.2c', text='Bitmaps', anchor=Tk.N)
        CanvasBitmap(self.cvs, '13c', '20c', tags='background', bitmap='@face.bmp')
        CanvasBitmap(self.cvs, '17c', '18.5c', tags='background', bitmap='@noletter.bmp')
        CanvasBitmap(self.cvs, '17c', '21.5c', tags='background', bitmap='@letters.bmp')
        self.cvs.create_text('25c', '16.2c', text='Windows', anchor=Tk.N)
        self.cvs_button = Tk.Button(self.cvs, text="Press Me", command =self.but_press_red) 
        self.cvs.create_window('21c', '18c', window=self.cvs_button, anchor=Tk.NW, tags='window')
        self.cvs_entry=Tk.Entry(self.cvs, width=20, relief=Tk.SUNKEN)
        self.cvs_entry.insert(Tk.END, 'Edit this text')
        self.cvs.create_window('21c', '21c', window=self.cvs_entry, anchor=Tk.NW, tags='window')
        self.cvs_scale = Tk.Scale(self.cvs, from_=0, to=100, length='6c', sliderlength='0.4c',
                                   width='0.5c', tickinterval=0)
        self.cvs.create_window('28.5c', '17.5c', window=self.cvs_scale, anchor=Tk.N, tags='window')
        self.cvs.create_text('21c', '17.9c', text='Button:', anchor=Tk.SW)
        self.cvs.create_text('21c', '20.9c', text='Entry:', anchor=Tk.SW)
        self.cvs.create_text('28.5c', '17.4c', text='Scale:', anchor=Tk.S)

        # bindings
        self.cvs.bind('<3>', self.create_angle_ini)
        self.cvs.bind('<Button3-Motion>', self.create_angle)
        self.cvs.bind('<2>', self.mouse_scroll_start)
        self.cvs.bind('<Button2-Motion>', self.mouse_scrolling)



    def but_press_red(self):
        self.temp = self.cvs.create_text('25c', '18.1c', text='Ouch!!', fill=self.red, anchor=Tk.N)
        self.cvs.after(500, self.delete_temp)

    def delete_temp(self):
        self.cvs.delete(self.temp)

    def create_angle_ini(self, event):
        if self.angle:
            self.cvs.delete(self.angle)        # event.x is x coordinate form the left size of the canvas.
        self.xa0 = self.cvs.canvasx(event.x)   # if the canvas is scrolled, event.x differs from the coordinate
        self.ya0 = self.cvs.canvasy(event.y)   # of the screen. `.canvasx' method is used to correct the dirrerence.


    def create_angle(self, event):
        self.cvs.delete(self.angle)
        self.angle=self.cvs.create_rectangle(self.xa0, self.ya0,
                             self.cvs.canvasx(event.x), self.cvs.canvasy(event.y))

    def mouse_scroll_start(self, event):
        self.xs0 = event.x
        self.ys0 = event.y
        self.xf1, self.xf2 = self.xscroll.get()
        self.yf1, self.yf2 = self.yscroll.get()
        self.fdx = self.xf2-self.xf1
        self.fdy = self.yf2-self.yf1

    def mouse_scrolling(self, event):
        dx = (event.x - self.xs0)*0.002
        dy = (event.y - self.ys0)*0.002
        x1 = self.xf1+dx
        x2 = x1+ self.fdx
        y1 = self.yf1+dy
        y2 = y1+self.fdy
        if (x1>=-0.03 and x2 <= 1.03):
            self.xscroll.set(x1, x2)
            self.cvs.xview_moveto(x1)
        if (y1>=-0.03 and y2 <= 1.03):
            self.yscroll.set(y1, y2)
            self.cvs.yview_moveto(y1)
 
##----------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()

