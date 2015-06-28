#! /usr/bin/env python

import Tkinter as Tk
from PIL import Image, ImageTk

CLOCK = 'meza-bl-2.png'

class Frame(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        image = Image.open(CLOCK)
        self.img = ImageTk.PhotoImage(image)


        il = Tk.Label(self, image=self.img)
        il.pack()


if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()

