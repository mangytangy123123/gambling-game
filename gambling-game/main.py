from tkinter import *
import random
import time
import os

cash = 1000


def winScreen(window,dir):
  picsdir = os.listdir("winpics")
  randnum = random.randint(0,len(picsdir))
  pic = Label(window, image=PhotoImage(file=picsdir[randnum]))
  pic.image = picsdir[randnum]
  pic.pack()
  

def lossScreen(window,dir):
  picsdir = os.listdir("losspics")
  randnum = random.randint(0,len(picsdir)-1)
  imgpath = os.path.join(dir,f"losspics\{picsdir[randnum]}")
  pic = Label(window, image=PhotoImage(file=imgpath))
  pic['image'] = imgpath
  pic.place(x=0,y=0)

def clear_frame(window):
   for widgets in window.winfo_children():
      widgets.destroy()
   print("cleared screen")

def change(coinDisplay,img):
    coinDisplay["image"] = img

def checkWin(bet,cash,coins,window):
    scriptpath = os.path.abspath(__file__) # get the complete absolute path to this script
    scriptdir = os.path.dirname(scriptpath) # strip away the file name
    if bet == coins[-1]:
      print("you won")
      winScreen(window,scriptdir)
    else:
      print("you lost")
      lossScreen(window,scriptdir)


def coinFrame(window,cash,bet):
  def change2():
    coinDisplay.image = randTable[5]
  coinTable = [PhotoImage(file="silvercoin.png"),PhotoImage(file="copper.png"),PhotoImage(file="gold.png")]
  randTable = []
  strtable = []
  for i in range(6):
    randnum = random.randint(0,100)
    randnum2 = random.randint(0,1)
    print(f'{randnum = }')
    if randnum <= 70:
     randTable.append(coinTable[randnum2])
     if randnum2 == 1:
       strtable.append("copper")
     else: strtable.append("silver")
    else:
      randTable.append(coinTable[2])
      strtable.append("gold")
  clear_frame(window)
  mainframe=Frame(window,height=150,width=350)
  mainframe.pack()
  coinDisplay = Label(mainframe,image=randTable[0])
  coinDisplay.grid(row=0,column=0,sticky=N)
  moneyLabel = Label(window,text = f"Money: {cash}")
  moneyLabel.place(x=0,y=0)
  betDisplay = Label(window,text = f"you betted on: {bet}")
  betDisplay.place(x=0,y=30)
  window.after(500,lambda:change(coinDisplay,randTable[0]))
  window.after(1500,lambda:change(coinDisplay,randTable[1]))
  window.after(2500,lambda:change(coinDisplay,randTable[2]))
  window.after(3500,lambda:change(coinDisplay,randTable[3]))
  window.after(4500,lambda:change(coinDisplay,randTable[4]))
  window.after(5500,lambda:change(coinDisplay,randTable[5]))
  window.after(6500,change2)
  Label(mainframe,text=strtable).grid(row=1,column=0)
  window.after(6800,lambda:checkWin(bet,cash,strtable,window))

  
 

def chooseBet(window,cash):
  clear_frame(window)
  mainframe = Frame(window,highlightbackground="black",highlightthickness=2,width=500,height=500)
  Label(window,text="guess which coin").pack()
  copperButton = Button(mainframe,text="copper",command=lambda:coinFrame(window,cash,bet="copper")).grid(row=0,column=0,padx=30)
  goldButton = Button(mainframe,text="gold",command=lambda:coinFrame(window,cash,bet="gold")).grid(row=0,column=1,padx=30)
  silverButton = Button(mainframe,text="silver",command=lambda:coinFrame(window,cash,bet="silver")).grid(row=0,column=2,padx=30)
  mainframe.pack(pady=100)
  
  
def inputCash(window,cash): 
  def getinput(cash):
    def change(label,text):
      label['text'] = text
    val = cashEntry.get()
    try: int(val) 
    except: print("not int")
    else: 
     if cash - int(val) < 0:
       textholder['text'] = "You do not have enough for that."
       window.after(1599,lambda:change(textholder,text="Enter bet amount"))
     else:
        print("is int",cash)
        cash -= int(val)
        cashLabel['text'] = "Money: " + str(cash)
        print("cash after subtract: " + str(cash))
        #coinFrame(window)
        chooseBet(window,cash)
  clear_frame(window)
  cashLabel = Label(window,text="Money: " + str(cash))
  cashLabel.pack()
  container = Frame(window).pack(pady=80)
  textholder = Label(container,text="Enter bet amount.")
  textholder.pack() 
  cashEntry = Entry(container,text="Enter bet")
  cashEntry.pack()  # done in seperate line because cashentry will reutrn as NONE otherwise
  Button(container,text="Enter",command=lambda:getinput(cash)).pack()


window = Tk()
window.geometry("750x400") # 750x400 is for replit 
#lambda:inputCash(window)
Label(window,text="roulette game").pack()
container = Frame(window)
quitButton = Button(container,text="quit?",command=lambda:quit())
playButton = Button(container,text="play!",command=lambda:inputCash(window,cash))
quitButton.grid(row=1)
playButton.grid(row=0)
container.pack(pady=80)
mainloop()