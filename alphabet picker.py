from tkinter import *
import random
global count
count = 0

hiragana_alpha = {"あ":"a","い":"i","う":"u","え":"e","お":"o",
            "か":"ka","き":"ki","く":"ku","け":"ke","こ":"ko",
            "さ":"sa","し":"shi","す":"su","せ":"se","そ":"so",}

def otherfunction():
    if v.get() == 1:
        print("selected: hiragana")
        hiragana(hiragana_alpha)
    else:
        print("fears: confirmed")

def counter(count):
    count =+ 1

def hiragana(hiragana):
    root = Tk()
    Label(root,text=random.choice(list(hiragana.keys())),height=1,width=16,fg="black",font="Times").pack()
    counter(counter)
    
#pick alphabet
def pickalphabet():
    global v
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

    Button(text="quit",
           fg=random.choice(colours),
           command=quit).pack()
    Button(text='ok',
           command=otherfunction).pack()
pickalphabet()
