#! /usr/bin/env python

import Tkinter as Tk

CLOCK = 'meza-bl-2.gif'

class Frame(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.img = Tk.PhotoImage(file=CLOCK)
        il = Tk.Label(self, image=self.img)
        il.pack()


if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()

