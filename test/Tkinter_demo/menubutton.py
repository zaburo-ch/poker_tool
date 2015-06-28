#! /usr/bin/env python

"""
menubutton.py 

This demonstration script creates a window with a bunch of menus
and cascaded menus using menubuttons.

June 22, 2005
"""


import Tkinter as Tk
import template as A
import menu as M
import math


def get_row_column(i):
    if i==0:
        return (0,1, Tk.N)
    elif i==1:
        return (1,0, Tk.W)
    elif i==2:
        return (1,2, Tk.E)
    else:
        return (2,1, Tk.S)



class ColorPalette(Tk.Menu):
    """ a menu to select a color """
    def __init__(self, master, var, *colors):
        Tk.Menu.__init__(self, master, tearoff=0, borderwidth=3, relief=Tk.SUNKEN)
        self.var = var
        self.dim = math.ceil(math.sqrt(len(colors)))
        for i, c in enumerate(colors):
            self.add_radiobutton(background=c, selectcolor='gray25', value=c, variable=self.var)
            if (i%self.dim == 0 and i>0):
                self.entryconfigure(i, columnbreak=1)



class Demo(A.Demo):
    """ a demo for menu buttons """
    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_demo(self):
        """ override A.Demo.ini_demo"""
        ## added ---
        self.echo = Tk.StringVar()
        self.statusbar = Tk.Frame(self.demo_main_frame)
        self.echo_label = Tk.Label(self.statusbar, textvariable= self.echo, relief=Tk.SUNKEN, bd=1,
                                    font=('Helvetica', '10'), anchor=Tk.W, width=65)
        self.echo_label.pack(side=Tk.LEFT)
        self.statusbar.pack(side=Tk.BOTTOM)
        #----
        self.demo_frame = Tk.Frame(self.demo_main_frame)
        self.demo_buttons = A.ButtonFrame(self.demo_main_frame, "Dismiss", self.demo_destroy, "Show Code", self.show_code)
        self.demo_main_frame.pack(fill=Tk.BOTH, expand=1, padx=3, pady=3)
        self.demo_frame.pack(fill=Tk.BOTH, expand=1, padx=20, pady=30)
        self.demo_buttons.pack(side=Tk.BOTTOM, expand=0, pady=5)



    def ini_frame(self):
        """ this method has been overrode."""
        
        self.demo_main_frame.master.title("Menu Button Demonstration")
        self.demo_main_frame.master.geometry('+50+50')

        f = Tk.Frame(self.demo_frame)
        f.grid(row=1, column=1, sticky=Tk.N+Tk.S+Tk.E+Tk.W, padx=20, pady=30)
        mb=A.newlist(4)
        m=A.newlist(4)
        for i, title in enumerate(['Below','Right','Left', 'Above']):
            mb[i]= Tk.Menubutton(self.demo_frame, text=title, underline=0, direction=title.lower(), relief=Tk.RAISED)
            m[i] = Tk.Menu(mb[i], tearoff=0)
            mb[i].configure(menu=m[i])
            for count in ['first', 'second']:  
                m[i].add_command(label=title + ' menu: '+count+' item',
                    command=M.Echo(self.echo, 'You have selected the '+count+' item from the ' + title +' menu.'))
            r,c,s = get_row_column(i)
            mb[i].grid(row=r, column=c, sticky=s)

        lbl = Tk.Label(f, text=
        "This is a demonstration of menubuttons. "
        "The \"Below\" menubutton pops its menu below the button; the \"Right\" button pops to the right, etc. "
        "There are two option menus directly below this text; "
        "one is just a standard menu and the other is a 16-color palette."
        , width=30, wraplength='7c', font=('Helvetica', '14'), justify=Tk.LEFT)

        lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        ott = ['one', 'two', 'three']
        count = Tk.StringVar()
        count.set(ott[0])
        collis = ['Black', 'red4',   'DarkGreen', 'NavyBlue', 'gray75', 'Red', 'Green',
                  'Blue', 'gray50', 'Yellow', 'Cyan', 'Magenta', 'White', 'Brown', 'DarkSeaGreen', 'DarkViolet']
        color = Tk.StringVar()
        color.set(collis[1])
        op1 = Tk.OptionMenu(f, count, *ott)
        op1.grid(row=1, column=0)
        op2 = Tk.OptionMenu(f, color, *collis)
        op2.configure(menu=ColorPalette(op2, color, *collis))
        op2.grid(row=1, column=1)

        
        
##-----------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()
