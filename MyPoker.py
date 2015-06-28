# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
import re
from global_variable import *
from hud import *
from player import *
from tile import *

class MainWindow():
  def __init__(self):
    self.root = Tk()
    self.root.title("MyPoker")
    self.frame = Frame(self.root)
    self.frame.pack()
    self.bHello = Button(self.frame, text="履歴ファイルを選択",command=self.file_select)
    self.bHello.pack(pady=5,padx=5)
    self.bQuit = Button(self.frame, text="終了",command=self.root.quit)
    self.bQuit.pack(pady=5,padx=5)
    self.hud_list = []

    self.root.mainloop()

  def file_select(self):
    filename = askopenfilename(filetypes=[('hand history file','.txt')])
    if filename!="":
      mo = re.match('.*/([^/]+)/[^/]+$',filename)
      if mo:
        self.hud_list.append(HUD(mo.group(1),filename))
        if len(self.hud_list)==1:
          self.root.after(300,self.watch_all)

  def watch_all(self):
    for hud in self.hud_list:
      hud.watch()
    self.root.after(300,self.watch_all)


if __name__ == '__main__':
  app = MainWindow()