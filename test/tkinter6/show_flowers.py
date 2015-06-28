#! /usr/bin/env python
# -*- coding: euc-jp -*-
"""
show_flowers.py 

Change Background of flower

June 28, 2005
"""


import Tkinter as Tk

# thanks to 素材屋ひなとん(http://www.jttk.zaq.ne.jp/bacsn908/)
FLOWERS = ["suisencut4.gif", "tanpopotouka1.gif", "odamakitouka.gif", "rengetouka2.gif",              \
           "ajisaicatmurasaki-a.gif", "cosmos-s.gif", "fujimurasakitouka.gif", "minaesi-5.gif",       \
           "hotarubukuro3ko.gif", "burudejinarabi.gif", "aoaji3touka.gif", "sakurasou.gif",           \
           "rengetakusann.gif", "nanohana3.gif", "suzurantouka2.gif", "liradai.gif",                  \
           "cosmostouka-b.gif", "syunrantouka2.gif", "sakuraeda9.gif", "syoubu-s.gif",                \
           "suirenpink-a.gif", "yuri2.gif", "aoasagaoline.gif", "asagaoyoujiro2.gif",                 \
           "himawari-l.gif", "yagurumagikutouka1.gif", "susukistouka.gif"]


BGS = [('aliceblue', '#F0F8FF'), ('azure', '#F0FFFF'), ('beige', '#F5F5DC'),              \
       ('cornsilk', '#FFF8DC'), ('khaki', '#F0E68C'), ('lightgreen', '#90EE90'),          \
       ('lightpink', '#FFB6C1'), ('lightskyblue', '#87CEFA'), ('palegreen', '#98FB98')]

class ScrolledListbox(Tk.Listbox):
    """ Listbox with vertical scroll bar """
    
    def __init__(self, master, **key):
        self.frame = Tk.Frame(master)
        self.yscroll = Tk.Scrollbar (self.frame, orient=Tk.VERTICAL)
        self.yscroll.pack(side=Tk.RIGHT, fill=Tk.Y, expand=1)
        key['yscrollcommand']=self.yscroll.set
        Tk.Listbox.__init__(self, self.frame, **key)
        self.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.yscroll.config(command=self.yview)

        # Copy geometry methods of self.frame 
        for m in (Tk.Pack.__dict__.keys() + Tk.Grid.__dict__.keys() + Tk.Place.__dict__.keys()):
            m[0] == '_' or m == 'config' or m == 'configure' or \
                setattr(self, m, getattr(self.frame, m))


class BgChange:

    def __init__(self, label, color):
        self.label = label
        self.color = color

    def __call__(self, event=None):
        self.label.configure(bg=self.color)


class Frame(Tk.Frame):
    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('show flower images')
        intro = Tk.Label(self, font=('Helvetica', '12'),  justify=Tk.LEFT, wraplength='8c', 
                         text = u"リストボックスから画像ファイル（マウス左ダブルクリック）、"
                                u"ボタンから背景色を選択してください。" 
                                u"左側のラベルに画像が表示されます。")
        intro.pack()
        f = Tk.Frame(self, bd=3, relief=Tk.RIDGE)
        f.pack(fill=Tk.BOTH, expand=1)
        
        self.listbox = ScrolledListbox(f)
        self.listbox.pack(side=Tk.LEFT, padx=5, pady=5, fill=Tk.Y)
        self.listbox.bind("<Double-Button-1>", self.change_flower)
        for flw in FLOWERS:
            self.listbox.insert(Tk.END, flw)
            
        f_button = Tk.Frame(f)
        f_button.pack(side=Tk.LEFT, padx=5, pady=5)
        self.flower = Tk.PhotoImage(file=FLOWERS[0])
        self.label = Tk.Label(f, image=self.flower, relief=Tk.RAISED, bd=3)
        self.label.pack(side=Tk.RIGHT, padx =5)

        for name, code in BGS:
            b = Tk.Button(f_button, text=name,  bg=code, command=BgChange(self.label, code))
            b.pack(fill=Tk.X)

    def change_flower(self, event):
        tup = self.listbox.curselection()
        if tup:
            i = int(tup[0])
            self.flower = Tk.PhotoImage(file=FLOWERS[i])
            self.label.configure(image=self.flower)

            
##------------------------------------------------ 

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
