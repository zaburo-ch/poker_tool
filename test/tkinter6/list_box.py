# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))

buffer = StringVar()
buffer.set("")

e = Entry(root, textvariable = buffer)

lb = Listbox(root)

sb1 = Scrollbar(root, orient = 'v', command = lb.yview)
sb2 = Scrollbar(root, orient = 'h', command = lb.xview)

lb.configure(yscrollcommand = sb1.set)
lb.configure(xscrollcommand = sb2.set)

def calc(event):
    expr = buffer.get()
    lb.insert('end', expr)
    lb.see('end')
    value = eval(expr)
    buffer.set(str(value))

def get_expr(event):
    buffer.set(lb.get('active'))

e.bind('<Return>', calc)
lb.bind('<Double-1>', get_expr)

e.grid(row = 0, columnspan = 2, sticky = 'ew')
lb.grid(row = 1, column = 0, sticky = 'nsew')
sb1.grid(row = 1, column = 1, sticky = 'ns')
sb2.grid(row = 2, column = 0, sticky = 'ew')

e.focus_set()

root.mainloop()
