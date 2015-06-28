#! /usr/bin/env python

"""
image2.py

This demonstration script creates a simple collection of widgets
that allow you to select and view images in a Tk label.

June 15, 2005
"""

import re
import os
import os.path
import Tkinter as Tk
import tkFileDialog as D
import template as A


class DirectoryBrowser(Tk.LabelFrame):
    def __init__(self, master, i_viewer):
        Tk.LabelFrame.__init__(self, master, text='Directory:')
        self.i_viewer = i_viewer
        self.entry = Tk.Entry(self, width=45)
        button = Tk.Button(self, width=11, text='Select Dir.', command=self.browse)
        self.entry.pack(side=Tk.LEFT, fill=Tk.X, expand=1, padx=5, pady=5)
        button.pack(side=Tk.RIGHT, padx=5, pady=5)
        dir0 = os.getcwd()
        self.entry.insert(0, dir0)
        self.i_viewer.update(dir0)

        self.entry.bind('<Return>', self.send_dir)

    def browse(self):
        dir = D.askdirectory()
        if dir:
            self.entry.delete(0, Tk.END)
            self.entry.insert(0, dir)
            self.i_viewer.update(dir)

    def send_dir(self, event):
        self.i_viewer.update(os.path.normpath(self.entry.get()))


            
class ImageViewer(Tk.Frame):
    wild_card = re.compile('\.(gif|ppm)$')
    
    def __init__(self, master):
        Tk.Frame.__init__(self, master)

        lframe_1 = Tk.LabelFrame(self, text='File: ')
        scroll = Tk.Scrollbar (lframe_1, orient=Tk.VERTICAL)
        scroll.pack(side=Tk.RIGHT, fill=Tk.Y, padx=5, pady=5)
        self.lbox= Tk.Listbox(lframe_1,  yscrollcommand=scroll.set)
        self.lbox.pack(side=Tk.LEFT, fill=Tk.Y, padx=5, pady=5)
        scroll.config(command=self.lbox.yview)
        lframe_1.grid(row=0, column=0, sticky=Tk.NW + Tk.SW, padx=5, pady=5)

        lframe_2 = Tk.LabelFrame(self, text='Image: ')
        self.ilabel = Tk.Label(lframe_2)
        lframe_2.grid(row=0, column=1, sticky=Tk.NW, padx=5, pady=5)
        self.ilabel.pack()
        self.lbox.bind('<Double-Button-1>', self.show_image)


    def show_image(self, event):
        tup = self.lbox.curselection()
        if tup:
            self.image = Tk.PhotoImage(file=self.lbox.get(tup[0]))
            self.ilabel.configure(image= self.image)

    def update(self, dir):
        self.lbox.delete(0, Tk.END)
        [self.lbox.insert(Tk.END, f) for f in os.listdir(dir) if self.wild_card.search(f)]




class Demo(A.Demo):
    """ a simple image loader """


    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("Image Demonstration #2")
        self.demo_main_frame.master.geometry('+50+50')
        
        A.Label(self.demo_main_frame, text=
        "This demonstration allows you to view images using a Tk \"photo\" image.  " 
        "First type a directory name in the listbox, then type Return to load the directory into the listbox.  " 
        "Then double-click on a file name in the listbox to see that image."
        , width=40, wraplength='8.5c')

        iv = ImageViewer(self.demo_frame)
        db = DirectoryBrowser(self.demo_frame, iv)

        db.pack(fill=Tk.X, expand=1, padx=5, pady=5)
        iv.pack(side=Tk.LEFT, padx=5, pady=5)



def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()
