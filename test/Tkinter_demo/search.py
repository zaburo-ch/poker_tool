#! /usr/bin/env python

"""
search.py

This demonstration script creates a collection of widgets that
allow you to load a file into a text widget, then perform searches
on that file.

June 20, 2005
"""

import string
import os.path
import Tkinter as Tk
import template as A
from ScrolledText import ScrolledText
from tkMessageBox import showwarning


# function -----------------------------------------------------------

def index_end(idx, i):
    ls = string.split(idx, '.')
    return ('%s.%d' % (ls[0], int(ls[1]) + i))



#-----------------------------------------------------------------------------------
class LEB(Tk.Frame):   # Label, Entry, Button
    def __init__(self, frame, label_text, button_text, command):

        self.frame = frame
        self.command = command # one arguemnt function
        Tk.Frame.__init__(self, frame)
        self.pack(padx=10, pady=5, fill=Tk.X)
        self.label = Tk.Label(self, text=label_text, width=13, anchor=Tk.W, justify=Tk.LEFT)
        self.label.pack(side=Tk.LEFT, anchor=Tk.W)
        self.entry = Tk.Entry(self, width = 40)
        self.entry.pack(side=Tk.LEFT, padx=10)
        self.entry.bind('<Return>', self.entry_command)
        self.button = Tk.Button(self, text=button_text, command=self.button_command, width=10)
        self.button.pack(side=Tk.LEFT)

    def entry_command(self, event):
        self.command(self.entry.get())

    def button_command(self):
        self.command(self.entry.get())




class Demo(A.Demo):
    """  searching """


    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("Search string:")
        self.demo_main_frame.master.geometry('+50+50')


        leb1 = LEB(self.demo_frame, 'File name:', 'Load File', self.load_file)
        leb2 = LEB(self.demo_frame,  'Search string:', 'Highlight', self.search_string)
        self.scrolled_text= ScrolledText(self.demo_frame, wrap=Tk.WORD,  width=60, height=30)
        self.scrolled_text.pack(fill=Tk.BOTH, expand=1)
        self.scrolled_text.insert(Tk.END,
          "This window demonstrates how to use the tagging facilities in text widgets to implement a searching mechanism.  "
          "First, type a file name in the top entry, then type <Return> or click on \"Load File\".  "
          "Then type a string in the lower entry and type <Return> or click on \"Highlight\".  "
          "This will cause all of the instances of the string to be tagged with the tag \"search\", "
          "and it will arrange for the tag's display attributes to change to make all of the strings blink.")

        self.fg='black'
        self.bg='white'
        
        self.highlight()              # blink the found.
        
    def load_file(self, fname):
        if not fname:
            showwarning('Warning', 'give file name') and \
            self.demo_main_frame.master.focus_set()
        elif(not os.path.exists(fname)):
            showwarning('Warning', 'no such file') and \
            self.demo_main_frame.master.focus_set()
        else:
            f = file(fname)
            self.scrolled_text.delete('1.0', Tk.END)
            self.scrolled_text.insert(Tk.END, f.read())
            f.close()


    def search_string(self, target):
        if not target:
            showwarning('Warning', 'empty string') and \
            self.demo_main_frame.master.focus_set()
        else:
            self.scrolled_text.tag_delete('found')
            idx0 ='1.0'
            slen = len(target)
            while True:
                idx = self.scrolled_text.search(target, idx0, stopindex=Tk.END)
                if not idx:
                    break
                idx0 = index_end(idx, slen)
                self.scrolled_text.tag_add('found', idx, idx0)

        
    def highlight(self):
        self.fg = self.fg == 'black' and 'white' or 'black'
        self.bg = self.bg == 'white' and '#ce5555' or 'white'
        self.scrolled_text.tag_config('found', foreground=self.fg, background=self.bg)
        self.scrolled_text.after(500, self.highlight)

            
##---------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()

