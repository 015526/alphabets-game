# alphabets 2.0
from tkinter import *
from hiragana import *
import random

def otherfunction():
    root.destroy()
    if v.get() == 1:
        print("selected: hiragana")
        hiragana1()
    else:
        print("selected: katakana")
        katakana.xyz
#pick alphabet
def pickalphabet():
    global v
    global root
    colours = ["brown","dark green","pink","purple","blue"]
    root = Tk()
    v = IntVar()
    Label(root,
          text="""pick an alphabet""",
          justify=LEFT,
          padx=20).pack()
    Radiobutton(root, 
                text="hiragana",
                padx = 20, 
                variable=v, 
                value=1).pack(anchor=W)
    Radiobutton(root, 
                text="katakana",
                padx = 20, 
                variable=v, 
                value=2).pack(anchor=W)
    Button(text='ok',
           command=otherfunction).pack()
    Button(text="quit",
           fg=random.choice(colours),
           command=quit).pack()
pickalphabet()
