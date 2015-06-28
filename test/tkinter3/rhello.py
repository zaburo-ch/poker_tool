#! /usr/bin/env python

import Tkinter as Tk
import random as R


class Label(Tk.Label):
    def __init__(self, master=None):
        Tk.Label.__init__(self, master, text='Hello world!', font=('Helvetica', '24', 'bold'))
        self.bind_all('<1>', self.bg_change)

    def bg_change(self, event):
        r = R.randint(0,255)
        g = R.randint(0,255)
        b = R.randint(0,255)
        self.configure(bg='#%02X%02X%02X' % (r, g, b))

if __name__ == '__main__':
    l = Label()
    l.pack()
    l.mainloop()

