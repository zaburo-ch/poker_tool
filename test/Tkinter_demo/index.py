#! /usr/bin/env python

"""
A index for the demo scripts for Tkinter.
The widgets produced by these demos are same as those
produced by the Tcl/Tk demos.
"""


import Tkinter as Tk
import tkMessageBox as Tm
from ScrolledText import ScrolledText
import re
import os
import sys

# demo scripts
import label       # label button checkbuttons, and radiobuttons
import unicodeout
import button      # label button checkbuttons, and radiobuttons
import check
import radio
import puzzle
import icon
import image1
import image2
import labelframe
import states      # The 50 states
import colors      # color
import sayings     # sayings
import entry1
import entry2
import entry3
import spin
import form
import text
import style
import bind
import twind
import search
import items
import plot
import ctext
import arrow
import ruler
import cscroll
import floor
import hscale
import vscale
import paned1
import paned2
import menu
import menubutton
import msgbox
import filebox
import clrpick
import bitmap
import dialog1
import dialog2

#########################################
        
class Link:
    def __init__(self, master, text, tag, command):
        master.insert(Tk.END, text + "\n", tag)
        
        self.tag = tag
        self.master = master
        self.command = command
        self.color0 = "#0020FF"
        self.on_leave()
        self.master.tag_bind(tag, "<Double-Button-1>", self.on_clicked)
        self.master.tag_bind(tag, "<Enter>", self.on_enter)
        self.master.tag_bind(tag, "<Leave>", self.on_leave)

    def on_leave(self, *rest):
        self.master.tag_config(self.tag, foreground=self.color0, underline=1)
        
    def on_clicked(self, event):
        self.color0="#006666"
        self.on_leave(event)
        self.command(event)
        
    def on_enter(self, event):
        self.master.tag_config(self.tag, foreground="#FF0099", underline=1)



class Tindex (ScrolledText):
    n_index = 0
    def __init__(self, master):
        ScrolledText.__init__(self, master,  font=("Helvetica", "12"), width=900, cursor="left_ptr", wrap=Tk.WORD)
        
        self.tag_config("title", font=("Helvetica", "22", "bold"))
        self.tag_config("em", font=("Helvetica", "12", "bold"))
        self.tag_config("section", font=("Helvetica", "18", "bold"))

        ## head ---------------------------------------------------------------------------------
        self.insert(Tk.END, "Tkinter Widget Demonstrations\n\n", "title")
        self.insert(Tk.END, "This application provides a front end for several short scripts " 
                             "that demonstrate what you can do with Tk widgets.  " 
                             "Each of the numbered lines below describes a demonstration;  " 
                             "you can click on it to invoke the demonstration.  " 
                             "Once the demonstration window appears, you can click the ")
        self.insert(Tk.END, "See Code", "em")
        self.insert(Tk.END, " button to see the Python/Tk code that created the demonstration.  " 
                              "If you wish, you can edit the code and click the ")
        self.insert(Tk.END, "Rerun Demo", "em")
        self.insert(Tk.END, " button in the code window to reinvoke the demonstration with the modified code.\n"
                             "This demonstration is just a transration of Tcl/Tk demo by "
                             "Sun Microsystems, Inc. (1996-1997), Ajuba Solutions, Inc. (1997-2000), and"
                             "Donal K. Fellows (2001-2002).\n\n")



        ## contents ---------------------------------------------------------------------------
        self.def_section("Labels, buttons, checkbuttons, and radiobuttons ",
                            [(label.demo, "Labels (text and bitmaps)"),
                             (unicodeout.demo, "Labels and UNICODE text"),
                             (button.demo, "Buttons"),
                             (check.demo, "Check-buttons (select any of a group)"),
                             (radio.demo,  "Radio-buttons (select one of a group)"), 
                             (puzzle.demo,  "A 15-puzzle game made out of buttons"), 
                             (icon.demo,  "Iconic buttons that use bitmaps"), 
                             (image1.demo,  "Two labels displaying images"), 
                             (image2.demo,  "A simple user interface for viewing images"), 
                             (labelframe.demo,  "Labelled frames") 
                            ] )
        
        self.def_section("Listboxes", [
                            (states.demo, "The 50 states"),
                            (colors.demo, "Colors: change the color scheme for the application"),
                            (sayings.demo, "A collection of famous and infamous sayings")
                         ])
        
        self.def_section("Entries and Spin-boxes", [
                              (entry1.demo, "Entries without scrollbars"),
                              (entry2.demo, "Entries with scrollbars"),
                              (entry3.demo, "Validated entries and password fields"),
                              (spin.demo, "Spin-boxes"),
                              (form.demo, "Simple Rolodex-like form")
                         ])
                         
        self.def_section("Text", [
                              (text.demo, "Basic editable text"),
                              (style.demo, "Text display styles"),
                              (bind.demo, "Hypertext (tag bindings)"), 
                              (twind.demo, "A text widget with embedded windows"), 
                              (search.demo, "A search tool built with a text widget") 

                         ])
                         
        self.def_section("Canvases", [
                              (items.demo, "The canvas item types"),
                              (plot.demo, "A simple 2-D plot"),
                              (ctext.demo, "Text items in canvases"),
                              (arrow.demo, "An editor for arrowheads on canvas lines"),
                              (ruler.demo, "A ruler with adjustable tab stops"),
                              (floor.demo, "A building floor plan"),
                              (cscroll.demo, "A simple scrollable canvas")
                         ])

        self.def_section("Scales", [
                              (hscale.demo, "Horizontal scale"),
                              (vscale.demo, "Vertical scale")
                          ])
                          
        self.def_section("Paned Windows", [
                              (paned1.demo, "Horizontal paned window"),
                              (paned2.demo, "Vertical paned window")
                          ])

        self.def_section("Menus", [
                              (menu.demo, "Menus and cascades (sub-menus)"),
                              (menubutton.demo, "Menu-buttons")
                          ])

        self.def_section("Common Dialogs", [
                              (msgbox.demo, "Message boxes"),
                              (filebox.demo, "File selection dialog"),
                              (clrpick.demo, "Color picker")
                          ])


        self.def_section("Miscellaneous", [
                              (bitmap.demo, "The built-in bitmaps"),
                              (dialog1.demo, "A dialog box with a local grab"),
                              (dialog2.demo, "A dialog box with a global grab")
                          ])

        self.pack(fill=Tk.BOTH, expand=1)


##---------------------------------------------------------------------------






                          
                            
    def def_section(self, sec_title, ls_discription):
        self.insert(Tk.END, sec_title + "\n", "section")
        for i, (command, discription) in enumerate(ls_discription):
            self.insert(Tk.END, "          ")
            Link(self, "%d. %s." % (i+1, discription), str(self.n_index), command)
            self.n_index += 1
        self.insert(Tk.END, "\n")




class DMenu(Tk.Menu):
    """ menubar for Demo"""


    def __init__(self, master):
        Tk.Menu.__init__(self, master)
        menu = Tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=menu)
        menu.add_command(label="About <F1>", command=self.show_about)
        menu.add_command(label="Exit <Ctrl-Q>", command=self.quit)
        self.bind_all("<F1>", self.show_about)
        self.bind_all("<Control-q>", self.quit)

    def show_about(self, *event):
        Tm.showinfo(title="About", message="Tkinter widget demonstration.\n\nCopyright (c) 2005 SHIDO, Takafumi")

    def quit(self, *event):
        sys.exit()

        
##
class Demo(Tk.Frame):
    """ Frame for demo """
    


    def __init__(self, master=None):
        Tk.Frame.__init__(self, master, height=600, width=600)
        self.master.title("Tkinter Widget Demonstrations")
        self.pack(padx=0,pady=0,fill=Tk.BOTH, expand=1)   # options should be specified
        self.pack_propagate(0)

        self.menubar = DMenu(self)
        try:
            self.master.config(menu=self.menubar) # this required to show the menu bar
        except AttributeError:
            self.master.Tk.call(master, "config", "-menu", self.menubar)

        Tindex(self)
#########################################
#         self.sbar = Tk.Scrollbar (self, orient=Tk.VERTICAL)
#         self.sbar.pack(side=Tk.RIGHT, fill=Tk.Y,expand=1 )
#         self.text_index = Tindex(self, self.sbar.set)
#         self.text_index.pack(padx=0,pady=0,fill=Tk.BOTH, expand=1 )
#         self.sbar.config(command=self.text_index.yview)
#########################################
        

    



##---------------- The main loop -------------------------------------------

if __name__ == '__main__':
        
    demo = Demo()
    demo.mainloop()
    