# -*- coding: utf-8 -*-
import datetime
import time
import os
#from stat import *
from stat import ST_MTIME
import re
import sys

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

    player_sb = re.findall('^([^:]+):\s*SBをポスト',info,re.M)[0]
    all_players[player_sb].sb_num += 1
    player_bb = re.findall('^([^:]+):\s*BBをポスト',info,re.M)[0]
    all_players[player_bb].bb_num += 1

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

    #出力
    for p in players:
      if not p:
        continue
      print "--{0:-<20}-({1:3d} hands)-----------".format(p.name,p.join_num)
      output = ""
      if p.join_num == 0:
        output += " -- / -- "
      else:
        if p.join_num == p.vpip_done:
          output += "100"
        else:
          output += "{0:.1f}".format(p.clac_vpip())

        if p.join_num == p.pfr_done:
          output += "/100"
        else:
          output += "/{0:.1f}".format(p.clac_pfr())
      if p.pfa_call == 0:
        if p.pfa_bet == 0:
          output += "/ - "
        else:
          output += "/ ∞ "
      else:
        output += "/{0:.1f}".format(p.clac_pfa())
      if p.wtsd_chance == 0:
        output += "/ - "
      else:
        output += "/{0:.1f}".format(p.clac_wtsd())
      print output

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
