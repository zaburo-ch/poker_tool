#! /usr/bin/env python

"""
This is a template for demo codes of Tkinter.
"""

import sys
import string
import Tkinter as Tk
from ScrolledText import ScrolledText

## functions -------------------------------------

def read_contents(fname):
    """ read contens of `fname' """
    f = file(fname)
    str = f.read()
    f.close()
    return str


def newlist(n):
    ls = []
    for i in range(n):
        ls.append(None)
    return ls

def i_range(val, min, max):
    if(min and val < min):
        return(min)
    elif(max and val > max):
        return(max)
    else:
        return(val)

def bottom_slide(str, dx):
    ls0 = str.split('+')
    ls1 = ls0[0].split('x')
    return ('+%d+%d' % (int(ls0[1]) + dx, int(ls1[1]) + int(ls0[2]) + 50))


def left_slide(str):  
    ls0 = str.split('+')
    ls1 = ls0[0].split('x')
    return ('500x600+%d+%s' % (int(ls1[0]) + int(ls0[1]) + 50, ls0[2]))


def str_same_p(str0, str1):
    ls0=string.split(str0)
    ls1=string.split(str1)
    for s0, s1 in zip(ls0, ls1):
        if s0!=s1:
            return False
    else:
        return True


## classes ----------------------------------------



class ShowVars:
    """ a function class to show variables' value in a separated window """
    
    def __init__(self, demo_window, dx, *vars):
        self.demo_window = demo_window
        self.vars = vars
        self.toplevel = None
        self.dx = dx

    def __call__(self, *av):
        if self.toplevel:
            self.toplevel.focus_set()
        else:
            self.toplevel=Tk.Toplevel(self.demo_window)
            self.toplevel.title('Variable values')
            self.toplevel.geometry(bottom_slide( self.demo_window.winfo_geometry(), self.dx))
            frame = Tk.Frame(self.toplevel)
            frame.pack(fill=Tk.BOTH, expand=1)
            l0 = Tk.Label(frame, text='Variable values: ', font=('Helvetica', '14'))
            l0.pack(padx=10, pady=10)
            f= Tk.Frame(frame)
            for i, (label, var) in enumerate(self.vars):
                l1 = Tk.Label(f, text=label, justify=Tk.LEFT, anchor=Tk.W, width=15)
                l1.grid(row=i, column=0, sticky=Tk.W)
                l2 = Tk.Label(f, textvariable=var, justify=Tk.LEFT, anchor=Tk.W, width=20)
                l2.grid(row=i, column=1, sticky=Tk.W)
            f.pack(fill=Tk.BOTH, anchor=Tk.W, padx=20, pady=20)
            b=Tk.Button(frame, text='OK', command=self.destroy_window)
            b.pack(side=Tk.BOTTOM, padx=10, pady=10)
#            self.demo_window.focus_set()

    def destroy_window(self):
        if self.toplevel:
            self.toplevel.destroy()
            self.toplevel= None



class ButtonFrame(Tk.Frame):
    """ This is a Frame of two common buttons; dismess and (see code or return demo) """

    def __init__(self, master, b0_text, b0_command,  b1_text,  b1_command):
        Tk.Frame.__init__(self, master, height=35)
        b0 = Tk.Button(self, text=b0_text, width=10, command=b0_command)
        b1 = Tk.Button(self, text=b1_text, width=10, command=b1_command)
        b0.pack(side=Tk.LEFT,  padx=30, pady=5)
        b1.pack(side=Tk.LEFT,  padx=30, pady=5)



class Label(Tk.Label):
    """ a label class for the demo """
    
    def __init__(self, master, **key):   #justify=Tk.LEFT, font=("Helvetica", "12")
        key['justify'] = Tk.LEFT
        key['font'] = ("Helvetica", "12")
        Tk.Label.__init__(self, master, **key)
        self.pack(fill=Tk.X, padx=5, pady=5)



class Demo:
    """  A class defining demo window and source code window. """

    demo_window = None
    demo_main_frame = None
    demo_label = None
    demo_frame = None
    code_window = None
    
    def __init__(self, cmain, fname):
        self.fname = fname.split('.').pop(0) + '.py'
        self.cmain = cmain
        if cmain:
            self.demo_main_frame=Tk.Frame()
        else:
            self.demo_window = Tk.Toplevel()
            self.demo_main_frame=Tk.Frame(self.demo_window)

        self.ini_demo()


    def ini_demo(self):
        self.demo_frame = Tk.Frame(self.demo_main_frame)
        self.demo_buttons = ButtonFrame(self.demo_frame, "Dismiss", self.demo_destroy, "Show Code", self.show_code)
        self.demo_main_frame.pack(fill=Tk.BOTH, expand=1, padx=3, pady=3)
        self.demo_frame.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)
        self.demo_buttons.pack(side=Tk.BOTTOM, expand=0, pady=5)


    def ini_demo_called_0(self):
        self.demo_window = Tk.Toplevel()
        self.demo_main_frame=Tk.Frame(self.demo_window)
        self.ini_demo()



    def ini_demo_called(self):
        pass



    def show_code(self):
        if not self.code_window:
            self.code_window = Tk.Toplevel()
            self.code_window.geometry(left_slide(self.demo_main_frame.master.winfo_geometry()))
            self.code_window.title(self.fname)
            self.code_frame = Tk.Frame(self.code_window)
            self.code_frame.pack(fill=Tk.BOTH, expand=1)
            self.scrolled_text = ScrolledText(self.code_frame, wrap=Tk.WORD)
            self.scrolled_text.pack(fill=Tk.BOTH, expand=1)
            self.content0 = read_contents(self.fname)
            self.scrolled_text.insert(Tk.END, self.content0)
            self.code_buttons = ButtonFrame(self.code_frame, "Dismiss", self.code_destroy, "Return Demo", self.return_demo)
            self.code_buttons.pack()
        self.code_window.focus_set()

    def code_destroy(self):
        self.code_window.destroy()
        self.code_window = None

    def demo_destroy(self):
        if self.cmain:
            sys.exit()
        else:
            self.demo_window.destroy()
            self.demo_window = None

    def return_demo(self):
        if self.cmain:
            self.demo_main_frame.focus_set()
        else:
            content = self.scrolled_text.get('1.0', Tk.END)
            if str_same_p(self.content0, content):
                if self.demo_window:
                    self.demo_window.focus_set()
                else:
                    self.ini_demo_called()
            else:
                if self.demo_window:
                    self.demo_window.destroy()
                f=file('temp.py', 'w')
                f.write(content)
                f.close()
                mod = __import__('temp')
                reload(mod)
                self.code_window.destroy()
                d = mod.Demo(False)
                d.demo_window.focus_set()
                d.demo_window.master.after(20, d.show_code)
            

##----------------------------------------------------
if __name__ == '__main__':
    class De (Demo):
        def __init__(self):
            Demo.__init__(self, True, __file__)
            Label(self.demo_frame, text="test test test")
            
    a = De()
    a.demo_main_frame.mainloop()

