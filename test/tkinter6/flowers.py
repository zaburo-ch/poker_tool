#! /usr/bin/env python
# -*- coding: shift_jis -*-
"""
flowers.py 

Show flower images

June 28, 2005
"""


import Tkinter as Tk
import Image as I
import ImageTk as Itk
import math
import scrolled_listbox as SL

# thanks to 素材屋ひなとん(http://www.jttk.zaq.ne.jp/bacsn908/)
FLOWERS = ["suisencut4.gif", "tanpopotouka1.gif", "odamakitouka.gif", "rengetouka2.gif",              \
           "ajisaicatmurasaki-a.gif", "cosmos-s.gif", "fujimurasakitouka.gif", "minaesi-5.gif",       \
           "hotarubukuro3ko.gif", "burudejinarabi.gif", "aoaji3touka.gif", "sakurasou.gif",           \
           "rengetakusann.gif", "nanohana3.gif", "suzurantouka2.gif", "liradai.gif",                  \
           "cosmostouka-b.gif", "syunrantouka2.gif", "sakuraeda9.gif", "syoubu-s.gif",                \
           "suirenpink-a.gif", "yuri2.gif", "aoasagaoline.gif", "asagaoyoujiro2.gif",                 \
           "himawari-l.gif", "yagurumagikutouka1.gif", "susukistouka.gif"]


SIZE = 100



def get_size(tup):
    """ It returns the size of images on the summary"""
    x, y = tup
    if (x<=100 and y<=100):
        return (x, y)
    elif x > y:
        r = float(SIZE) / float(x)
        return (100, int(y*r))
    else:
        r = float(SIZE) / float(y)
        return (int(x*r), 100)
        


class Frame(Tk.Frame):
    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('show flower images')
        intro = Tk.Label(self, font=('Helvetica', '12'),  justify=Tk.LEFT, wraplength='11c', width=50,
                         text =
          u"リストボックスから画像ファイルを選択してください。"
          u"左ボタンのドラッグ、Shift + 左ボタン、Ctrl + 左ボタン などで複数の画像の選択が可能です。\n"
          u"選択が終わったら、マウス右ボタンをクリックしてください。"
          u"選択された画像が左側に表示されます。")
          
        intro.pack()
        self.f = Tk.Frame(self, bd=3, relief=Tk.RIDGE)
        self.f.pack(fill=Tk.BOTH, expand=1)
        
        self.listbox = SL.ScrolledListbox(self.f, selectmode=Tk.EXTENDED)
        self.listbox.pack(side=Tk.LEFT, padx=5, pady=5, fill=Tk.Y)
        self.listbox.bind("<3>", self.show_flowers)
        self.listbox.insert(Tk.END, *FLOWERS)
            
        self.renew()
        

    def show_flowers(self, event):
        if self.images:
            self.ff.destroy()
            self.renew()
            
        selected = [ int(x) for x in self.listbox.curselection()]
        span = int(math.ceil(math.sqrt(len(selected))))
        for i, j in  enumerate(selected):
            img = I.open(FLOWERS[j])
            img = img.resize(get_size(img.size))
            tkimg = Itk.PhotoImage(img)
            la = Tk.Label(self.ff, image=tkimg)
            la.grid(row=i/span, column=i%span, sticky=Tk.SW)
            self.images.append(tkimg)
        self.listbox.selection_clear(min(selected), max(selected))


    def renew(self):
        self.images = []
        self.ff = Tk.Frame(self.f, border=3, relief=Tk.RAISED)
        self.ff.pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=1, padx =5)
        
        
##------------------------------------------------ 

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
