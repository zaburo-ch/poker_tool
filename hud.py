# -*- coding: utf-8 -*-
from Tkinter import *
import os
from stat import ST_MTIME
import re
import sys
from global_variable import *
from hud import *
from player import *
from tile import *

class HUD():
  def __init__(self,name,path):
    self.name = name
    self.path = path

    self.tiles = []
    self.corner = []
    self.offset = 0

    self.readHand()
    self.timestamp = os.stat(path)[ST_MTIME]
    self.init_finished = True

  def init_tiles(self,num):
    for t in self.tiles:
      t.root.destroy()
    for c in self.corner:
      c.root.destroy()

    self.table_num = num
    self.tile_pos = tile_pos_origin[num-2]
    self.master_pos = [50,50]
    self.master_size = master_size_origin

    for pos in self.tile_pos:
      self.tiles.append(StatsWidget(self,self.master_pos[0]+pos[0],self.master_pos[1]+pos[1],stats_size_origin[0],stats_size_origin[1]))
    self.corner.append(ConerWidget(self,self.master_pos[0],self.master_pos[1],corner_size_origin,corner_size_origin,True))
    self.corner.append(ConerWidget(self,self.master_pos[0]+self.master_size[0]-corner_size_origin,self.master_pos[1]+self.master_size[1]-corner_size_origin,corner_size_origin,corner_size_origin,False))

  def watch(self):
    if self.init_finished:
      file_timestamp = os.stat(self.path)[ST_MTIME]
      if self.timestamp < file_timestamp:
        self.timestamp = file_timestamp
        self.readHand()

  def readHand(self):
    f = open(self.path)
    f.seek(self.offset)
    whole_handtext = f.read()
    f.close()

    self.offset += len(whole_handtext)

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
      if not table_num in precomposed_table_size:
        sys.exit(0)
      if len(self.tiles)!=table_num:
        self.init_tiles(table_num)
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

      aggressor = ""
      bet_CB = False
      bet_count = 0

      #プリフロップ　一行目は自分のカードなのでスキップ
      for line in preflop.splitlines()[1:]:
        mo = re.match('([^:]+):\s*([^\s\n]+)',line)
        if mo and mo.group(1) in name_to_seat.keys() and mo.group(2) in ACTION_STR:
          i =  name_to_seat[mo.group(1)]
          action = mo.group(2)
          if not players[i].pay_money:
            if action == "レイズ":
              players[i].pfr_done += 1
              players[i].vpip_done += 1
              aggressor = players[i].name
              players[i].pay_money = True
            elif action == "コール":
              players[i].vpip_done += 1
              players[i].pay_money = True
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
              if action == "レイズ" or action == "ベット" or action == "コール":
                players[i].vpip_done += 1
                players[i].pay_money = True
            if bet_CB:
              players[i].ftcb_chance += 1
            if bet_count == 0 and players[i].name == aggressor:
              players[i].cb_chance += 1
            if action == "レイズ" or action == "ベット":
              players[i].pfa_bet += 1
              bet_count += 1
              if bet_count == 1 and players[i].name == aggressor:
                bet_CB = True
                players[i].cb_done += 1
              else:
                bet_CB = False
              aggressor = players[i].name
            elif action == "コール":
              players[i].pfa_call += 1
            elif action == "フォールド":
              if bet_CB:
                players[i].ftcb_done += 1
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
              if action == "レイズ" or action == "ベット" or action == "コール":
                players[i].vpip_done += 1
                players[i].pay_money = True
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
              if action == "レイズ" or action == "ベット" or action == "コール":
                players[i].vpip_done += 1
                players[i].pay_money = True
            if action == "フォールド":
              players[i].fold = True
              join_players_num -= 1
              if join_players_num == 1:
                break
        if join_players_num > 1:
          for p in players:
            if p and not p.fold:
              p.wtsd_done += 1

    i = name_to_seat[self.name]
    for t in self.tiles:
      line_str_list = []
      line_str_list.append("")
      line_str_list.append("")
      if players[i]:
        p = players[i]
        if len(p.name)>8:
          line_str_list[0] += "{0}({1:3d}) ".format(str(p.name[:8]),p.join_num)
        else:
          line_str_list[0] += "{0:<8}({1:3d}) ".format(p.name,p.join_num)
        if p.join_num == 0:
          line_str_list[0] += " - / - "
        else:
          if p.join_num == p.vpip_done:
            line_str_list[0] += "100"
          else:
            line_str_list[0] += "{0:.1f}".format(p.calc_vpip())

          if p.join_num == p.pfr_done:
            line_str_list[0] += "/100"
          else:
            line_str_list[0] += "/{0:.1f}".format(p.calc_pfr())
        if p.pfa_call == 0:
          if p.pfa_bet == 0:
            line_str_list[1] += " - "
          else:
            line_str_list[1] += " ∞ "
        else:
          line_str_list[1] += "{0:.1f}".format(p.calc_pfa())
        if p.cb_chance == 0:
          line_str_list[1] += "/ - "
        else:
          line_str_list[1] += "/{0:.1f}".format(p.calc_cb())
        if p.ftcb_chance == 0:
          line_str_list[1] += "/ - "
        else:
          line_str_list[1] += "/{0:.1f}".format(p.calc_ftcb())
        if p.wtsd_chance == 0:
          line_str_list[1] += "/ - "
        else:
          line_str_list[1] += "/{0:.1f}".format(p.calc_wtsd())
      t.setText(line_str_list)

      i += 1
      if i == len(players):
        i = 0
