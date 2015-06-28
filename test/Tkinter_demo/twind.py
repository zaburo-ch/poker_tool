#! /usr/bin/env python

"""
twind.py

This demonstration script creates a text widget with a bunch of
embedded windows.

June 20, 2005
"""


import Tkinter as Tk
import template as A
import plot as P

class ChangeBG:
    """ This is a class of functions to change the background of the widget. """
    
    def __init__(self, widget, bg):
        self.widget = widget
        self.bg = bg

    def __call__(self, *av):
        self.widget.configure(background=self.bg)


class BinText(Tk.Button):
    """ a class of buttons in a Tk.Text widget """
    
    def __init__(self, master, **key):
        self.master = master
        key['cursor'] = 'top_left_arrow'
        Tk.Button.__init__(self, self.master, **key)
        self.master.window_create(Tk.END, window=self, padx=3, pady=2)
    


class Demo(A.Demo):
    """ a demo class """



    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("Text Demonstration - Embedded Windows")
        self.demo_main_frame.master.geometry('550x550+50+50')
        self.f = Tk.Frame(self.demo_frame)
        self.f.pack(fill=Tk.BOTH, expand=1)
        yscroll = Tk.Scrollbar (self.f, orient=Tk.VERTICAL)
        yscroll.pack(side=Tk.RIGHT, fill=Tk.Y)
        self.stext= Tk.Text(self.f, wrap=Tk.WORD, font=('Helvetica', '12'), yscrollcommand=yscroll.set)
        yscroll.config(command=self.stext.yview)
        self.stext.pack(fill=Tk.BOTH, expand=1)
        self.default_bg=self.stext.cget('background')  
        
        self.stext.insert(Tk.END, 
                        "A text widget can contain other widgets embedded it.  "
                        "These are called \"embedded windows\", and they can consist of arbitrary widgets.  "
                        "For example, here are two embedded button widgets.  "
                        "You can click on the first button to "
                     )
        BinText(self.stext, text='Turn On', command=self.xscroll_on, cursor='top_left_arrow') 
        self.stext.insert(Tk.END,
                                  " horizontal scrolling, which also turns off word wrapping.  "
                                  "Or, you can click on the second button to\n")
                                  
        BinText(self.stext, text='Turn Off', command=self.xscroll_off) # arrow = pointer
        self.stext.insert(Tk.END, 
                          " horizontal scrolling and turn back on word wrapping.\n\n"
                          "Or, here is another example.  If you ")
        BinText(self.stext, text='Click Here', command=self.show_plot)
        self.c = None               # plotting widget
        self.stext.insert(Tk.END, " a canvas displaying an x-y plot will appear right here.")
        self.stext.mark_set('plot', Tk.INSERT)
        self.stext.mark_gravity('plot', Tk.LEFT)    # The mark stays the same  position
        self.stext.insert(Tk.END, "  You can drag the data points around with the mouse, "
                                  "or you can click here to ")
        BinText(self.stext, text='Delete', command=self.delete_plot) 
        self.stext.insert(Tk.END, " the plot again.\n\n"
                                  "You may also find it useful to put embedded windows in "
                                  "a text without any actual text.  In this case the "
                                  "text widget acts like a geometry manager.  For "
                                  "example, here is a collection of buttons laid out "
                                  "neatly into rows by the text widget.  These buttons "
                                  "can be used to change the background color of the "
                                  "text widget (\"Default\" restores the color to "
                                  "its default).  If you click on the button labeled "
                                  "\"Short\", it changes to a longer string so that "
                                  "you can see how the text widget automatically "
                                  "changes the layout.  Click on the button again "
                                  "to restore the short string.\n")
        self.stext.mark_set('idx0', Tk.INSERT)
        self.stext.mark_gravity('idx0', Tk.LEFT)
        BinText(self.stext, text='Default', command=self.set_default)
        embToggle = Tk.StringVar()
        embToggle.set('Short')
        ch = Tk.Checkbutton(self.stext, textvariable = embToggle, indicatoron=0, variable=embToggle,
                            cursor = 'top_left_arrow',
                            onvalue = 'A much longer string', offvalue='Short', pady=5, padx=2)
        self.stext.window_create(Tk.END,  window=ch, pady=5, padx=2)
                            
        for clr in ['AntiqueWhite3',  'Bisque1',  'Bisque2',  'Bisque3',  'Bisque4',  'SlateBlue3',  'RoyalBlue1',  
                    'SteelBlue2',  'DeepSkyBlue3',  'LightBlue1', 'DarkSlateGray1',  'Aquamarine2',  'DarkSeaGreen2',
                    'SeaGreen1', 'Yellow1',  'IndianRed1',  'IndianRed2',  'Tan1',  'Tan4']: 
            BinText(self.stext, text=clr, command=ChangeBG(self.stext, clr))

        self.stext.tag_add('cite', 'idx0', Tk.END)
        self.stext.tag_config('cite', lmargin1=30, lmargin2=30, rmargin=20)

        
    def xscroll_on(self):
        self.xscroll=Tk.Scrollbar(self.f, orient=Tk.HORIZONTAL, command=self.stext.xview)
        self.xscroll.pack(side=Tk.BOTTOM, fill=Tk.X)
        self.stext.configure(xscrollcommand=self.xscroll.set, wrap=Tk.NONE)

        
    def xscroll_off(self):
        self.xscroll.destroy()
        self.stext.configure(xscrollcommand=Tk.NONE, wrap=Tk.WORD)

        
    def show_plot(self):
        if not self.c:
            self.c = P.Plot(self.stext, P.XY_DATA, "A Simple Plot", (0, 100), (0, 250), range(0,105,10), range(0,255,50))
            self.c.configure(cursor='top_left_arrow')
            self.stext.insert('plot', '\n')
            self.stext.window_create('plot', window=self.c, padx=15, pady=15)
            self.stext.tag_add('center', 'plot') 
            self.stext.tag_config('center', justify=Tk.CENTER)
            self.stext.insert('plot', '\n')
        

    def delete_plot(self):
        if self.c:
            for i in range(3):
                self.stext.delete('plot')
            self.c = None


    def set_default(self):
        self.stext.configure(background=self.default_bg)





##---------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


