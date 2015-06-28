# -*- coding: utf-8 -*-

class Player:
  def __init__(self,name):
    self.name = name
    self.pay_money = False
    self.fold = False
    self.join_num = 1
    self.bb_num = 0
    self.sb_num = 0

    """
      ここで、
      * 参加はテーブルにつきカードをもらうこと
      * CBは前のラウンドで最後にベットorレイズした人のベット
      を言うものとする
      VPIP : 1度でもポッドにお金を入れたハンド / 参加したハンド
      PFR  : プリフロップで(自分がまだお金を出していない状態から)レイズしたハンド / 参加したハンド
      PFA  : ポストフロップでレイズorベットした回数 / コールした回数
      WTSD : ショウダウンまで行った回数 / ポストフロップまで行った回数
      CB   : フロップでCBを打った回数 / フロップでCBを打てた回数
      FTCB : フロップでCBにフォールドした回数 / フロップでCBにアクションをした回数
    """
    self.vpip_done = 0
    self.pfr_done = 0
    self.pfa_call = 0
    self.pfa_bet = 0
    self.wtsd_chance = 0
    self.wtsd_done = 0
    self.cb_chance = 0
    self.cb_done = 0
    self.ftcb_chance = 0
    self.ftcb_done = 0

  def calc_vpip(self):
    return float(self.vpip_done*100)/self.join_num

  def calc_pfr(self):
    return float(self.pfr_done*100)/self.join_num

  def calc_pfa(self):
    return float(self.pfa_bet)/self.pfa_call

  def calc_cb(self):
    return float(self.cb_done*100)/self.cb_chance

  def calc_ftcb(self):
    return float(self.ftcb_done*100)/self.ftcb_chance

  def calc_wtsd(self):
    return float(self.wtsd_done*100)/self.wtsd_chance