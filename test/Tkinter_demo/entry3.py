#! /usr/bin/env python

"""
entry3.py

This demonstration script creates several entry widgets whose
permitted input is constrained in some way.  It also shows off a
password entry.

.after method can be used as a timer
see tkinter refertence: a GUI for Python by Jhon W. Shipman, p.61

June 14, 2005
"""


import Tkinter as Tk
import template as A
import re
import sys


class Entry_with_LabelFrame(Tk.LabelFrame):
    def __init__(self, master, title):
        Tk.LabelFrame.__init__(self, master, text=title)
        self.entry = Tk.Entry(self, width=25)
        self.entry.pack(padx=3, pady=2)



class Demo(A.Demo):
    """ a demo for entry box with check. """


    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()

    def ini_frame(self):
        p = re.compile(r"^\d-\(\d{3}\)-\d{3}-\d{4}$")
        self.str_before=""

        self.demo_main_frame.master.title("Constrained Entry Demonstration")
        self.demo_main_frame.master.geometry("+50+50")        
        A.Label(self.demo_main_frame, text=
        "Four different entries are displayed below.  " 
        "You can add characters by pointing, clicking and typing, " 
        "though each is constrained in what it will accept.  " 
        "The first only accepts integers or the empty string (checking when focus leaves it) " 
        "and will flash to indicate any problem.  " 
        "The second only accepts strings with fewer than ten characters " 
        "and sounds the bell when an attempt to go over the limit is made.  " 
        "The third accepts US phone numbers, mapping letters to their digit equivalent " 
        "and sounding the bell on encountering an illegal character or " 
        "if trying to type over a character that is not a digit.  " 
        "The fourth is a password field that accepts up to eight characters (silently ignoring further ones), " 
        "and displaying them as asterisk characters."
        ,width=45,  wraplength='10c')

        eframe = Tk.Frame(self.demo_frame)
        eframe.pack()
        self.fe1 = Entry_with_LabelFrame(eframe, "Integer Entry")
        self.fe2 = Entry_with_LabelFrame(eframe, "Length-Constrained Entry")
        self.fe3 = Entry_with_LabelFrame(eframe, "US Phone-Number Entry")
        self.fe4 = Entry_with_LabelFrame(eframe, "Password Entry")

        self.fe1.grid(row=0, column=0, padx=8, pady=5)
        self.fe2.grid(row=0, column=1, padx=8, pady=5)
        self.fe3.grid(row=1, column=0, padx=8, pady=5)
        self.fe4.grid(row=1, column=1, padx=8, pady=5)
        
        self.flash=False
        self.fe1.entry.bind("<FocusOut>", self.check_integer)
        self.fe1.entry.bind("<FocusIn>", self.quiet)

        self.fe2.entry.bind("<Any-KeyRelease>", self.check_length)

        self.fe3.entry.insert(Tk.END, "1-(000)-000-0000")
        self.fe3.entry.bind("<Any-KeyRelease>", self.check_phone_number)
        self.fe3.entry.bind("<Any-KeyPress>", self.clear_selection)

        self.fe4.entry.config(show='*')

    def check_integer(self, event):
        str = self.fe1.entry.get().strip()
        if (str and (not (str.isdigit() or (str[0] == '-' and str[1:].isdigit())))) :
            self.bgcolor = "red"
            self.flash=True
            self.fe1.entry.bell()
            self.flash_bg()

    def flash_bg(self):
        self.fe1.entry.config(bg=self.bgcolor)
        self.bgcolor = (self.bgcolor == "red") and "yellow" or "red"
        if self.flash:
            self.fe1.entry.after(400, self.flash_bg)
        else:
            self.fe1.entry.config(bg="white")
            
    def quiet(self, event):
        self.flash=False
        
    def check_length(self, event):
        slen = self.fe2.entry.index(Tk.END)
        if slen > 10:
            self.fe2.entry.delete(slen-1)
            self.fe2.entry.bell()
                
    def check_phone_number(self, event):    #     "1-(000)-000-0000"
        if(self.str_before):
            self.fe3.entry.delete(0, Tk.END)
            self.fe3.entry.insert(0, self.str_before)
            self.str_before=""
        else:
            c = event.char
            sn = event.keysym_num
            str0 = self.fe3.entry.get()
            idx = self.fe3.entry.index(Tk.INSERT)
            if idx > 15:
                self.fe3.entry.bell()
                self.fe3.entry.delete(16)
            elif c:                                   # if the key input is ascii
                c0 = str0[idx]
                if(c0==c or (c0.isdigit() and c.isdigit())):
                    self.fe3.entry.delete(idx)
                else:
                    self.fe3.entry.delete(idx-1)
                    self.fe3.entry.bell()
            elif(sn in (65288, 65535)):                    # backspace, or delete
                idx=self.fe3.entry.index(Tk.INSERT)
            
                if (idx in (1,7,11)):
                    c_add = '-'
                elif(idx==2):
                    c_add =  '('
                elif(idx==6):
                    c_add = ')'
                elif(idx==0):
                    c_add = '1'
                else:
                    c_add = '0'
                    
                self.fe3.entry.insert(Tk.INSERT, c_add)

    def clear_selection(self, event):
        if (self.fe3.entry.select_present()):
            self.fe3.entry.select_clear()
            self.str_before = self.fe3.entry.get()

            
##---------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()

