#! /usr/bin/env python

"""
msgbox.py

This demonstration script creates message boxes of various type

June 17, 2005
"""

import Tkinter as Tk
import tkMessageBox as Mb
import template as A

class Radiobuttons(Tk.Frame):
    def __init__(self, master, title, var, values):
        self.var = var
        Tk.Frame.__init__(self, master)
        label = Tk.Label(self, text=title)
        label.pack()
        sep = Tk.Frame(self, width=120, relief=Tk.RIDGE, bd=1, height=2)
        sep.pack()
        for obj in values:
            r = Tk.Radiobutton(self, text=obj, variable=self.var, value=obj, justify=Tk.LEFT)
            r.pack(anchor=Tk.W)


class Demo(A.Demo):
    """
     a demo for simple labels
    """
    def __init__(self, cmain):                              #cmain = __name== '__main__'
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_frame(self):
        self.demo_main_frame.master.title("Message Box Demonstration")
        self.demo_main_frame.master.geometry("+50+50")
        A.Label(self.demo_main_frame, text=
        "Choose the icon and type option of the message box. "
        "Then press the \"Message Box\" button to see the message box."
        , width=45, wraplength='9c')

        f0 = Tk.Frame(self.demo_frame)
        f0.pack(padx=20, pady=20)

        # select icon
        self.icon = Tk.StringVar()
        f1 = Radiobuttons(f0, 'Icon', self.icon,  ('error', 'info', 'question', 'warning'))
        f1.pack(side=Tk.LEFT, padx=40, anchor=Tk.N)
            

        # select type
        self.type = Tk.StringVar()
        f2 = Radiobuttons(f0, 'Type', self.type,
                                    ('abortretryignore', 'ok', 'okcancel', 'retrycancel', 'yesno', 'yesnocancel'))
        f2.pack(side=Tk.RIGHT, padx=40, anchor=Tk.N)

        # add 'Message Box' button
        b3 = Tk.Button(self.demo_buttons, text='Message Box', command=self.show_msg)
        b3.pack(side=Tk.RIGHT, padx=25)




    def show_msg(self):
        answer =  Mb._show(
                  title = "Message",
                  message = "This is a \'%s\' type messagebox with the \'%s\' icon." % (self.type.get(),self.icon.get()),
                  icon = self.icon.get(),
                  type = self.type.get())

        Mb.showinfo(title='Choise', message="You have selected \'%s\'." % (answer))
        self.demo_main_frame.master.focus_set()

##--------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


