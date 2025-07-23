from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import random

titles = ["Flappy Bird", "Aztec", "Balls"]
paths = {"bgDay": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\background-day.png",
         "bgNight": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\background-night.png",
         "redBirdUpflap": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\redbird-upflap.png",
         "redBirdmidflap": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\redbird-midflap.png",
         "redBirdDownflap": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\redbird-downflap.png",
         "blueBirdUpflap": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\bluebird-upflap.png",
         "blueBirdmidflap": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\bluebird-midflap.png",
         "blueBirdDownflap": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\bluebird-downflap.png",
         "yellowBirdUpflap": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\yellowbird-upflap.png",
         "yellowBirdmidflap": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\yellowbird-midflap.png",
         "yellowBirdDownflap": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\yellowbird-downflap.png",
         "base": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\base.png",
         "green-top": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\pipe-green-top.png",
         "green-bottom": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\pipe-green-bottom.png",
         "red-top": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\pipe-red-top.png",
         "red-bottom": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\pipe-red-bottom.png"}
bird = "red"
pipe = "red"
fps = 60
gameEnd = False
background = [800, 800]
cursor = [100, 100]
flapStage = 0
pipes = [2000, 2000, 2000, 0, 0, 0]
begin = True
mode = 0
order = [[0, 0, 1, 2, 3],
         [0, 0, 1, 2, 3],
         [1, 2, 3, 0, 0],
         [0, 2, 3, 1, 0],
         [3, 1, 2, 0, 0],
         [0, 1, 2, 3, 0],
         [2, 3, 1, 0, 0],
         [0, 3, 1, 2, 0]]

def selectMapFlappyBird():
    global root, canvas, bg1, bg2, gr1, gr2, up, mid, down, top1, top2, top3, bottom1, bottom2, bottom3
    root.destroy()
    root = Tk()
    root.geometry("800x600")
    root.title("Flappy Bird")
    root.resizable(False, False)
    canvas = Canvas(root, width = 800, height = 600)
    canvas.pack()
    light = messagebox.askyesno(title=None, message="Use light theme?")
    if light:
        bgPath = Image.open(paths["bgDay"])
    else:
        bgPath = Image.open(paths["bgNight"])
    grPath = Image.open(paths["base"])
    bgImg = ImageTk.PhotoImage(bgPath)
    grImg = ImageTk.PhotoImage(grPath)
    bg1 = canvas.create_image(0, 0, image = bgImg, anchor="nw")
    bg2 = canvas.create_image(0, 0, image = bgImg, anchor="nw")
    gr1 = canvas.create_image(0, 500, image = grImg, anchor="nw")
    gr2 = canvas.create_image(0, 500, image = grImg, anchor="nw")
    messagebox.showinfo(title=None, message="Click to start")
    upPath = Image.open(paths[bird+"BirdUpflap"])
    midPath = Image.open(paths[bird+"Birdmidflap"])
    downPath = Image.open(paths[bird+"BirdDownflap"])
    topPath = Image.open(paths[pipe+"-top"])
    bottomPath = Image.open(paths[pipe+"-bottom"])
    upImg = ImageTk.PhotoImage(upPath)
    midImg = ImageTk.PhotoImage(midPath)
    downImg = ImageTk.PhotoImage(downPath)
    topImg = ImageTk.PhotoImage(topPath)
    bottomImg = ImageTk.PhotoImage(bottomPath)
    up = canvas.create_image(100, 300, image = upImg, anchor="nw")
    mid = canvas.create_image(1000, 1000, image = midImg, anchor="nw")
    down = canvas.create_image(1000, 1000, image = downImg, anchor="nw")
    top1 = canvas.create_image(1000, 1000, image = topImg, anchor="nw")
    top2 = canvas.create_image(1000, 1000, image = topImg, anchor="nw")
    top3 = canvas.create_image(1000, 1000, image = topImg, anchor="nw")
    bottom1 = canvas.create_image(1000, 1000, image = bottomImg, anchor="nw")
    bottom2 = canvas.create_image(1000, 1000, image = bottomImg, anchor="nw")
    bottom3 = canvas.create_image(1000, 1000, image = bottomImg, anchor="nw")
    root.config(cursor="none")
    #root.bind('<Motion>', motion)
    root.bind("<Button-1>", start)
    root.bind("w", p1w)
    root.bind("a", p1a)
    root.bind("s", p1s)
    root.bind("d", p1d)
    update_window()
    root.mainloop()


def update_window():
    global background, flapStage, mode
    print(cursor)
    if flapStage == 0:
        canvas.moveto(up, cursor[0], cursor[1])
        canvas.moveto(mid, 1000, 1000)
    elif flapStage == 1:
        canvas.moveto(up, 1000, 1000)
        canvas.moveto(mid, cursor[0], cursor[1])
    elif flapStage == 2:
        canvas.moveto(mid, 1000, 1000)
        canvas.moveto(down, cursor[0], cursor[1])
    elif flapStage == 3:
        canvas.moveto(mid, cursor[0], cursor[1])
        canvas.moveto(down, 1000, 1000)
        flapStage = -1
    if background[0] % 4 == 0:
        flapStage += 1
    canvas.moveto(bg1, background[0], 0)
    canvas.moveto(bg2, background[0]-800, 0)
    canvas.moveto(gr1, background[1], 500)
    canvas.moveto(gr2, background[1]-800, 500)
    background[0] -= 1
    background[1] -= 4
    if background[0] == 0:
        background[0] = 800
    if background[1] == 0:
        background[1] = 800
    if begin:
        if pipes[0] == 2000 :
            pipes[0] = random.randint(-620, -300)
            pipes[1] = random.randint(-620, -300)
            pipes[2] = random.randint(-620, -300)
            pipes[3] = random.randint(700, 840)
            pipes[4] = random.randint(700, 840)
            pipes[5] = random.randint(700, 840)
        array = order[mode]
        canvas.moveto(top1, background[1]-800+400*array.index(1), pipes[0])
        canvas.moveto(top2, background[1]-800+400*array.index(2), pipes[1])
        canvas.moveto(top3, background[1]-800+400*array.index(3), pipes[2])
        canvas.moveto(bottom1, background[1]-800+400*array.index(1), pipes[0]+pipes[3])
        canvas.moveto(bottom2, background[1]-800+400*array.index(2), pipes[1]+pipes[4])
        canvas.moveto(bottom3, background[1]-800+400*array.index(3), pipes[2]+pipes[5])
        if background[1] % 400 == 0:
            mode += 1
            if mode == 3:
                pipes[0] = random.randint(-620, -300)
            elif mode == 5:
                pipes[2] = random.randint(-620, -300)
            elif mode == 7:
                pipes[1] = random.randint(-620, -300)
            if mode == len(order):
                mode = 2
        #print(mode)
    root.after(int(1000/fps), update_window)

def start(event):
    global begin
    begin = True
    #print(event)

def selectMapAztec(): 
    global map
    map = 2

def p1w(event):
    global cursor
    cursor[1] -= 10
def p1a(event):
    global cursor
    cursor[0] -= 10
def p1s(event):
    global cursor
    cursor[1] += 10
def p1d(event):
    global cursor
    cursor[0] += 10

def motion(event):
    global cursor
    x, y = event.x, event.y
    cursor = [x-27, y-22]
    if flapStage == 0:
        canvas.moveto(up, cursor[0], cursor[1])
        canvas.moveto(mid, 1000, 1000)
    elif flapStage == 1:
        canvas.moveto(up, 1000, 1000)
        canvas.moveto(mid, cursor[0], cursor[1])
    elif flapStage == 2:
        canvas.moveto(mid, 1000, 1000)
        canvas.moveto(down, cursor[0], cursor[1])
    elif flapStage == 3:
        canvas.moveto(mid, cursor[0], cursor[1])
        canvas.moveto(down, 1000, 1000)
    #canvas.moveto(img, x-27, y-22)
    #print('{}, {}'.format(x, y))

root = Tk()
root.title("Mode Select")
Button(root, text="Flappy Bird", command=selectMapFlappyBird, width=30).pack()
Button(root, text="Aztec", command=selectMapAztec, width=30).pack()

root.mainloop()