from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import random


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
         "0-top": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\pipe-green-top.png",
         "0-bottom": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\pipe-green-bottom.png",
         "1-top": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\pipe-red-top.png",
         "1-bottom": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\pipe-red-bottom.png",
         "yellow-heart": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\yellow heart.png",
         "blue-heart": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\blue heart.png",
         "red-heart": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\red heart.png",
         "dead-heart": r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\dead heart.png"}

fps = 60
gameEnd = False
background = [800, 800]
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
history = []
pos = [[100, 100], [100, 200], [100, 300]]

def keyup(e):
    if  e.char in history :
        history.pop(history.index(e.char))

def keydown(e):
    if not e.char in history :
        history.append(e.char)

def selectMapFlappyBird():
    lives = w.get()
    global root, canvas, bg1, bg2, gr1, gr2, yu, ym, yd, bu, bm, bd, ru, rm, rd, top1, top2, top3, bottom1, bottom2, bottom3, yh, bh, rh, dyh, dbh, drh, ty, tb, tr
    yh = bh = rh = dyh = dbh = drh = []
    if data[0].get() == "None" and data[1].get() == "None" and data[2].get() == "None": return()
    root.destroy()
    root = Tk()
    root.focus_force()
    root.geometry("800x750")
    root.title("Flappy Bird")
    root.resizable(False, False)
    Scores = Canvas(root, width=800, height=150)
    Scores.pack()
    Scores.configure(bg='white')
    canvas = Canvas(root, width = 800, height = 600)
    canvas.pack()
    if bool(data[6].get()):
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
    yuPath = Image.open(paths["yellowBirdUpflap"])
    ymPath = Image.open(paths["yellowBirdmidflap"])
    ydPath = Image.open(paths["yellowBirdDownflap"])
    buPath = Image.open(paths["blueBirdUpflap"])
    bmPath = Image.open(paths["blueBirdmidflap"])
    bdPath = Image.open(paths["blueBirdDownflap"])
    ruPath = Image.open(paths["redBirdUpflap"])
    rmPath = Image.open(paths["redBirdmidflap"])
    rdPath = Image.open(paths["redBirdDownflap"])
    yhPath = Image.open(paths["yellow-heart"])
    bhPath = Image.open(paths["blue-heart"])
    rhPath = Image.open(paths["red-heart"])
    dhPath = Image.open(paths["dead-heart"])
    topPath = Image.open(paths[str(data[5].get())+"-top"])
    bottomPath = Image.open(paths[str(data[5].get())+"-bottom"])
    yuImg = ImageTk.PhotoImage(yuPath)
    ymImg = ImageTk.PhotoImage(ymPath)
    ydImg = ImageTk.PhotoImage(ydPath)
    buImg = ImageTk.PhotoImage(buPath)
    bmImg = ImageTk.PhotoImage(bmPath)
    bdImg = ImageTk.PhotoImage(bdPath)
    ruImg = ImageTk.PhotoImage(ruPath)
    rmImg = ImageTk.PhotoImage(rmPath)
    rdImg = ImageTk.PhotoImage(rdPath)
    yhImg = ImageTk.PhotoImage(yhPath)
    bhImg = ImageTk.PhotoImage(bhPath)
    rhImg = ImageTk.PhotoImage(rhPath)
    dhImg = ImageTk.PhotoImage(dhPath)
    topImg = ImageTk.PhotoImage(topPath)
    bottomImg = ImageTk.PhotoImage(bottomPath)
    for i in range(lives):
        if data[0].get() != "None":
            if i < 5:
                yh.append(Scores.create_image(i*40+20, 10, image = yhImg, anchor="nw"))
            else:
                yh.append(Scores.create_image(i*40-180, 50, image = yhImg, anchor="nw"))
            ty = Scores.create_text(20, 100, text="Score: 0", fill="black", anchor="nw", font="rockwell 25 bold")
        if data[1].get() != "None":
            if i < 5:
                bh.append(Scores.create_image(i*40+280, 10, image = bhImg, anchor="nw"))
            else:
                bh.append(Scores.create_image(i*40+80, 50, image = bhImg, anchor="nw"))
            tb = Scores.create_text(280, 100, text="Score: 0", fill="black", anchor="nw", font="rockwell 25 bold")
        if data[2].get() != "None":
            if i < 5:
                rh.append(Scores.create_image(i*40+560, 10, image = rhImg, anchor="nw"))
            else:
                rh.append(Scores.create_image(i*40+360, 50, image = rhImg, anchor="nw"))
            tr = Scores.create_text(560, 100, text="Score: 0", fill="black", anchor="nw", font="rockwell 25 bold")
        bh.append(Scores.create_image(1000, 1000, image = bhImg, anchor="nw"))
        rh.append(Scores.create_image(1000, 1000, image = rhImg, anchor="nw"))
        dyh.append(Scores.create_image(1000, 1000, image = dhImg, anchor="nw"))
        dbh.append(Scores.create_image(1000, 1000, image = dhImg, anchor="nw"))
        drh.append(Scores.create_image(1000, 1000, image = dhImg, anchor="nw"))
    yu = canvas.create_image(1000, 1000, image = yuImg, anchor="nw")
    ym = canvas.create_image(1000, 1000, image = ymImg, anchor="nw")
    yd = canvas.create_image(1000, 1000, image = ydImg, anchor="nw")
    bu = canvas.create_image(1000, 1000, image = buImg, anchor="nw")
    bm = canvas.create_image(1000, 1000, image = bmImg, anchor="nw")
    bd = canvas.create_image(1000, 1000, image = bdImg, anchor="nw")
    ru = canvas.create_image(1000, 1000, image = ruImg, anchor="nw")
    rm = canvas.create_image(1000, 1000, image = rmImg, anchor="nw")
    rd = canvas.create_image(1000, 1000, image = rdImg, anchor="nw")
    top1 = canvas.create_image(1000, 1000, image = topImg, anchor="nw")
    top2 = canvas.create_image(1000, 1000, image = topImg, anchor="nw")
    top3 = canvas.create_image(1000, 1000, image = topImg, anchor="nw")
    bottom1 = canvas.create_image(1000, 1000, image = bottomImg, anchor="nw")
    bottom2 = canvas.create_image(1000, 1000, image = bottomImg, anchor="nw")
    bottom3 = canvas.create_image(1000, 1000, image = bottomImg, anchor="nw")
    #root.config(cursor="none")
    #root.bind('<Motion>', motion)
    root.bind("<KeyPress>", keydown)
    root.bind("<KeyRelease>", keyup)
    update_window()
    root.mainloop()


def update_window():
    global background, flapStage, mode, pos
    root.after(int(1000/fps), update_window)
    #print(history)
    for item in history:
        #print(item)
        if data[0].get() != "None":
            if item == "w": pos[0][1] -= sensitivities[options.index(data[0].get())]
            elif item == "a": pos[0][0] -= sensitivities[options.index(data[0].get())]
            elif item == "s": pos[0][1] += sensitivities[options.index(data[0].get())]
            elif item == "d": pos[0][0] += sensitivities[options.index(data[0].get())]
        if data[1].get() != "None":
            if item == "t": pos[1][1] -= sensitivities[options.index(data[1].get())]
            elif item == "f": pos[1][0] -= sensitivities[options.index(data[1].get())]
            elif item == "g": pos[1][1] += sensitivities[options.index(data[1].get())]
            elif item == "h": pos[1][0] += sensitivities[options.index(data[1].get())]
        if data[2].get() != "None":
            if item == "i": pos[2][1] -= sensitivities[options.index(data[2].get())]
            elif item == "j": pos[2][0] -= sensitivities[options.index(data[2].get())]
            elif item == "k": pos[2][1] += sensitivities[options.index(data[2].get())]
            elif item == "l": pos[2][0] += sensitivities[options.index(data[2].get())]
    if flapStage == 0:
        if data[0].get() != "None":
            canvas.moveto(yu, pos[0][0], pos[0][1])
            canvas.moveto(ym, 1000, 1000)
        if data[1].get() != "None":
            canvas.moveto(bm, pos[1][0], pos[1][1])
            canvas.moveto(bd, 1000, 1000)
        if data[2].get() != "None":
            canvas.moveto(rm, 1000, 1000)
            canvas.moveto(rd, pos[2][0], pos[2][1])
    elif flapStage == 1:
        if data[0].get() != "None":
            canvas.moveto(yu, 1000, 1000)
            canvas.moveto(ym, pos[0][0], pos[0][1])
        if data[1].get() != "None":
            canvas.moveto(bu, pos[1][0], pos[1][1])
            canvas.moveto(bm, 1000, 1000)
        if data[2].get() != "None":
            canvas.moveto(rm, pos[2][0], pos[2][1])
            canvas.moveto(rd, 1000, 1000)
    elif flapStage == 2:
        if data[0].get() != "None":
            canvas.moveto(ym, 1000, 1000)
            canvas.moveto(yd, pos[0][0], pos[0][1])
        if data[1].get() != "None":
            canvas.moveto(bu, 1000, 1000)
            canvas.moveto(bm, pos[1][0], pos[1][1])
        if data[2].get() != "None":
            canvas.moveto(ru, pos[2][0], pos[2][1])
            canvas.moveto(rm, 1000, 1000)
    elif flapStage == 3:
        if data[0].get() != "None":
            canvas.moveto(ym, pos[0][0], pos[0][1])
            canvas.moveto(yd, 1000, 1000)
        if data[1].get() != "None":
            canvas.moveto(bm, 1000, 1000)
            canvas.moveto(bd, pos[1][0], pos[1][1])
        if data[2].get() != "None":
            canvas.moveto(ru, 1000, 1000)
            canvas.moveto(rm, pos[2][0], pos[2][1])
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
        ##print(mode)




root = Tk()
root.geometry("335x240")
options = ["Slow", "Regular", "Fast", "None"]
sensitivities = [3, 4, 5]
data = [StringVar(value="None"), StringVar(value="None"), StringVar(value="None"), IntVar(value=0), IntVar(value=1), IntVar(value=1), IntVar(value=0)]
root.title("Settings")
root.resizable(False, False)
Label(root, text="Yellow Bird (WASDZ)", bg="lightyellow", width=30).grid(row=0, column=0, columnspan=2)
OptionMenu(root, data[0], *options).grid(row=0, column=2)
Label(root, text="Blue Bird (TFGHV)", bg="lightblue", width=30).grid(row=1, column=0, columnspan=2)
OptionMenu(root, data[1], *options).grid(row=1, column=2)
Label(root, text="Red Bird (IJKLM)", bg="pink", width=30).grid(row=2, column=0, columnspan=2)
OptionMenu(root, data[2], *options).grid(row=2, column=2)
Checkbutton(root, text="Death on collision", variable=data[3], onvalue=1, offvalue=0).grid(row=3, column=0)
Checkbutton(root, text="Deadly poop laser", variable=data[4], onvalue=1, offvalue=0).grid(row=3, column=1)
Label(root, text="Lives").grid(row=4, column=0)
w = Scale(root, from_=1, to=10, orient=HORIZONTAL, length=130)
w.grid(row=4, column=1, columnspan=1)
Radiobutton(root, text='Green', variable=data[5], value=0).grid(row=5, column=0)
Radiobutton(root, text='Red', variable=data[5], value=1).grid(row=5, column=1)
Radiobutton(root, text='Dark', variable=data[6], value=0).grid(row=6, column=0)
Radiobutton(root, text='Light', variable=data[6], value=1).grid(row=6, column=1)
Button(root, text="Play", command=selectMapFlappyBird, width=45).grid(row=7, column=0, columnspan=3)

root.mainloop()