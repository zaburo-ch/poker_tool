#! /usr/bin/env python

"""
style.py

This demonstration script creates a text widget that illustrates the
various display styles that may be set for tags.

June 14, 2005
"""


import Tkinter as Tk
import template as A
from ScrolledText import ScrolledText





class Demo(A.Demo):
    """ a demo for styled text """



    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        self.demo_main_frame.master.title("Text Demonstration - Display Styles")
        self.demo_main_frame.master.geometry('500x500+50+50')
        stext= ScrolledText(self.demo_frame, wrap=Tk.WORD)
        stext.pack(fill=Tk.BOTH, expand=1)
        
# Set up display styles

        stext.tag_config("bold", font=("Courier", "12", "bold", "italic"))
        stext.tag_config("big", font=("Courier", "14", "bold"))
        stext.tag_config("verybig",  font=("Helvetica", "24", "bold"))
        if (self.demo_frame.winfo_depth() > 1):
            stext.tag_config("color1",  background="#a0b7ce")
            stext.tag_config("color2", foreground="red")
            stext.tag_config("raised", relief=Tk.RAISED, borderwidth=1)
            stext.tag_config("sunken", relief=Tk.SUNKEN, borderwidth=1)  #### here!!!!
        else:
            stext.tag_config("color1", background = "black", foreground = "white")
            stext.tag_config("color2", background = "black", foreground = "white")
            stext.tag_config("raised", background = "white",  relief=Tk.RAISED, borderwidth=1)
            stext.tag_config("sunken", background = "white",  relief= Tk.SUNKEN, borderwidth=1)

        stext.tag_config("bgstipple", background = "black", borderwidth = 0, bgstipple= "gray12") 
        stext.tag_config("fgstipple", fgstipple= "gray50")
        stext.tag_config("underline", underline=1)
        stext.tag_config("overstrike", overstrike=1)
        stext.tag_config("right", justify=Tk.RIGHT)
        stext.tag_config("center", justify=Tk.CENTER)
        stext.tag_config("super", offset= "4p",  font=("Courier", "10"))
        stext.tag_config("sub", offset="-2p", font=("Courier", "10"))
        stext.tag_config("margins", lmargin1="12m", lmargin2="6m", rmargin="10m")
        stext.tag_config("spacing", spacing1="10p", spacing2="2p", lmargin1="12m", lmargin2="6m", rmargin="10m") 

## Text
        
        stext.insert(Tk.END, 
"""Text widgets like this one allow you to display information in a
variety of styles.  Display styles are controlled using a mechanism
called """)
        stext.insert(Tk.END, "tags", "bold")
        stext.insert(Tk.END, """. Tags are just textual names that you can apply to one
or more ranges of characters within a text widget.  You can configure
tags with various display styles.  If you do this, then the tagged
characters will be displayed with the styles you chose.  The
available display styles are:""")

        stext.insert(Tk.END,  "\n1. Font.", "big")
        stext.insert(Tk.END, "  You can choose any X font, ")
        stext.insert(Tk.END, "large", "verybig")
        stext.insert(Tk.END, " or ")
        stext.insert(Tk.END, "small.\n")
        stext.insert(Tk.END, "\n2. Color.", "big")
        stext.insert(Tk.END, "  You can change either the ")
        stext.insert(Tk.END, "background", "color1")
        stext.insert(Tk.END, " or ")
        stext.insert(Tk.END, "foreground", "color2")
        stext.insert(Tk.END, "\ncolor, or ")
        stext.insert(Tk.END, "both", ("color1", "color2"))
        stext.insert(Tk.END, ".\n")
        stext.insert(Tk.END, "\n3. Stippling.", "big")
        stext.insert(Tk.END, "  You can cause either the ")
        stext.insert(Tk.END, "background", "bgstipple")
        stext.insert(Tk.END, " or ")
        stext.insert(Tk.END, "foreground", "fgstipple")
        stext.insert(Tk.END, "information to be drawn with a stipple fill instead of a solid fill.\n")
        stext.insert(Tk.END, "\n4. Underlining.", "big")
        stext.insert(Tk.END, "  You can ")
        stext.insert(Tk.END, "underline", "underline")
        stext.insert(Tk.END,  " ranges of text.\n")
        stext.insert(Tk.END, "\n5. Overstrikes.", "big")
        stext.insert(Tk.END, "  You can ")
        stext.insert(Tk.END, "draw lines through", "overstrike")
        stext.insert(Tk.END,  " ranges of text.\n")
        stext.insert(Tk.END,  "\n6. 3-D effects.", "big")
        stext.insert(Tk.END,  "You can arrange for the background to be drawn with a border that makes characters appear either ")
        stext.insert(Tk.END,  "raised", "raised")
        stext.insert(Tk.END,  " or ")
        stext.insert(Tk.END,  "sunken", "sunken")
        stext.insert(Tk.END,  ".\n")
        stext.insert(Tk.END,  "\n7. Justification.", "big")
        stext.insert(Tk.END,  " You can arrange for lines to be displayed\n")
        stext.insert(Tk.END,  "left-justified,\n")
        stext.insert(Tk.END,  "right-justified, or\n", "right")
        stext.insert(Tk.END,  "centered.\n", "center")
        stext.insert(Tk.END,  "\n8. Superscripts and subscripts.",  "big")
        stext.insert(Tk.END,  " You can control the vertical\n")
        stext.insert(Tk.END,  "position of text to generate superscript effects like 10")
        stext.insert(Tk.END,  "n", "super")
        stext.insert(Tk.END,  " or\nsubscript effects like X")
        stext.insert(Tk.END,  "i", "sub")
        stext.insert(Tk.END,  ".\n")
        stext.insert(Tk.END,  "\n9. Margins.", "big")
        stext.insert(Tk.END,  " You can control the amount of extra space left")
        stext.insert(Tk.END,  " on\neach side of the text:\n")
        stext.insert(Tk.END,  "This paragraph is an example of the use of ", "margins")
        stext.insert(Tk.END,  "margins.  It consists of a single line of text ", "margins")
        stext.insert(Tk.END,  "that wraps around on the screen.  There are two ", "margins")
        stext.insert(Tk.END,  "separate left margin values, one for the first ", "margins")
        stext.insert(Tk.END,  "display line associated with the text line, ", "margins")
        stext.insert(Tk.END,  "and one for the subsequent display lines, which ", "margins")
        stext.insert(Tk.END,  "occur because of wrapping.  There is also a ", "margins")
        stext.insert(Tk.END,  "separate specification for the right margin, ", "margins")
        stext.insert(Tk.END,  "which is used to choose wrap points for lines.\n", "margins")
        stext.insert(Tk.END,  "\n10. Spacing.", "big")
        stext.insert(Tk.END,  " You can control the spacing of lines with three\n")
        stext.insert(Tk.END,  "separate parameters.  \"Spacing1\" tells how much ")
        stext.insert(Tk.END,  "extra space to leave\nabove a line, \"spacing3\" ")
        stext.insert(Tk.END,  "tells how much space to leave below a line,\nand ")
        stext.insert(Tk.END,  "if a text line wraps, \"spacing2\" tells how much ")
        stext.insert(Tk.END,  "space to leave\nbetween the display lines that ")
        stext.insert(Tk.END,  "make up the text line.\n")
        stext.insert(Tk.END,  "These indented paragraphs illustrate how spacing ", "spacing")
        stext.insert(Tk.END,  "can be used.  Each paragraph is actually a ", "spacing")
        stext.insert(Tk.END,  "single line in the text widget, which is ", "spacing")
        stext.insert(Tk.END,  "word-wrapped by the widget.\n", "spacing")
        stext.insert(Tk.END,  "Spacing1 is set to 10 points for this text, ", "spacing")
        stext.insert(Tk.END,  "which results in relatively large gaps between ", "spacing")
        stext.insert(Tk.END,  "the paragraphs.  Spacing2 is set to 2 points, ", "spacing")
        stext.insert(Tk.END,  "which results in just a bit of extra space ", "spacing")
        stext.insert(Tk.END,  "within a pararaph.  Spacing3 isn't used ", "spacing")
        stext.insert(Tk.END,  "in this example.\n", "spacing")
        stext.insert(Tk.END,  "To see where the space is, select ranges of ", "spacing")
        stext.insert(Tk.END,  "text within these paragraphs.  The selection ", "spacing")
        stext.insert(Tk.END,  "highlight will cover the extra space.", "spacing")






##---------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


