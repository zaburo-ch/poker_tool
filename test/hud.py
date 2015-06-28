from Tkinter import *
import time

master_size_origin = [792,547]
stats_size_origin = [180,50]
corner_size_origin = 10
line_size_origin = 18
master_size_min = [99,68]
fontsize_max = 200

tile_pos_origin = [
  [], #2
  [], #3
  [], #4
  [], #5
  [], #6
  [], #7
  [], #8
  [[306,429],[80,387],[0,271],[30,158],[187,102],[425,102],[582,158],[612,271],[532,387]] #9
  ]
tile_pos = []

line_pos = [[5,5],[5,27]]
master_pos = [50,50]
master_size = master_size_origin
cursor_pos = [0,0]
tiles = []
corner = []
opside_corner = []



class HUD():
  def __init__(self,num):
    self.root = Tk()
    global tile_pos
    tile_pos = tile_pos_origin[num-2]
    for pos in tile_pos:
      tiles.append(StatsWidget(master_pos[0]+pos[0],master_pos[1]+pos[1],stats_size_origin[0],stats_size_origin[1]))
    corner.append(ConerWidget(master_pos[0],master_pos[1],corner_size_origin,corner_size_origin,True))
    corner.append(ConerWidget(master_pos[0]+master_size[0]-corner_size_origin,master_pos[1]+master_size[1]-corner_size_origin,corner_size_origin,corner_size_origin,False))

    self.root.mainloop()


class TileWidget():
  def __init__(self,x,y,width,height):
    self.root = Toplevel()
    self.root.geometry(str(width)+"x"+str(height)+"+"+str(master_pos[0]+x)+"+"+str(master_pos[1]+y))
    self.root.overrideredirect(True)
    self.root.lift()
    self.root.wm_attributes("-alpha",0.5)
    self.root.wm_attributes("-topmost", True)
    self.x = x
    self.y = y
  def set_pos(self,x,y):
    self.root.geometry("+"+str(x)+"+"+str(y))
    self.x = x
    self.y = y
  def set_geo(self,x,y,width,height):
    self.root.geometry(str(width)+"x"+str(height)+"+"+str(x)+"+"+str(y))


class StatsWidget(TileWidget):
  def __init__(self,x,y,width,height):
    TileWidget.__init__(self,x,y,width,height)
    self.canvas = Canvas(self.root,width=width, height=height ,highlightthickness=0,bg="black")
    self.canvas.pack(fill=BOTH, expand=True)
    self.canvas.bind('<1>', drag_start)
    self.canvas.bind('<Button1-Motion>', dragging)
    self.lines = []
    self.lines.append(self.canvas.create_text(0,0, font=('Arial','16'), anchor=W, text="player(999)  / 99.9 / 99.9",fill="white"))
    self.lines.append(self.canvas.create_text(0,0, font=('Arial','16'), anchor=W, text="99.9 / 99.9 / 99.9 / 99.9",fill="white"))
    self.resize_text([1,1])

  def resize_text(self,ratio):
    fontsize = str(self.get_fontsize(int(ratio[1]*line_size_origin)))
    for i in range(len(self.lines)):
      bounds = self.canvas.bbox(self.lines[i])
      self.canvas.move(self.lines[i],int(ratio[0]*line_pos[i][0])-bounds[0],int(ratio[1]*line_pos[i][1])-bounds[1])
      self.canvas.itemconfigure(self.lines[i],font=('Arial',fontsize))

  def get_fontsize(self,height):
    for i in range(fontsize_max):
      testText = self.canvas.create_text(6,14,font=('Arial',str(i+1)),text="A")
      bounds = self.canvas.bbox(testText)
      self.canvas.delete(testText)
      if bounds[3]-bounds[1]>height:
        break
    return i


class ConerWidget(TileWidget):
  def __init__(self,x,y,width,height,side):
    TileWidget.__init__(self,x,y,width,height)
    self.frame = Frame(self.root,bg="white", width=width, height=height,borderwidth=0, relief=RAISED)
    self.frame.pack()
    self.frame.bind('<1>', drag_start)
    if side:  #left top coner is True
      self.frame.bind('<Button1-Motion>', expanding_left)
      self.frame.bind('<ButtonRelease-1>', expanded_left)
    else:
      self.frame.bind('<Button1-Motion>', expanding_right)
      self.frame.bind('<ButtonRelease-1>', expanded_right)


def drag_start(event):
  global cursor_pos
  cursor_pos = [event.x,event.y]

def dragging(event):
  dx = event.x-cursor_pos[0]
  dy = event.y-cursor_pos[1]
  if master_pos[0]+dx<0 or master_pos[1]+dy<0:
    return
  master_pos[0] += dx
  master_pos[1] += dy
  for i in range(len(tiles)):
    tiles[i].set_pos(master_pos[0]+tile_pos[i][0],master_pos[1]+tile_pos[i][1])
  corner[0].set_pos(master_pos[0],master_pos[1])
  corner[1].set_pos(master_pos[0]+master_size[0]-corner_size_origin,master_pos[1]+master_size[1]-corner_size_origin)

def expanding_left(event):
  dx = event.x-cursor_pos[0]
  dy = event.y-cursor_pos[1]
  if master_pos[0]+dx<0 or master_pos[1]+dy<0 or master_pos[0]+dx+master_size_min[0]>=corner[1].x or master_pos[1]+dy+master_size_min[1]>=corner[1].y:
    return
  master_pos[0] += dx
  master_pos[1] += dy
  corner[0].set_pos(master_pos[0],master_pos[1])

def expanded_left(event):
  master_size = [corner[1].x+corner_size_origin-master_pos[0],corner[1].y+corner_size_origin-master_pos[1]]
  ratio = [float(master_size[0])/master_size_origin[0],float(master_size[1])/master_size_origin[1]]
  for i in range(len(tiles)):
    tiles[i].set_geo( master_pos[0]+int(tile_pos[i][0]*ratio[0]),
      master_pos[1]+int(tile_pos[i][1]*ratio[1]),
      int(stats_size_origin[0]*ratio[0]),
      int(stats_size_origin[1]*ratio[1]) )
    tiles[i].resize_text(ratio)

def expanding_right(event):
  dx = event.x-cursor_pos[0]
  dy = event.y-cursor_pos[1]
  if corner[1].x+corner_size_origin+dx-master_pos[0]<master_size_min[0] or corner[1].y+corner_size_origin+dy-master_pos[1]<master_size_min[1]:
    return
  corner[1].set_pos(corner[1].x+dx,corner[1].y+dy)

def expanded_right(event):
  master_size = [corner[1].x+corner_size_origin-master_pos[0],corner[1].y+corner_size_origin-master_pos[1]]
  ratio = [float(master_size[0])/master_size_origin[0],float(master_size[1])/master_size_origin[1]]
  for i in range(len(tiles)):
    tiles[i].set_geo( master_pos[0]+int(tile_pos[i][0]*ratio[0]),
      master_pos[1]+int(tile_pos[i][1]*ratio[1]),
      int(stats_size_origin[0]*ratio[0]),
      int(stats_size_origin[1]*ratio[1]) )
    tiles[i].resize_text(ratio)

if __name__ == '__main__':
  app = HUD(9)
