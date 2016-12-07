from tkinter import *
import random, sys, alphabets
count = 0
correct = 0
hiraganaAl = {"あ":"a","い":"i","う":"u","え":"e","お":"o",
            "か":"ka","き":"ki","く":"ku","け":"ke","こ":"ko",
            "さ":"sa","し":"shi","す":"su","せ":"se","そ":"so",}
def give_score():
    root = Tk()
    score = "congratulations, you scored",correct,"out of 10"
    Label(root,text=score,fg="red",font="Times 20").pack()
    Button(root,text="thanks for that i would like to leave this application now",command=quit).pack()
    Button(root,text="thanks for that i would like to play again",command=alphabets)
def counter():
    global count
    count+=1
    print(count)
    if count == 10:
        give_score()
        root.destroy()
    else:
        root.destroy()
        hiragana1()

def check():
    global correct
    print(entry.get())
    if entry.get() == hiraganaAl[x]:
        Label(root,text=answer,fg="red").pack()
        print("correct!")
        correct+=1
        counter()
        #root.destroy()
    else:
        print("not quite right...")
        counter()

def hint():
    global hinted
    if not hinted: #check if the hint is already being displayed
        hinted = True
        global answer
        answer = "sneaky-peak:",hiraganaAl[x] #answer is not definied
        Label(root,text=answer,fg="red").pack()
    
def hiragana1():
    global hinted
    global entry
    global x
    global root
    root = Tk()
    Label(root,text="""fill in the box below with the correct letter!\nif you need help, click the hint box.\nwhen you are sure of your answer, click 'okay'""",
          fg="blue",font="Times 12 italic").pack()
    x = random.choice(list(hiraganaAl.keys()))
    Label(root,text=x,height=1,width=16,fg="black",font="\"Comic Sans MS\" 50 bold").pack()
    hinted = False
    #entry and OK button
    entry=Entry(root)
    entry.pack()
    Button(root,text='ok',command=check).pack()
    #hint button
    Button(root,text='show me a hint',command=hint).pack()
