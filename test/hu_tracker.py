# -*- coding: utf-8 -*-
import datetime
import time
import os
#from stat import *
from stat import ST_MTIME
import re
import sys

DIRECTORY = "/Users/user/Library/Application Support/PokerStars/HandHistory/musharna000"

offset = 0
players = {}

class Player:
  def __init__(self,name):
    self.name = name
    self.is_join = True
    self.join_num = 1
    self.bb_num = 0
    self.sb_num = 0
    self.tb_chance = 0       #Three Bet
    self.tb_done = 0
    self.fts_chance = 0      #Fold To Steal
    self.fts_done = 0
    self.pc_chance = 0       #Preflop Call
    self.pc_done = 0
    self.ffc_chance = 0      #Flop Fold vs CB
    self.ffc_done = 0

  def calc_tb(self):
    return float(self.tb_done*100)/self.tb_chance

  def calc_fts(self):
    return float(self.fts_done*100)/self.fts_chance

  def calc_pc(self):
    return float(self.pc_done*100)/self.pc_chance

  def calc_ffc(self):
    return float(self.ffc_done*100)/self.ffc_chance

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
    print showdown

    #---------------infoから参加者とBB,SBの情報取得---------------
    #既存のプレイヤーの参加フラグをリセット
    for p in players.values():
      p.is_join = False

    for name in re.findall('^シート\s*\d+:\s*([^(]+)',info,re.M):
      if name in players:
        players[name].join_num += 1
        players[name].is_join = True
      else:
        players[name] = Player(name)

    #参加していないプレイヤーを取り除く
    players = dict((name,players[name]) for name in players if players[name].is_join)
    if len(players)!=2:
      print "Not HU"
      sys.exit(1)
      return
    player_sb = re.findall('^([^:]+):\s*SBをポスト',info,re.M)[0]
    players[player_sb].sb_num += 1
    player_bb = re.findall('^([^:]+):\s*BBをポスト',info,re.M)[0]
    players[player_bb].bb_num += 1

    #---------------各ラウンドの動作---------------

    #プリフロップ　一行目は自分のカードなのでスキップ
    bet_count = 1
    aggressor = ""
    for line in preflop.splitlines()[1:]:
      mo = re.match('([^:]+):\s*([^\s\n]+)',line)
      if mo:
        name = mo.group(1)
        #action = actionstrToInt(mo.group(2))
        action = mo.group(2)
        if bet_count==1:
          #ブラインドだけがある状態
          if name == player_sb:
            players[name].pc_chance += 1
            if action == "レイズ":
              aggressor = name
              bet_count += 1
            elif action == "コール":
              players[name].pc_done += 1
          elif name == player_bb:
            if action == "レイズ":
              aggressor = name
              bet_count += 1
          """
          ヘッズアップ向けで限定するので今回は省略
          else:
            pass
          """
        elif bet_count==2:
          players[name].tb_chance += 1
          players[name].pc_chance += 1
          players[name].fts_chance += 1
          if action == "レイズ":
            aggressor = name
            bet_count += 1
            players[name].tb_done += 1
          elif action == "コール":
            players[name].pc_done += 1
          elif action == "フォールド":
            players[name].fts_done += 1
        elif bet_count>2:
          players[name].pc_chance += 1
          if action == "コール":
            players[name].pc_done += 1
        if action == "フォールド":
          break

    #フロップ　一行目はフロップのカードなのでスキップ
    if flop:
      bet_count = 0
      cb = False
      for line in flop.splitlines()[1:]:
        mo = re.match('([^:]+):\s*([^\s\n]+)',line)
        if mo:
          name = mo.group(1)
          #action = actionstrToInt(mo.group(2))
          action = mo.group(2)
          if bet_count==0:
            if action == "ベット":
              bet_count += 1
              if name == aggressor:
                cb = True
          elif bet_count==1 and cb:
            players[name].ffc_chance += 1
            if action == "フォールド":
              players[name].ffc_done += 1
          if action == "フォールド":
            break

    #出力
    for p in players.values():
      print "--{0:-<20}-({1:3d} hands)-----------".format(p.name,p.join_num)
      if p.tb_chance == 0:
        print "3Bet             :    -"
      else:
        print "3Bet             :  {0:.1f}%".format(p.calc_tb())
      if p.fts_chance == 0:
        print "Fold to Steal    :    -"
      else:
        print "Fold to Steal    :  {0:.1f}%".format(p.calc_fts())
      if p.pc_chance == 0:
        print "Preflop Call     :    -"
      else:
        print "Preflop Call     :  {0:.1f}%".format(p.calc_pc())
      if p.ffc_chance == 0:
        print "Flop Fold vs CB  :    -"
      else:
        print "Flop Fold vs CB  :  {0:.1f}%".format(p.calc_ffc())
    print

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

if __name__ == '__main__':
  filename = selectFile()
  readHand(DIRECTORY+"/"+filename)
  watch(DIRECTORY+"/"+filename)
