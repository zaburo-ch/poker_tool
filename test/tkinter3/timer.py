#! /usr/bin/env python

"""
timer.py

June 24, 2005
"""


import Tkinter as Tk
import sys

BLUE = '#99CCFF'
YELLOW = '#FFCC00'
RED = '#FF00FF'
CLOCK = 'meza-bl-2.gif'

class Frame(Tk.Frame):

    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.started = False
        self.echo = Tk.StringVar()
        self.min = len(sys.argv) > 1 and  int(sys.argv[1]) or 3
        self.echo.set('%02d:00' % (self.min))
        self.sec = 60 * self.min

        self.master.title('Alarm')
        self.label = Tk.Label(self, text='Click to start', font=('Helvetica', '8'))
        self.label.pack()
        f = Tk.Frame(self, relief=Tk.RIDGE, bd=4)
        f.pack(fill=Tk.BOTH, expand=1)
        self.image= Tk.PhotoImage(file=CLOCK)
        self.icon=Tk.Label(f, image=self.image, bg=BLUE)
        self.icon.pack(side=Tk.LEFT)
        display = Tk.Label(f, textvariable=self.echo, font=('Helvetica', '24'),
                           bg='white', width=5, anchor=Tk.E)
        display.pack(side=Tk.LEFT)
        self.bind_all('<1>', self.start_stop)
        self.bind_all('<3>', self.reset)

        # if you mind a buggy behaviour on double click, add the following code
        self.bind_all('<Double-Button-1>', lambda event:False)



    def start_stop(self, event):
        if not self.started:
            self.label.configure(text='Click to stop')
            if 0< self.sec <= 20:
               self.icon.configure(bg=YELLOW)
            if 0 >= self.sec:
               self.icon.configure(bg=RED)
            self.after(1000, self.counting)
            self.started = True
        else:
            self.label.configure(text='Click to start, RB to reset')
            self.icon.configure(bg=BLUE)
            self.started = False

    def counting(self):
        if self.started:
            self.sec -=1
            self.echo.set('%02d:%02d' % (self.sec/60, self.sec%60))
            if self.sec == 20:
                self.icon.configure(bg=YELLOW)

            if self.sec <= 0:
                t= -1 * self.sec
                self.icon.configure(bg=RED)
                self.bell()
                self.echo.set('-%02d:%02d' % (t/60, t%60))
                self.after(500, self.yellow)

            self.after(1000, self.counting)

    def yellow(self):
        if self.started:
            self.icon.configure(bg=YELLOW)


    def reset(self, event):
        if not self.started:
            self.sec=60*self.min
            self.echo.set('%02d:00' % (self.min))



if __name__ == '__main__':
    f = Frame()
    f.master.wm_attributes("-topmost", True)
    f.pack()
    f.mainloop()
