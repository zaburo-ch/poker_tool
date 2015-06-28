#! /usr/bin/env python

"""
radio.py

This demonstration script creates a toplevel window containing
several radiobutton widgets.

June 15, 2005
"""


import Tkinter as Tk
import template as A
import Dialog as D

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
        self.demo_main_frame.master.title("A dialog box with a global grab")
        self.demo_main_frame.master.geometry('+50+50')
        self.echo=Tk.StringVar()
        label = Tk.Label(self.demo_frame, textvariable=self.echo, font=('Helvetica', '12'))
        label.pack(anchor=Tk.CENTER)


        self.dialog = D.Dialog(None, {'title':'Dialog with global grab',
                         'text':
                             "This dialog box uses a global grab, "
                             "so it prevents you from interacting with anything "
                             "on your display until you invoke one of the buttons below.  "
                             "Global grabs are almost always a bad idea; "
                             "don't use them unless you're truly desperate.",
                         'bitmap':'warning',
                         'default':0,
                         'strings':('OK', 'Cancel', 'Show Code')})

        self.demo_main_frame.master.after(100, self.dialog.grab_set_global)

                         
        if(self.dialog.num==0):
            self.echo.set('You pressed OK.')
            self.demo_main_frame.master.after(1000, self.demo_main_frame.master.destroy)
        elif(self.dialog.num==1):
            self.echo.set('You pressed Cancel.')
            self.demo_main_frame.master.after(1000, self.demo_main_frame.master.destroy)
        elif(self.dialog.num==2):
            self.show_code()


##----------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()
