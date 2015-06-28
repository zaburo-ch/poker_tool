#! /usr/bin/env python

"""
menu.py

This demonstration script creates a window with a bunch of menus
and cascaded menus using menubars.

June 21, 2005
"""


import Tkinter as Tk
import template as A
from tkMessageBox import showinfo, showerror



SEPARATOR = 0


##-------------------------------------------------
class Info:
    def __init__(self, title, description, demo_window):
        self.title = title
        self.description = description
        self.demo_window = demo_window

    def __call__(self, *av):
        showinfo(self.title, self.description)
        self.demo_window.focus_set()


        
class Error:
    def __init__(self, str, demo_window):
        self.description = "this is just a demo: no action has been defined for the \"%s\" entry" % (str)
        self.demo_window = demo_window

    def __call__(self, *av):
        showerror('This is a demo', self.description)
        self.demo_window.focus_set()


        
class Echo:
    def __init__(self, var, str):
        self.var = var
        self.str = str
        
    def __call__(self, *av):
        self.var.set(self.str)




##------------------------------------------------------
class Demo(A.Demo):
    """a demo class """


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
                                    font=('Helvetica', '10'), anchor=Tk.W, width=60)
        self.echo_label.pack(side=Tk.LEFT)
        self.statusbar.pack(side=Tk.BOTTOM)
        #----
        self.demo_frame = Tk.Frame(self.demo_main_frame, relief=Tk.RIDGE, bd=2)
        self.demo_buttons = A.ButtonFrame(self.demo_frame, "Dismiss", self.demo_destroy, "Show Code", self.show_code)
        self.demo_main_frame.pack(fill=Tk.BOTH, expand=1, padx=3, pady=3)
        self.demo_frame.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)
        self.demo_buttons.pack(side=Tk.BOTTOM, expand=0, pady=5)



    def ini_frame(self):
        self.demo_main_frame.master.title("Menu Demonstration")
        self.demo_main_frame.master.geometry('+50+50')

        ## menu bar
        self.menu_bar = Tk.Menu(self.demo_main_frame, tearoff=0)

        ## File
        self.menu_file = Tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.menu_file,  underline=0)
        for obj in ["Open...", "New", "Save", "Save As...", SEPARATOR, "Print Setup...", "Print...", SEPARATOR]:
            if obj == SEPARATOR:
                self.menu_file.add_separator()
            else:
                self.menu_file.add_command(label= obj, command=Error(obj, self.demo_main_frame.master))
        self.menu_file.add_command(label="Dismiss Menus Demo", command=self.demo_main_frame.master.destroy)

        ## Basic
        self.menu_basic = Tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Basic", menu=self.menu_basic,  underline=0, state=Tk.NORMAL)
        self.menu_basic.add_command(label='Long entry that does nothing')
        for item in ['A', 'B', 'C', 'D', 'E', 'F']:
            self.menu_basic.add_command(label='Print letter \'' + item + '\'', underline=14,
                                    accelerator = item, command=Echo(self.echo, item))
            self.demo_main_frame.master.bind('<KeyPress-' + item.lower() + '>', Echo(self.echo, item))

        ## cascade
        self.menu_cascade = Tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Cascades", menu=self.menu_cascade,  underline=0)
        self.menu_cascade.add_command(label='Print hello', command=Echo(self.echo, 'Print hello'),
        accelerator='H', underline=0)
        self.demo_main_frame.master.bind('<KeyPress-h>', Echo(self.echo, 'Print hello'))
        self.menu_cascade.add_command(label='Print goodbye', command=Echo(self.echo, 'Print goodbye'),
        accelerator='G', underline=0)
        self.demo_main_frame.master.bind('<KeyPress-g>', Echo(self.echo, 'Print goodbye'))

        ## check buttons
        self.menu_check_buttons = Tk.Menu(self.menu_bar, tearoff=0)
        self.menu_cascade.add_cascade(label='Check buttons', menu=self.menu_check_buttons, underline=0)
        self.oil = Tk.IntVar()
        self.trans = Tk.IntVar()
        self.brakes = Tk.IntVar()
        self.lights = Tk.IntVar()
        
        for label, var in [('Oil checked', self.oil), ('Transmission checked', self.trans),
                           ('Brakes checked', self.brakes), ('Lights checked', self.lights)]:
            self.menu_check_buttons.add_checkbutton(label=label, variable=var)
        self.menu_check_buttons.add_separator()
        self.menu_check_buttons.add_command(label='Show current value',
                  command= A.ShowVars(self.demo_main_frame.master, 0,
                                    ('Oil: ', str(self.oil)), ('Transmission: ', str(self.trans)),
                                    ('Brakes: ', str(self.brakes)), ('Lights: ', str(self.lights))))
        self.menu_check_buttons.invoke(1)
        self.menu_check_buttons.invoke(3)


        ## radio buttons
        self.menu_radio_buttons = Tk.Menu(self.menu_bar, tearoff=0)
        self.menu_cascade.add_cascade(label='Radio buttons', menu=self.menu_radio_buttons, underline=0)
        self.point_size = Tk.IntVar()
        self.style = Tk.StringVar()

        for p in [10, 14, 18, 24, 32]:
            self.menu_radio_buttons.add_radiobutton(label='%d point' % (p),  variable = self.point_size, value=p)
        self.menu_radio_buttons.add_separator()
        for s in ['Roman', 'Bold', 'Italic']:
            self.menu_radio_buttons.add_radiobutton(label=s,  variable = self.style, value=s.lower())
        self.menu_radio_buttons.add_separator()
        self.menu_radio_buttons.add_command(label='Show current value',
                                            command=A.ShowVars(self.demo_main_frame.master, 300,
                                                 ('Point: ', str(self.point_size)), ('Style: ', self.style)))
        self.menu_radio_buttons.invoke(1)
        self.menu_radio_buttons.invoke(7)


        ## icon
        self.menu_icon=Tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Icons', menu=self.menu_icon, underline=0)
        self.menu_icon.add_command(bitmap='@pattern.bmp', hidemargin=1,
                             command=Info("About", 
                                          "The menu entry you invoked displays a bitmap rather than "
                                          "a text string.  Other than this, it is just like any other "
                                          "menu entry.", self.demo_main_frame.master))
        for item in ['info', 'questhead', 'error']:
            self.menu_icon.add_command(bitmap=item, hidemargin=1,
                                     command=Echo(self.echo, 'You invoked the %s bitmap' % (item)))
        self.menu_icon.entryconfigure(2, columnbreak=1)


        ## more
        self.menu_more=Tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='More', menu=self.menu_more, underline=0)
        self.menu_more.add_command(label='Enable below', command=self.enable_below)
        for item in ["An entry", "Another entry", "Does nothing", "Does almost nothing", "Make life meaningful"]:
            self.menu_more.add_command(label=item, state= Tk.DISABLED,
                                          command=Echo(self.echo, 'You invoked \"%s\"' % (item)))

        self.menu_more.add_command(label="Does almost nothing", bitmap='questhead',
                                    compound=Tk.LEFT, state= Tk.DISABLED,
                                    command=Info("Compound Menu Entry",
                                    "The menu entry you invoked displays both a bitmap and a "
                                    "text string.  Other than this, it is just like any other "
                                    "menu entry.", self.demo_main_frame.master))


        ## color
        self.menu_colors=Tk.Menu(self.menu_bar, tearoff=1)
        self.menu_bar.add_cascade(label='Colors', menu=self.menu_colors, underline=1)
        for item in ['red', 'orange', 'yellow', 'green', 'blue']:
            self.menu_colors.add_command(label=item, background=item,
                      command=Echo(self.echo, 'You invoked \"%s\"' % (item)))

        ## place the menu bar at the top of the window
        try:
            self.demo_main_frame.master.config(menu=self.menu_bar)     # this required to show the menu bar
        except AttributeError:
            self.demo_main_frame.master.Tk.call(master, "config", "-menu", self.menu_bar)


        ## description
        A.Label(self.demo_frame, text=
        "This window contains a menubar with cascaded menus.  "
        "You can post a menu from the keyboard by typing Alt+x, where \"x\" is the character underlined on the menu.  "
        "You can then traverse among the menus using the arrow keys.  "
        "When a menu is posted, you can invoke the current entry by typing Return,"
        "or you can invoke any entry by typing its underlined character.  "
        "If a menu entry has an accelerator, "
        "you can invoke the entry without posting the menu just by typing the accelerator. "
        "The rightmost menu can be torn off into a palette by selecting the first item in the menu."
        , width=50, wraplength='11.5c')



##-----------
    def enable_below(self):
        for i in range(1, 7):
            self.menu_more.entryconfigure(i, state=Tk.NORMAL)
        self.menu_more.entryconfigure(0, label='disable below', command=self.disable_below)

    def disable_below(self):
        for i in range(1, 7):
            self.menu_more.entryconfigure(i, state=Tk.DISABLED)
        self.menu_more.entryconfigure(0, label='enable below', command=self.enable_below)



##---------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()

    