import tkMessageBox
from Tkinter import *

class App():
    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(1)
        self.frame = Frame(self.root, width=320, height=200,
                           borderwidth=2, relief=RAISED)
        self.frame.pack_propagate(False)
        self.frame.pack()
        self.bQuit = Button(self.frame, text="Quit",
                            command=self.root.quit)
        self.bQuit.pack(pady=20)
        self.bHello = Button(self.frame, text="Hello",
                             command=self.hello)
        self.bHello.pack(pady=20)

    def hello(self):
        tkMessageBox.showinfo("Popup", "Hello!")

app = App()
app.root.mainloop()