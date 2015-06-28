# -*- coding: utf-8 -*-
from Tkinter import *
from global_variable import *
from hud import *
from player import *
from tile import *

class TileWidget():
  def __init__(self,master,x,y,width,height):
    self.master = master
    master_pos = self.master.master_pos

    self.root = Toplevel()
    self.root.geometry(str(width)+"x"+str(height)+"+"+str(master_pos[0]+x)+"+"+str(master_pos[1]+y))
    self.root.overrideredirect(True)
    self.root.lift()
    self.root.wm_attributes("-alpha",0.5)
    self.root.wm_attributes("-topmost", True)
    self.x = x
    self.y = y

  def drag_start(self,event):
    self.cursor_pos = [event.x,event.y]
  def set_pos(self,x,y):
    self.root.geometry("+"+str(x)+"+"+str(y))
    self.x = x
    self.y = y
  def set_geo(self,x,y,width,height):
    self.root.geometry(str(width)+"x"+str(height)+"+"+str(x)+"+"+str(y))


class StatsWidget(TileWidget):
  def __init__(self,master,x,y,width,height):
    TileWidget.__init__(self,master,x,y,width,height)
    self.canvas = Canvas(self.root,width=width, height=height ,highlightthickness=0,bg="black")
    self.canvas.pack(fill=BOTH, expand=True)
    self.canvas.bind('<1>',self.drag_start)
    self.canvas.bind('<Button1-Motion>',self.dragging)
    self.lines = []
    self.lines.append(self.canvas.create_text(0,0, font=('Arial','16'), anchor=W, text="   ",fill="white"))
    self.lines.append(self.canvas.create_text(0,0, font=('Arial','16'), anchor=W, text="   ",fill="white"))

    self.ratio = [1,1]
    self.fontsize = str(self.get_fontsize(line_size_origin))
    self.resize_text(self.ratio)

  def drag_start(self,event):
    self.cursor_pos = [event.x,event.y]

  def dragging(self,event):
    master_pos = self.master.master_pos
    tiles = self.master.tiles
    corner = self.master.corner
    tile_pos = self.master.tile_pos
    master_size = self.master.master_size

    dx = event.x-self.cursor_pos[0]
    dy = event.y-self.cursor_pos[1]
    if master_pos[0]+dx<0 or master_pos[1]+dy<0:
      return
    master_pos[0] += dx
    master_pos[1] += dy
    for i in range(len(tiles)):
      tiles[i].set_pos(master_pos[0]+tile_pos[i][0],master_pos[1]+tile_pos[i][1])
    corner[0].set_pos(master_pos[0],master_pos[1])
    corner[1].set_pos(master_pos[0]+master_size[0]-corner_size_origin,master_pos[1]+master_size[1]-corner_size_origin)

  def resize_text(self,ratio):
    if self.ratio[0] != ratio[0] or self.ratio[1] != ratio[1]:
      self.ratio = ratio
      self.fontsize = str(self.get_fontsize(int(ratio[1]*line_size_origin)))
    for i in range(len(self.lines)):
      bounds = self.canvas.bbox(self.lines[i])
      self.canvas.move(self.lines[i],int(ratio[0]*line_pos[i][0])-bounds[0],int(ratio[1]*line_pos[i][1])-bounds[1])
      self.canvas.itemconfigure(self.lines[i],font=('Arial',self.fontsize))

  def setText(self,line_str_list):
    for i in range(len(self.lines)):
      self.canvas.delete(self.lines[i])
      self.lines[i] = self.canvas.create_text(0,0,font=('Arial',self.fontsize),anchor=W,text=line_str_list[i],fill="white")
      bounds = self.canvas.bbox(self.lines[i])
      self.canvas.move(self.lines[i],int(self.ratio[0]*line_pos[i][0])-bounds[0],int(self.ratio[1]*line_pos[i][1])-bounds[1])

  def get_fontsize(self,height):
    for i in range(fontsize_max):
      testText = self.canvas.create_text(6,14,font=('Arial',str(i+1)),text="A")
      bounds = self.canvas.bbox(testText)
      self.canvas.delete(testText)
      if bounds[3]-bounds[1]>height:
        break
    return i


class ConerWidget(TileWidget):
  def __init__(self,master,x,y,width,height,side):
    TileWidget.__init__(self,master,x,y,width,height)
    self.frame = Frame(self.root,bg="white", width=width, height=height,borderwidth=0, relief=RAISED)
    self.frame.pack()
    self.frame.bind('<1>',self.drag_start)
    if side:  #left top coner is True
      self.frame.bind('<Button1-Motion>', self.expanding_left)
      self.frame.bind('<ButtonRelease-1>', self.expanded_left)
    else:
      self.frame.bind('<Button1-Motion>', self.expanding_right)
      self.frame.bind('<ButtonRelease-1>', self.expanded_right)

  def expanding_left(self,event):
    master_pos = self.master.master_pos
    corner = self.master.corner

    dx = event.x-self.cursor_pos[0]
    dy = event.y-self.cursor_pos[1]
    if master_pos[0]+dx<0 or master_pos[1]+dy<0 or master_pos[0]+dx+master_size_min[0]>=corner[1].x or master_pos[1]+dy+master_size_min[1]>=corner[1].y:
      return
    master_pos[0] += dx
    master_pos[1] += dy
    corner[0].set_pos(master_pos[0],master_pos[1])

  def expanded_left(self,event):
    master_pos = self.master.master_pos
    tiles = self.master.tiles
    corner = self.master.corner
    tile_pos = self.master.tile_pos

    master_size = [corner[1].x+corner_size_origin-master_pos[0],corner[1].y+corner_size_origin-master_pos[1]]
    ratio = [float(master_size[0])/master_size_origin[0],float(master_size[1])/master_size_origin[1]]
    self.master.master_size = master_size

    for i in range(len(tiles)):
      tiles[i].set_geo( master_pos[0]+int(tile_pos[i][0]*ratio[0]),
        master_pos[1]+int(tile_pos[i][1]*ratio[1]),
        int(stats_size_origin[0]*ratio[0]),
        int(stats_size_origin[1]*ratio[1]) )
      tiles[i].resize_text(ratio)

  def expanding_right(self,event):
    master_pos = self.master.master_pos
    corner = self.master.corner

    dx = event.x-self.cursor_pos[0]
    dy = event.y-self.cursor_pos[1]
    if corner[1].x+corner_size_origin+dx-master_pos[0]<master_size_min[0] or corner[1].y+corner_size_origin+dy-master_pos[1]<master_size_min[1]:
      return
    corner[1].set_pos(corner[1].x+dx,corner[1].y+dy)

  def expanded_right(self,event):
    master_pos = self.master.master_pos
    tiles = self.master.tiles
    corner = self.master.corner
    tile_pos = self.master.tile_pos

    master_size = [corner[1].x+corner_size_origin-master_pos[0],corner[1].y+corner_size_origin-master_pos[1]]
    ratio = [float(master_size[0])/master_size_origin[0],float(master_size[1])/master_size_origin[1]]
    self.master.master_size = master_size
    for i in range(len(tiles)):
      tiles[i].set_geo( master_pos[0]+int(tile_pos[i][0]*ratio[0]),
        master_pos[1]+int(tile_pos[i][1]*ratio[1]),
        int(stats_size_origin[0]*ratio[0]),
        int(stats_size_origin[1]*ratio[1]) )
      tiles[i].resize_text(ratio)
