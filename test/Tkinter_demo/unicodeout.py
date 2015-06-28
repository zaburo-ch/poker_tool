#! /usr/bin/env python

"""
unicodeout.py

This demonstration script shows how you can produce output (in label
widgets) using many different alphabets.

June 16, 2005
"""

import Tkinter as Tk
import template as A

class Demo(A.Demo):
    """ demo for unicode labels """

    
    def __init__(self, cmain):                              #cmain = __name== '__main__'
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_frame(self):
        self.demo_main_frame.master.title("Unicode Label Demonstration")
        
        A.Label(self.demo_main_frame, text=
        "This is a sample of Tk's support for languages that use " 
        "non-Western character sets.  However, what you will actually see " 
        "below depends largely on what character sets you have installed, " 
        "and what you see for characters that are not present varies greatly " 
        "between platforms as well.  The strings are written in Tcl using " 
        "UNICODE characters using the \\uXXXX escape so as to do so in a " 
        "portable fashion."
        , width=40, wraplength='8.5c')


        self.ulabel('Arabic',
                    u"\uFE94\uFEF4\uFE91\uFEAE\uFECC\uFEDF\uFE8D\uFE94",
	            u"\uFEE4\uFEE0\uFEDC\uFEDF\uFE8D")
                        
        self.ulabel("Trad. Chinese",
                    u"\u4E2D\u570B\u7684\u6F22\u5B57")
                       
        self.ulabel("Simpl. Chinese", u"\u6C49\u8BED")
        
        self.ulabel('Greek', 
                    u"\u0395\u03BB\u03BB\u03B7\u03BD\u03B9\u03BA\u03AE " ,
                    u"\u03B3\u03BB\u03CE\u03C3\u03C3\u03B1")
                       
        self.ulabel('Hebrew',
	            u"\u05DD\u05D9\u05DC\u05E9\u05D5\u05E8\u05D9 ",
	            u"\u05DC\u05D9\u05D0\u05E8\u05E9\u05D9")
                       
        self.ulabel('Japanese', 
	            u"\u65E5\u672C\u8A9E\u306E\u3072\u3089\u304C\u306A, " ,
	            u"\u6F22\u5B57\u3068\u30AB\u30BF\u30AB\u30CA")
                        
        self.ulabel('Korean', u"\uB300\uD55C\uBBFC\uAD6D\uC758 \uD55C\uAE00")
        
        self.ulabel('Russian', u"\u0420\u0443\u0441\u0441\u043A\u0438\u0439 \u044F\u0437\u044B\u043A")


        
    def ulabel(self, lang, *rest):
        lang += ':'
        sample = ' '.join(rest)
        label = Tk.Label(self.demo_frame, font=('Helvetica', '12'), text= '%-15s\t%s' % (lang, sample), anchor=Tk.W, pady=0)
        label.pack(fill=Tk.X, expand=1, padx=10, pady=3)


##-----------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


