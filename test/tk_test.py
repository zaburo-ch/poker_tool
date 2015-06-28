# -*- coding: utf-8 -*-
from Tkinter import *

class ScrolledListbox(Listbox):
  def __init__(self, master, **key):
    self.frame = Frame(master,relief=SUNKEN, bd=2)
    self.yscroll = Scrollbar(self.frame,orient=VERTICAL)
    self.yscroll.pack(side=RIGHT, fill=Y, expand=1)
    key['yscrollcommand']=self.yscroll.set
    Listbox.__init__(self, self.frame,width=50,height=10, **key)
    self.pack(side=LEFT, fill=BOTH, expand=1)
    self.yscroll.config(command=self.yview)
    self.config(borderwidth=0)

    # Copy geometry methods of self.frame
    for m in (Pack.__dict__.keys() + Grid.__dict__.keys() + Place.__dict__.keys()):
      m[0] == '_' or m == 'config' or m == 'configure' or \
        setattr(self, m, getattr(self.frame, m))

class MainWindow():
  def __init__(self):
    self.root = Tk()
    self.frame = Frame(self.root)
    self.frame.pack(fill=BOTH, expand=YES)
    self.listbox = ScrolledListbox(self.frame)
    self.listbox.pack(padx=10, pady=10, fill=Y)
    self.bQuit = Button(self.frame, text="終了",command=self.root.quit)
    self.bQuit.pack(pady=5)
    #self.listbox.insert(END,*FLOWERS)

    self.root.mainloop()

if __name__ == '__main__':
    MainWindow()
