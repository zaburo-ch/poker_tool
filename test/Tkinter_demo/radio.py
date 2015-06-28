#! /usr/bin/env python

"""
radio.py

This demonstration script creates a toplevel window containing
several radiobutton widgets.

June 15, 2005
"""


import Tkinter as Tk
import template as A

class Demo(A.Demo):
    """
    a demo for radio buttons
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
        "Three groups of radiobuttons are displayed below.  " 
        "If you click on a button then the button will become selected exclusively among all the buttons in its group.  " 
        "A Tcl variable is associated with each group to indicate which of the group's buttons is selected.  " 
        "Click the \"See Variables\" button to see the current values of the variables."
        , width=45, wraplength='9c')

        f = Tk.Frame(self.demo_frame)
        f.pack()

                           
        
        lf_left = Tk.LabelFrame(f, text='Point Size', padx=2)
        self.lf_mid  = Tk.LabelFrame(f, text='Color', padx=2)
        lf_right  = Tk.LabelFrame(f, text='Alignment', padx=2)
        lf_left.pack(side=Tk.LEFT, expand=1, pady=10, padx=10)
        self.lf_mid.pack(side=Tk.LEFT, expand=1, pady=10, padx=10)
        lf_right.pack(side=Tk.LEFT, expand=1, pady=10, padx=10)

        # variables 
        self.fsize=Tk.IntVar()
        self.color=Tk.StringVar()
        self.align = Tk.StringVar()
        
        for i, j in enumerate((10, 12, 14, 18, 24)):
            rd = Tk.Radiobutton(lf_left, text = 'Point Size %d' % (j), variable=self.fsize,
                                   relief=Tk.FLAT, value=j)
            rd.pack(pady=2, anchor=Tk.W, fill=Tk.X)

            
        
        for i, c in enumerate(('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple')):
            cl = c.lower()
            rc = Tk.Radiobutton(self.lf_mid, text=c, variable=self.color, relief=Tk.FLAT, value=cl,
                                 anchor=Tk.W, command=self.change_color)
            rc.pack(pady=2, fill=Tk.X)

        self.ra=dict()

        self.ra['center'] = Tk.Label(lf_right, text='Label', bitmap='questhead', compound=Tk.LEFT)
        self.ra['center'].configure(width=self.ra['center'].winfo_reqwidth(), compound=Tk.TOP)
        self.ra['center'].configure(height=self.ra['center'].winfo_reqheight())


        for a in ('Top', 'Left', 'Right', 'Bottom'):
            al = a.lower()
            self.ra[al] = \
                    Tk.Radiobutton(lf_right, text=a, variable=self.align, relief=Tk.FLAT, value=al,
                                   indicatoron=0, width=7, command=self.change_align)

        for k, v in self.ra.iteritems():
            if(k=='top'):
                r, c = 0, 1
            elif(k=='left'):
                r, c = 1, 0
            elif(k=='center'):
                r, c = 1, 1
            elif(k=='right'):
                r, c = 1, 2
            elif(k=='bottom'):
                r, c = 2, 1
            v.grid(row=r, column=c)

        bv = Tk.Button(self.demo_buttons, text='See Variables', width=20,
                       command=A.ShowVars(self.demo_main_frame.master, 0,
                        ('size:', str(self.fsize)), ('color:', self.color), ('align:', self.align)))
        bv.pack(side=Tk.RIGHT, padx=10, pady=5)
        



    def change_color(self):
        self.lf_mid.configure(fg=self.color.get())

    def change_align(self):
        self.ra['center'].configure(compound=self.align.get())




##----------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()
