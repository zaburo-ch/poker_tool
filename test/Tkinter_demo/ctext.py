#! /usr/bin/env python

"""
ctext.py

This demonstration script creates a canvas widget with a text
item that can be edited and reconfigured in various ways.

June 14, 2005
"""
import Tkinter as Tk
import template as A


class CommandRectangle:
    id = None
    plot = None
    color0 = None
    color1 = 'black'
    width= 30
    height= 30
    
    
    def __init__(self, canvas, x0, y0, **key):
        self.canvas = canvas
        self.command= key['command']
        self.color0=key['fill']
        del key['command']
        self.id = self.canvas.create_rectangle(x0, y0, x0+self.width, y0+self.height, **key)
        self.canvas.tag_bind(self.id, '<1>', self.command)
        self.canvas.tag_bind(self.id, '<Enter>', self.color_change)
        self.canvas.tag_bind(self.id, '<Leave>', self.color_original)

    def color_original(self,event):
        self.canvas.itemconfigure(self.id, fill=self.color0)

    def color_change(self,event):
        self.canvas.itemconfigure(self.id, fill=self.color1)



class Demo(A.Demo):
    """ a demo for canvas text """

    tselected=False

    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()
            
             
    def ini_frame(self):
        
        self.demo_main_frame.master.title("Canvas Text Demonstration")
        self.demo_main_frame.master.geometry("+50+50")        
        A.Label(self.demo_frame, text=
                  "This window displays a string of text to demonstrate the text facilities of canvas widgets." 
                  "You can click in the boxes to adjust the position of the text " 
                  "relative to its positioning point or change its justification. "
                  "The text also supports the following simple bindings for editing:\n" 
                   "1. You can point, click, and type.\n" 
                   "2. You can also select with button 1.\n" 
                   "3. You can copy the selection to the mouse position with button 2.\n" 
                   "4. Backspace and Control+h delete the selection if there is one;\n" 
                   "   otherwise they delete the character just before the insertion cursor.\n" 
                   "5. Delete deletes the selection if there is one; otherwise it deletes\n"
                   "   the character just after the insertion cursor."
        , width=57,  wraplength='12c')
        self.cvs=Tk.Canvas(self.demo_frame, relief=Tk.FLAT, borderwidth=0, width=500, height=350, selectborderwidth=0)
        self.cvs.pack(expand=1, fill=Tk.BOTH)

        self.cvs.create_rectangle(245,195,255,205, outline='black', fill='red')
        self.ctext = self.cvs.create_text(250, 200, text=
        "This is just a string of text to demonstrate the text facilities of canvas widgets. " 
        "Bindings have been defined to support editing (see above)."
        , width= 440, anchor=Tk.N, font=('Helvetica', '24'), justify=Tk.LEFT)

        self.cvs.tag_bind(self.ctext, '<1>', self.put_cursol)
        self.cvs.tag_bind(self.ctext, '<Button1-Motion>', self.select_region)
        self.cvs.tag_bind(self.ctext, '<Shift-1>', self.mark_it)
        self.cvs.tag_bind(self.ctext, '<Shift-Button1-Motion>', self.select_region) #?? Shift-Button1
        self.cvs.tag_bind(self.ctext, '<KeyPress>', self.insert_text)
        self.cvs.tag_bind(self.ctext, '<Return>', self.insert_return)
        self.cvs.tag_bind(self.ctext, '<Control-h>', self.text_backspace)
        self.cvs.tag_bind(self.ctext, '<BackSpace>', self.text_backspace)
        self.cvs.tag_bind(self.ctext, '<Delete>', self.text_del)
        self.cvs.tag_bind(self.ctext, '<2>', self.text_paste)

        # text position rectangles
        pos_cmds = {(0,0):self.pse, (0,1):self.pe, (0,2):self.pne,
                         (1,0):self.ps,  (1,1):self.pc, (1,2):self.pn,
                         (2,0):self.psw, (2,1):self.pw, (2,2):self.pnw}

        jcmds=(self.jl, self.jc, self.jr)

        self.cvs.create_text(95, 45, text='Text Position', anchor=Tk.S, font=('Times', '24'), fill='brown')
        for i in range(3):
            for j in range(3):
                CommandRectangle(self.cvs, 50+i*30, 50+j*30, outline='black', fill= 'LightSkyBlue1', width=1,
                                 command = pos_cmds[(i, j)])
                                 
        center_rect = self.cvs.create_rectangle(90,90,100,100, outline='black', fill='red')

        self.cvs.create_text(395, 45, text='Justification', anchor=Tk.S, font=('Times', '24'), fill='brown')
        for i in range(3):
            CommandRectangle(self.cvs, 350+i*30, 50, command = jcmds[i], fill='SeaGreen2')

        self.cvs.tag_bind(center_rect, '<1>', self.pc)


    def pnw(self, event):
        self.cvs.itemconfigure(self.ctext, anchor=Tk.NW)

    def pw(self, event):
        self.cvs.itemconfigure(self.ctext, anchor=Tk.W)

    def psw(self, event):
        self.cvs.itemconfigure(self.ctext, anchor=Tk.SW)

    def pn(self, event):
        self.cvs.itemconfigure(self.ctext, anchor=Tk.N)

    def pc(self, event):
        self.cvs.itemconfigure(self.ctext, anchor=Tk.CENTER)

    def ps(self, event):
        self.cvs.itemconfigure(self.ctext, anchor=Tk.S)

    def pne(self, event):
        self.cvs.itemconfigure(self.ctext, anchor=Tk.NE)

    def pe(self, event):
        self.cvs.itemconfigure(self.ctext, anchor=Tk.E)

    def pse(self, event):
        self.cvs.itemconfigure(self.ctext, anchor=Tk.SE)

    def jl(self, event):
        self.cvs.itemconfigure(self.ctext, justify=Tk.LEFT)


    def jc(self, event):
        self.cvs.itemconfigure(self.ctext, justify=Tk.CENTER)


    def jr(self, event):
        self.cvs.itemconfigure(self.ctext, justify=Tk.RIGHT)

    def tdchars(self):
        self.cvs.dchars(self.ctext, self.tindex0, self.tindex1)
        self.tselected=False


        
    def put_cursol(self, event):
        if self.tselected:
            self.cvs.select_clear()
            self.tselected=False
        self.cvs.focus(self.ctext)
        self.cvs.focus_set()
        str = '@%d,%d' % (event.x, event.y)
        self.tindex0 = self.cvs.index(self.ctext, str)
        self.cvs.icursor(self.ctext, str)


    def select_region(self, event):
        self.tselected=True
        self.cvs.select_from(self.ctext, self.tindex0)
        str = '@%d,%d' % (event.x, event.y)
        self.tindex1 = self.cvs.index(self.ctext, str)
        self.cvs.select_to(self.ctext, self.tindex1)



    def mark_it(self, event):
        self.cvs.insert(self.ctext, self.tindex0, '!')


    def insert_text(self, event):
        c = event.char
        if c:
            if self.tselected:
                self.tdchars()
            self.cvs.insert(self.ctext, self.tindex0, c)
            self.tindex0 += 1


    def insert_return(self, event):
        if self.tselected:
            self.tdchars()
        self.cvs.insert(self.ctext, self.tindex0, '\n')
        self.tindex0 += 1

    def text_backspace(self, event):
        if self.tselected:
            self.tdchars()
        else:
            self.tindex0 -= 1
            self.cvs.dchars(self.ctext, self.tindex0)
        

    def text_del(self, event):
        if self.tselected:
            self.tdchars()
        else:
            self.cvs.dchars(self.ctext, self.tindex0)

    def text_paste(self, event):
        if self.tselected:
            str = self.cvs.selection_get()
            idx = '@%d,%d' % (event.x, event.y)
            self.cvs.insert(self.ctext, idx, str)
            self.cvs.icursor(self.ctext, idx)

        
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()

