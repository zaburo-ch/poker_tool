# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
import datetime
import time
import os
from stat import ST_MTIME
import re
import sys

username = ""

# hud.py
master_size_origin = [792,547]
stats_size_origin = [180,50]
corner_size_origin = 10
line_size_origin = 18
master_size_min = [99,68]
fontsize_max = 200

precomposed_table_size = [2,6,9]
tile_pos_origin = [
  [[480,366],[480,56]], #2
  [], #3
  [], #4
  [], #5
  [], #6
  [[306,429],[0,332],[0,160],[306,0],[612,160],[612,332]], #7
  [], #8
  [[306,429],[80,387],[0,271],[0,158],[38,24],[582,24],[612,158],[612,271],[532,387]] #9
  ]
tile_pos = []

line_pos = [[5,5],[5,27]]
master_pos = [50,50]
master_size = master_size_origin
cursor_pos = [0,0]
tiles = []
corner = []
opside_corner = []


#multi_tracker.py
DIRECTORY = "/Users/user/Library/Application Support/PokerStars/HandHistory/musharna000"
ACTION_STR = ["レイズ","ベット","フォールド","チェック","コール"]

offset = 0
all_players = {}


class Player:
  def __init__(self,name):
    self.name = name
    self.pay_money = False
    self.fold = False
    self.join_num = 1
    self.bb_num = 0
    self.sb_num = 0

    """
      ここで、参加はテーブルにつきカードをもらうことを言う
      VPIP : 1度でもポッドにお金を入れたハンド / 参加したハンド
      PFR  : プリフロップで(自分がまだお金を出していない状態から)レイズしたハンド / 参加したハンド
      PFA  : ポストフロップでレイズorベットした回数 / コールした回数
      WTSD : ショウダウンまで行った回数 / ポストフロップまで行った回数
    """
    self.vpip_done = 0
    self.pfr_done = 0
    self.pfa_call = 0
    self.pfa_bet = 0
    self.wtsd_chance = 0
    self.wtsd_done = 0

  def clac_vpip(self):
    return float(self.vpip_done*100)/self.join_num

  def clac_pfr(self):
    return float(self.pfr_done*100)/self.join_num

  def clac_pfa(self):
    return float(self.pfa_bet)/self.pfa_call

  def clac_wtsd(self):
    return float(self.wtsd_done*100)/self.wtsd_chance

def watch(path):
  timestamp = time.mktime(datetime.datetime.now().utctimetuple())
  while True:
    file_timestamp = os.stat(path)[ST_MTIME]
    if timestamp < file_timestamp:
      timestamp = file_timestamp
      readHand(path)
    time.sleep(0.3)

def readHand(path):
  global offset
  global players

  f = open(path)
  f.seek(offset)
  whole_handtext = f.read()
  f.close()

  offset += len(whole_handtext)

  handtexts = whole_handtext.split("\n\n\n\n")
  players = []
  for handtext in handtexts:

    #---------------ランド毎にhandtextを分割---------------

    temp = handtext.split("\n*** ホールカード ***\n")
    if len(temp)==1:
      continue
    info = temp[0]

    temp = temp[1].split("\n*** フロップ ***")
    preflop = temp[0]

    if len(temp)==1:
      flop = None
    else:
      temp = temp[1].split("\n*** ターン ***")
      flop = temp[0]

    if len(temp)==1:
      turn = None
    else:
      temp = temp[1].split("\n*** リバー ***")
      turn = temp[0]

    if len(temp)==1:
      river = None
    else:
      temp = temp[1].split("\n*** ショーダウン ***")
      river = temp[0]

    if len(temp)==1:
      showdown = None
    else:
      showdown = temp[1]


    #---------------infoから参加者とBB,SBの情報取得---------------
    table_num = int(re.findall("(\d)-max",info.splitlines()[1])[0])
    if not table_num in precomposed_table_size:
      sys.exit(0)
    if len(tiles)!=table_num:
      init_tiles(table_num)
    players = []
    name_to_seat = {}
    join_players_num = 0
    seat = 1
    for line in info.splitlines()[2:]:
      while True:
        if seat > table_num:
          break
        mo = None
        if line.find("プレイ一時中断")<0:
          mo = re.match('シート\s*'+str(seat)+':\s*([^(]+)',line)
        else:
          players.append(None)
          seat += 1
          break
        if mo:
          name = mo.group(1)
          if name in all_players:
            all_players[name].join_num += 1
            all_players[name].pay_money = False
            all_players[name].fold = False
          else:
            all_players[name] = Player(name)
          players.append(all_players[name])
          name_to_seat[name] = seat-1
          seat += 1
          join_players_num += 1
          break
        else:
          players.append(None)
          seat += 1

    #---------------各ラウンドの動作---------------

    #プリフロップ　一行目は自分のカードなのでスキップ
    for line in preflop.splitlines()[1:]:
      mo = re.match('([^:]+):\s*([^\s\n]+)',line)
      if mo and mo.group(1) in name_to_seat.keys() and mo.group(2) in ACTION_STR:
        i =  name_to_seat[mo.group(1)]
        action = mo.group(2)
        if not players[i].pay_money:
          players[i].pay_money = True
          if action == "レイズ":
            players[i].pfr_done += 1
            players[i].vpip_done += 1
          elif action == "コール":
            players[i].vpip_done += 1
        if action == "フォールド":
          players[i].fold = True
          join_players_num -= 1
          if join_players_num == 1:
            break

    #フロップ　一行目はフロップのカードなのでスキップ
    if flop:
      for p in players:
        if p:
          p.wtsd_chance += 1
      for line in flop.splitlines()[1:]:
        mo = re.match('([^:]+):\s*([^\s\n]+)',line)
        if mo and mo.group(1) in name_to_seat.keys() and mo.group(2) in ACTION_STR:
          i =  name_to_seat[mo.group(1)]
          action = mo.group(2)
          if not players[i].pay_money:
            players[i].pay_money = True
            if action == "レイズ" or action == "コール":
              players[i].vpip_done += 1
          if action == "レイズ" or action == "ベット":
            players[i].pfa_bet += 1
          elif action == "コール":
            players[i].pfa_call += 1
          elif action == "フォールド":
            players[i].fold = True
            join_players_num -= 1
            if join_players_num == 1:
              break

    #ターン　一行目はフロップのカードなのでスキップ
    if turn:
      for line in turn.splitlines()[1:]:
        mo = re.match('([^:]+):\s*([^\s\n]+)',line)
        if mo and mo.group(1) in name_to_seat.keys() and mo.group(2) in ACTION_STR:
          i =  name_to_seat[mo.group(1)]
          action = mo.group(2)
          if not players[i].pay_money:
            players[i].pay_money = True
            if action == "レイズ" or action == "コール":
              players[i].vpip_done += 1
          if action == "フォールド":
            players[i].fold = True
            join_players_num -= 1
            if join_players_num == 1:
              break

    #リバー　一行目はフロップのカードなのでスキップ
    if river:
      for line in river.splitlines()[1:]:
        mo = re.match('([^:]+):\s*([^\s\n]+)',line)
        if mo and mo.group(1) in name_to_seat.keys() and mo.group(2) in ACTION_STR:
          i =  name_to_seat[mo.group(1)]
          action = mo.group(2)
          if not players[i].pay_money:
            players[i].pay_money = True
            if action == "レイズ" or action == "コール":
              players[i].vpip_done += 1
          if action == "フォールド":
            players[i].fold = True
            join_players_num -= 1
            if join_players_num == 1:
              break
      if join_players_num > 1:
        for p in players:
          if p and not p.fold:
            p.wtsd_done += 1

  i = name_to_seat[username]
  for t in tiles:
    if players[i]:
      p = players[i]
      line_str_list = []
      line_str_list.append("")
      line_str_list.append("")
      if len(p.name)>8:
        line_str_list[0] += "{0}({1:3d})".format(str(p.name[:8]),p.join_num)
      else:
        line_str_list[0] += "{0:<8}({1:3d})".format(p.name,p.join_num)
      if p.join_num == 0:
        line_str_list[1] += " -- / -- "
      else:
        if p.join_num == p.vpip_done:
          line_str_list[1] += "100"
        else:
          line_str_list[1] += "{0:.1f}".format(p.clac_vpip())

        if p.join_num == p.pfr_done:
          line_str_list[1] += "/100"
        else:
          line_str_list[1] += "/{0:.1f}".format(p.clac_pfr())
      if p.pfa_call == 0:
        if p.pfa_bet == 0:
          line_str_list[1] += "/ - "
        else:
          line_str_list[1] += "/ ∞ "
      else:
        line_str_list[1] += "/{0:.1f}".format(p.clac_pfa())
      if p.wtsd_chance == 0:
        line_str_list[1] += "/ - "
      else:
        line_str_list[1] += "/{0:.1f}".format(p.clac_wtsd())

      t.setText(line_str_list)

    i += 1
    if i == len(players):
      i = 0

def cmpFileTimestamp(x,y):
  return os.stat(DIRECTORY+"/"+y)[ST_MTIME] - os.stat(DIRECTORY+"/"+x)[ST_MTIME]

def selectFile():
  print "select hand history file"
  page = 0
  while True:
    file_list = [i for i in os.listdir(DIRECTORY) if i[0]!='.']
    file_list.sort(cmp = cmpFileTimestamp)
    print "page:{0:5d}".format(page)
    for i in range(10):
      if i+page*10>=len(file_list):
        break
      print "{0:d}:{1}".format(i+page*10,file_list[i+page*10])
    if page == 0:
      sys.stdout.write("input 0~9 or next: ")
    elif page==(len(file_list)+9)/10-1:
      sys.stdout.write("input 0~9 or back: ")
    else:
      sys.stdout.write("input 0~9 or next or back: ")
    c = raw_input()
    if '0'<=c and c<='9':
      return file_list[int(c)]
    elif c == "next" and page<(len(file_list)+9)/10-1:
      page += 1
    elif c == "back" and page > 0:
      page -= 1
    print


#----------------------------------------------------------------

class HUD():
  def __init__(self):
    self.root = Tk()
    self.root.title("MyPoker")
    self.frame = Frame(self.root)
    self.frame.pack()
    self.bHello = Button(self.frame, text="履歴ファイルを選択",command=self.file_select)
    self.bHello.pack(pady=5,padx=5)
    self.bQuit = Button(self.frame, text="終了",command=self.root.quit)
    self.bQuit.pack(pady=5,padx=5)
    self.root.mainloop()

  def file_select(self):
    filename = askopenfilename(filetypes=[('hand history file','.txt')])
    if filename!="":
      mo = re.match('.*/([^/]+)/[^/]+$',filename)
      if mo:
        global username
        username = mo.group(1)
        self.start_track(filename)

  def start_track(self,path):
    readHand(path)

    self.path = path
    self.timestamp = os.stat(path)[ST_MTIME]
    self.watch()

  def watch(self):
    file_timestamp = os.stat(self.path)[ST_MTIME]
    if self.timestamp < file_timestamp:
      self.timestamp = file_timestamp
      readHand(self.path)
    self.root.after(300,self.watch)

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
    self.lines.append(self.canvas.create_text(0,0, font=('Arial','16'), anchor=W, text="   ",fill="white"))
    self.lines.append(self.canvas.create_text(0,0, font=('Arial','16'), anchor=W, text="   ",fill="white"))

    self.ratio = [1,1]
    self.fontsize = str(self.get_fontsize(line_size_origin))
    self.resize_text(self.ratio)

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

def init_tiles(num):
  global tile_pos,master_pos,master_pos
  for t in tiles:
    t.root.destroy()
  for c in corner:
    c.root.destroy()

  master_pos = [50,50]
  master_size = master_size_origin

  tile_pos = tile_pos_origin[num-2]
  for pos in tile_pos:
    tiles.append(StatsWidget(master_pos[0]+pos[0],master_pos[1]+pos[1],stats_size_origin[0],stats_size_origin[1]))
  corner.append(ConerWidget(master_pos[0],master_pos[1],corner_size_origin,corner_size_origin,True))
  corner.append(ConerWidget(master_pos[0]+master_size[0]-corner_size_origin,master_pos[1]+master_size[1]-corner_size_origin,corner_size_origin,corner_size_origin,False))


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
  app = HUD()
