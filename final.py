from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import random



paths = {"bgDay": r"Collision game/FlappyBirdSprites/background-day.png",
         "bgNight": r"Collision game/FlappyBirdSprites/background-night.png",
         "redBirdUpflap": r"Collision game/FlappyBirdSprites/redbird-upflap.png",
         "redBirdmidflap": r"Collision game/FlappyBirdSprites/redbird-midflap.png",
         "redBirdDownflap": r"Collision game/FlappyBirdSprites/redbird-downflap.png",
         "blueBirdUpflap": r"Collision game/FlappyBirdSprites/bluebird-upflap.png",
         "blueBirdmidflap": r"Collision game/FlappyBirdSprites/bluebird-midflap.png",
         "blueBirdDownflap": r"Collision game/FlappyBirdSprites/bluebird-downflap.png",
         "yellowBirdUpflap": r"Collision game/FlappyBirdSprites/yellowbird-upflap.png",
         "yellowBirdmidflap": r"Collision game/FlappyBirdSprites/yellowbird-midflap.png",
         "yellowBirdDownflap": r"Collision game/FlappyBirdSprites/yellowbird-downflap.png",
         "base": r"Collision game/FlappyBirdSprites/base.png",
         "0-top": r"Collision game/FlappyBirdSprites/pipe-green-top.png",
         "0-bottom": r"Collision game/FlappyBirdSprites/pipe-green-bottom.png",
         "1-top": r"Collision game/FlappyBirdSprites/pipe-red-top.png",
         "1-bottom": r"Collision game/FlappyBirdSprites/pipe-red-bottom.png",
         "yellow-heart": r"Collision game/FlappyBirdSprites/yellow heart.png",
         "blue-heart": r"Collision game/FlappyBirdSprites/blue heart.png",
         "red-heart": r"Collision game/FlappyBirdSprites/red heart.png",
         "dead-heart": r"Collision game/FlappyBirdSprites/dead heart.png",
         "grave": r"Collision game/FlappyBirdSprites/grave.png",
         "poop": r"Collision game/FlappyBirdSprites/egg.png"}

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
prev_hits = [0, 0, 0]
hits = [0, 0, 0]
history = []
pos = [[100, 100], [100, 200], [100, 300]]
poops = []
pospoops = []
eggspeed = 20
def keyup(e):
    if  e.char in history :
        history.pop(history.index(e.char))

def keydown(e):
    if not e.char in history :
        history.append(e.char)

def circleLineIntersect(xcentre, ycentre, xradius, yradius, xline=False, yline=False):
    if xline and (yradius*yradius)*(1-((xline-xcentre)*(xline-xcentre))/(xradius*xradius))>=0 or yline and (xradius*xradius)*(1-((yline-ycentre)*(yline-ycentre))/(yradius*yradius))>=0:
        return(True)
    return(False)

def selectMapFlappyBird():
    if data[0].get() == "None" and data[1].get() == "None" and data[2].get() == "None": return()
    global root, canvas, bg1, bg2, gr1, gr2, yu, ym, yd, bu, bm, bd, ru, rm, rd, top1, top2, top3, bottom1, bottom2, bottom3, yh, bh, rh, dyh, dbh, drh, sy, sb, sr, Hearts, Scores, lives, Lives, deathStage, graves
    graves = []
    Lives = [int(w.get()), int(w.get()), int(w.get())]
    deathStage = [0, 0, 0]
    lives = w.get()
    root.destroy()
    root = Tk()
    root.focus_force()
    root.geometry("800x750")
    root.title("Flappy Bird")
    #root.resizable(False, False)
    Scores = [StringVar(), StringVar(), StringVar()]
    sy = Label(root, textvariable = Scores[0], font="rockwell 20 bold")
    sb = Label(root, textvariable = Scores[1], font="rockwell 20 bold")
    sr = Label(root, textvariable = Scores[2], font="rockwell 20 bold")
    sy.grid(row=0, column=0)
    sb.grid(row=0, column=1)
    sr.grid(row=0, column=2)
    yh = []
    bh = []
    rh = []
    dyh = []
    dbh = []
    drh = []
    Hearts = Canvas(root, width=800, height=100)
    Hearts.grid(row=1, column=0, columnspan=3)
    Hearts.configure(bg='white')
    canvas = Canvas(root, width = 800, height = 600)
    canvas.grid(row=2, column=0, columnspan=3)
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
    gvPath = Image.open(paths["grave"])
    poPath = Image.open(paths["poop"])
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
    gvImg = ImageTk.PhotoImage(gvPath)
    poImg = ImageTk.PhotoImage(poPath)
    for i in range(3):
        graves.append(canvas.create_image(1000, 1000, image = gvImg, anchor="nw"))
    for i in range(lives):
        if data[0].get() != "None":
            if i < 5:
                yh.append(Hearts.create_image(i*40+20, 10, image = yhImg, anchor="nw"))
            else:
                yh.append(Hearts.create_image(i*40-180, 50, image = yhImg, anchor="nw"))
            dyh.append(Hearts.create_image(1000, 1000, image = dhImg, anchor="nw"))
            Scores[0].set("Score: 0")
        if data[1].get() != "None":
            if i < 5:
                bh.append(Hearts.create_image(i*40+280, 10, image = bhImg, anchor="nw"))
            else:
                bh.append(Hearts.create_image(i*40+80, 50, image = bhImg, anchor="nw"))
            dbh.append(Hearts.create_image(1000, 1000, image = dhImg, anchor="nw"))
            Scores[1].set("Score: 0")
        if data[2].get() != "None":
            if i < 5:
                rh.append(Hearts.create_image(i*40+560, 10, image = rhImg, anchor="nw"))
            else:
                rh.append(Hearts.create_image(i*40+360, 50, image = rhImg, anchor="nw"))
            drh.append(Hearts.create_image(1000, 1000, image = dhImg, anchor="nw"))
            Scores[2].set("Score: 0")
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
    for i in range(3):
        poops.append(canvas.create_image(-1000, 0, image = poImg, anchor = "nw"))
        pospoops.append([-1000, 0])
    #root.config(cursor="none")
    #root.bind('<Motion>', motion)
    root.bind("<KeyPress>", keydown)
    root.bind("<KeyRelease>", keyup)
    update_window()
    root.mainloop()


def update_window():
    global background, flapStage, mode, pos, hits, deathStage
    root.after(int(1000/fps), update_window)
    #print(history)
    
    array = order[mode]
    for item in history:
        #print(item)
        if data[0].get() != "None" and Lives[0] != 0:
            if item == "w": pos[0][1] -= sensitivities[options.index(data[0].get())]
            elif item == "a": pos[0][0] -= sensitivities[options.index(data[0].get())]
            elif item == "s": pos[0][1] += sensitivities[options.index(data[0].get())]
            elif item == "d": pos[0][0] += sensitivities[options.index(data[0].get())]
            elif item == "z" and pospoops[0][0] < -40 and data[0] != "None" and Lives[0]>0 and bool(data[4].get()):
                canvas.moveto(poops[0], pos[0][0]-40, pos[0][1]+20)
                pospoops[0][0] = pos[0][0]-40
                pospoops[0][1] = pos[0][1]+20
        if data[1].get() != "None" and Lives[1] != 0:
            if item == "t": pos[1][1] -= sensitivities[options.index(data[1].get())]
            elif item == "f": pos[1][0] -= sensitivities[options.index(data[1].get())]
            elif item == "g": pos[1][1] += sensitivities[options.index(data[1].get())]
            elif item == "h": pos[1][0] += sensitivities[options.index(data[1].get())]
            elif item == "v" and pospoops[1][0] < -40 and data[1] != "None" and Lives[1]>0 and bool(data[4].get()):
                canvas.moveto(poops[1], pos[1][0]-40, pos[1][1]+20)
                pospoops[1][0] = pos[1][0]-40
                pospoops[1][1] = pos[1][1]+20
        if data[2].get() != "None" and Lives[2] != 0:
            if item == "i": pos[2][1] -= sensitivities[options.index(data[2].get())]
            elif item == "j": pos[2][0] -= sensitivities[options.index(data[2].get())]
            elif item == "k": pos[2][1] += sensitivities[options.index(data[2].get())]
            elif item == "l": pos[2][0] += sensitivities[options.index(data[2].get())]
            elif item == "m" and pospoops[2][0] < -40 and data[2] != "None" and Lives[2]>0 and bool(data[4].get()):
                canvas.moveto(poops[2], pos[2][0]-40, pos[2][1]+20)
                pospoops[2][0] = pos[2][0]-40
                pospoops[1][1] = pos[1][1]+20
    if mode > 0:
        if data[0].get() != "None":
            prev_hits[0] = hits[0]
            hits[0] = 0
            a = background[1]
            b = (a+400)%800
            if deathStage[0] == 0 and Lives[0] != 0:
                if pos[0][0] < 0 or pos[0][1]<0 or pos[0][0] > 770 or pos[0][1] > 476:
                    hits[0] = 1
                if pos[0][0]>a and pos[0][0]<a+104 or pos[0][0]+60>a and pos[0][0]+60<a+104 or pos[0][0]>b and pos[0][0]<b+104 or pos[0][0]+60>b and pos[0][0]+60<b+104 or ((pos[0][0]-pos[1][0])*(pos[0][0]-pos[1][0])+(pos[0][1]-pos[1][1])*(pos[0][1]-pos[1][1])<48*48 or (pos[0][0]-pos[2][0])*(pos[0][0]-pos[2][0])+(pos[0][1]-pos[2][1])*(pos[0][1]-pos[2][1])<48*48) and bool(data[3].get()) or ((pos[0][0]-pospoops[1][0])*(pos[0][0]-pospoops[1][0])+(pos[0][1]-pospoops[1][1])*(pos[0][1]-pospoops[2][1])<48*48 or (pos[0][0]-pospoops[2][0])*(pos[0][0]-pospoops[2][0])+(pos[0][1]-pospoops[2][1])*(pos[0][1]-pospoops[2][1])<48*48) and bool(data[4].get()):
                    c = [pipes[order[mode][1+mode%2]-1]+640, pipes[order[mode][2+mode%2]-1]+640]
                    d = [pipes[order[mode][1+mode%2]-1]+pipes[order[mode][1+mode%2]+2], pipes[order[mode][2+mode%2]-1]+pipes[order[mode][2+mode%2]+2]]
                    if pos[0][0] < 401:
                        if pos[0][1] < c[0] or pos[0][1]+48 > d[0]:
                            hits[0] = 1
                    else:
                        if pos[0][1] < c[1]or pos[0][1]+48 > d[1]:
                            hits[0] = 1
            elif deathStage[0] == fps * 2:
                deathStage[0] = 0
            if hits[0] == 1 and prev_hits[0] == 1 or deathStage[0] > 0:
                if deathStage[0] == 0:
                    deathStage[0] += 1
                    Lives[0] -= 1
                if deathStage[0] != 0:
                    deathStage[0] += 1
                    a = deathStage[0] % 40
                    b = Lives[0]
                    if a < 20:
                        if b < 5:
                            Hearts.moveto(yh[b], 1000, 1000)
                            Hearts.moveto(dyh[b], b*40+20, 10)
                        else:
                            Hearts.moveto(yh[b], 1000, 1000)
                            Hearts.moveto(dyh[b], b*40-180, 50)
                    else:
                        if b < 5:
                            Hearts.moveto(yh[b], b*40+20, 10)
                            Hearts.moveto(dyh[b], 1000, 1000)
                        else:
                            Hearts.moveto(yh[b], b*40-180, 50)
                            Hearts.moveto(dyh[b], 1000, 1000)
                    if Lives[0] == 0:
                        canvas.moveto(ym, 1000, 1000)
                        canvas.moveto(yd, 1000, 1000)
                        if pos[0][1] <= 540:
                            pos[0][1] += 10
                        elif pos[0][1] < 550:
                            pos[0][1] = 550
                        elif pos[0][1] == 550:
                            canvas.moveto(graves[0], pos[0][0]-5, 450)
        if data[1].get() != "None":
            prev_hits[1] = hits[1]
            hits[1] = 0
            a = background[1]
            b = (a+400)%800
            if deathStage[1] == 0 and Lives[1] != 0:
                if pos[1][0] < 0 or pos[1][1]<0 or pos[1][0] > 770 or pos[1][1] > 476:
                    hits[1] = 1
                if pos[1][0]>a and pos[1][0]<a+104 or pos[1][0]+60>a and pos[1][0]+60<a+104 or pos[1][0]>b and pos[1][0]<b+104 or pos[1][0]+60>b and pos[1][0]+60<b+104 or ((pos[0][0]-pos[1][0])*(pos[0][0]-pos[1][0])+(pos[0][1]-pos[1][1])*(pos[0][1]-pos[1][1])<48*48 or (pos[1][0]-pos[2][0])*(pos[1][0]-pos[2][0])+(pos[1][1]-pos[2][1])*(pos[1][1]-pos[2][1])<48*48) and bool(data[3].get()) or ((pos[1][0]-pospoops[0][0])*(pos[1][0]-pospoops[0][0])+(pos[1][1]-pospoops[0][1])*(pos[1][1]-pospoops[0][1])<48*48 or (pos[1][0]-pospoops[2][0])*(pos[1][0]-pospoops[2][0])+(pos[1][1]-pospoops[2][1])*(pos[1][1]-pospoops[2][1])<48*48) and bool(data[4].get()):
                    c = [pipes[order[mode][1+mode%2]-1]+640, pipes[order[mode][2+mode%2]-1]+640]
                    d = [pipes[order[mode][1+mode%2]-1]+pipes[order[mode][1+mode%2]+2], pipes[order[mode][2+mode%2]-1]+pipes[order[mode][2+mode%2]+2]]
                    if pos[1][0] < 401:
                        if pos[1][1] < c[0] or pos[1][1]+48 > d[0]:
                            hits[1] = 1
                    else:
                        if pos[1][1] < c[1]or pos[1][1]+48 > d[1]:
                            hits[1] = 1
            elif deathStage[1] == fps * 2:
                deathStage[1] = 0
            if hits[1] == 1 and prev_hits[1] == 1 or deathStage[1] > 0:
                if deathStage[1] == 0:
                    deathStage[1] += 1
                    Lives[1] -= 1
                if deathStage[1] != 0:
                    deathStage[1] += 1
                    a = deathStage[1] % 40
                    b = Lives[1]
                    if a < 20:
                        if b < 5:
                            Hearts.moveto(bh[b], 1000, 1000)
                            Hearts.moveto(dbh[b], b*40+280, 10)
                        else:
                            Hearts.moveto(bh[b], 1000, 1000)
                            Hearts.moveto(dbh[b], b*40+80, 50)
                    else:
                        if b < 5:
                            Hearts.moveto(bh[b], b*40+280, 10)
                            Hearts.moveto(dbh[b], 1000, 1000)
                        else:
                            Hearts.moveto(bh[b], b*40+80, 50)
                            Hearts.moveto(dbh[b], 1000, 1000)
                    if Lives[1] == 0:
                        canvas.moveto(bm, 1000, 1000)
                        canvas.moveto(bd, 1000, 1000)
                        if pos[1][1] <= 540:
                            pos[1][1] += 10
                        elif pos[1][1] < 550:
                            pos[1][1] = 550
                        elif pos[1][1] == 550:
                            canvas.moveto(graves[1], pos[1][0]-5, 450)
        if data[2].get() != "None":
            prev_hits[2] = hits[2]
            hits[2] = 0
            a = background[1]
            b = (a+400)%800
            if deathStage[2] == 0 and Lives[2] != 0:
                if pos[2][0] < 0 or pos[2][1]<0 or pos[2][0] > 770 or pos[2][1] > 476:
                    hits[2] = 1
                if pos[2][0]>a and pos[2][0]<a+104 or pos[2][0]+60>a and pos[2][0]+60<a+104 or pos[2][0]>b and pos[2][0]<b+104 or pos[2][0]+60>b and pos[2][0]+60<b+104 or ((pos[0][0]-pos[2][0])*(pos[0][0]-pos[2][0])+(pos[0][1]-pos[2][1])*(pos[0][1]-pos[2][1])<48*48 or (pos[1][0]-pos[2][0])*(pos[1][0]-pos[2][0])+(pos[1][1]-pos[2][1])*(pos[1][1]-pos[2][1])<48*48) and bool(data[3].get()) or ((pos[2][0]-pospoops[0][0])*(pos[2][0]-pospoops[0][0])+(pos[2][1]-pospoops[0][1])*(pos[2][1]-pospoops[0][1])<48*48 or (pos[2][1]-pospoops[2][0])*(pos[2][1]-pospoops[2][0])+(pos[2][1]-pospoops[2][1])*(pos[2][1]-pospoops[2][1])<48*48) and bool(data[4].get()):
                    c = [pipes[order[mode][1+mode%2]-1]+640, pipes[order[mode][2+mode%2]-1]+640]
                    d = [pipes[order[mode][1+mode%2]-1]+pipes[order[mode][1+mode%2]+2], pipes[order[mode][2+mode%2]-1]+pipes[order[mode][2+mode%2]+2]]
                    if pos[2][0] < 401:
                        if pos[2][1] < c[0] or pos[2][1]+48 > d[0]:
                            hits[2] = 1
                    else:
                        if pos[2][1] < c[1]or pos[2][1]+48 > d[1]:
                            hits[2] = 1
            elif deathStage[2] == fps * 2:
                deathStage[2] = 0
            if hits[2] == 1 and prev_hits[2] == 1 or deathStage[2] > 0:
                if deathStage[2] == 0:
                    deathStage[2] += 1
                    Lives[2] -= 1
                if deathStage[2] != 0:
                    deathStage[2] += 1
                    a = deathStage[2] % 40
                    b = Lives[2]
                    if a < 20:
                        if b < 5:
                            Hearts.moveto(rh[b], 1000, 1000)
                            Hearts.moveto(drh[b], b*40+560, 10)
                        else:
                            Hearts.moveto(rh[b], 1000, 1000)
                            Hearts.moveto(drh[b], b*40+360, 50)
                    else:
                        if b < 5:
                            Hearts.moveto(rh[b], b*40+560, 10)
                            Hearts.moveto(drh[b], 1000, 1000)
                        else:
                            Hearts.moveto(rh[b], b*40+360, 50)
                            Hearts.moveto(drh[b], 1000, 1000)
                    if Lives[2] == 0:
                        canvas.moveto(rm, 1000, 1000)
                        canvas.moveto(rd, 1000, 1000)
                        if pos[2][1] <= 540:
                            pos[2][1] += 10
                        elif pos[2][1] < 550:
                            pos[2][1] = 550
                        elif pos[2][1] == 550:
                            canvas.moveto(graves[2], pos[2][0]-5, 450)
    canvas.moveto(bg1, background[0], 0)
    canvas.moveto(bg2, background[0]-800, 0)
    canvas.moveto(gr1, background[1], 500)
    canvas.moveto(gr2, background[1]-800, 500)
    canvas.moveto(top1, background[1]-800+400*array.index(1), pipes[0])
    canvas.moveto(top2, background[1]-800+400*array.index(2), pipes[1])
    canvas.moveto(top3, background[1]-800+400*array.index(3), pipes[2])
    canvas.moveto(bottom1, background[1]-800+400*array.index(1), pipes[0]+pipes[3])
    canvas.moveto(bottom2, background[1]-800+400*array.index(2), pipes[1]+pipes[4])
    canvas.moveto(bottom3, background[1]-800+400*array.index(3), pipes[2]+pipes[5])
    canvas.move(poops[0], -6, 0)
    canvas.move(poops[1], -6, 0)
    canvas.move(poops[2], -6, 0)
    pospoops[0][0] -= eggspeed
    pospoops[1][0] -= eggspeed
    pospoops[2][0] -= eggspeed
    if flapStage == 0:
        if data[0].get() != "None":
            canvas.moveto(yu, pos[0][0], pos[0][1])
            canvas.moveto(ym, 1000, 1000)
        if data[1].get() != "None":
            if Lives[1] != 0:
                canvas.moveto(bm, pos[1][0], pos[1][1])
                canvas.moveto(bd, 1000, 1000)
            else:
                canvas.moveto(bu, pos[1][0], pos[1][1])
        if data[2].get() != "None":
            if Lives[2] != 0:
                canvas.moveto(rm, 1000, 1000)
                canvas.moveto(rd, pos[2][0], pos[2][1])
            else:
                canvas.moveto(ru, pos[2][0], pos[2][1])
    elif flapStage == 1:
        if data[0].get() != "None":
            if Lives[0] != 0:
                canvas.moveto(yu, 1000, 1000)
                canvas.moveto(ym, pos[0][0], pos[0][1])
            else: 
                canvas.moveto(yu, pos[0][0], pos[0][1])
        if data[1].get() != "None":
            canvas.moveto(bu, pos[1][0], pos[1][1])
            canvas.moveto(bm, 1000, 1000)
        if data[2].get() != "None":
            if Lives[2] != 0:
                canvas.moveto(rm, pos[2][0], pos[2][1])
                canvas.moveto(rd, 1000, 1000)
            else:
                canvas.moveto(ru, pos[2][0], pos[2][1])
    elif flapStage == 2:
        if data[0].get() != "None":
            if Lives[0] != 0:
                canvas.moveto(ym, 1000, 1000)
                canvas.moveto(yd, pos[0][0], pos[0][1])
            else: 
                canvas.moveto(yu, pos[0][0], pos[0][1])
        if data[1].get() != "None":
            if Lives[1] != 0:
                canvas.moveto(bu, 1000, 1000)
                canvas.moveto(bm, pos[1][0], pos[1][1])
            else:
                canvas.moveto(bu, pos[1][0], pos[1][1])
        if data[2].get() != "None":
            canvas.moveto(ru, pos[2][0], pos[2][1])
            canvas.moveto(rm, 1000, 1000)
    elif flapStage == 3:
        if data[0].get() != "None":
            if Lives[0] != 0:
                canvas.moveto(ym, pos[0][0], pos[0][1])
                canvas.moveto(yd, 1000, 1000)
            else: 
                canvas.moveto(yu, pos[0][0], pos[0][1])
        if data[1].get() != "None":
            if Lives[1] != 0:
                canvas.moveto(bm, 1000, 1000)
                canvas.moveto(bd, pos[1][0], pos[1][1])
            else:
                canvas.moveto(bu, pos[1][0], pos[1][1])
        if data[2].get() != "None":
            if Lives[2] != 0:
                canvas.moveto(ru, 1000, 1000)
                canvas.moveto(rm, pos[2][0], pos[2][1])
            else:
                canvas.moveto(ru, pos[2][0], pos[2][1])
        flapStage = -1
    if background[0] % 4 == 0:
        flapStage += 1
    background[0] -= 1
    background[1] -= 4
    if background[0] == 0:
        background[0] = 800
    if background[1] == 0:
        background[1] = 800
    if pipes[0] == 2000 :
        pipes[0] = random.randint(-620, -300)
        pipes[1] = random.randint(-620, -300)
        pipes[2] = random.randint(-620, -300)
        pipes[3] = random.randint(740, 840)
        pipes[4] = random.randint(740, 840)
        pipes[5] = random.randint(740, 840)
    if background[1] % 400 == 0:
        mode += 1
        if data[0].get() != "None" and Lives[0] != 0:
            Scores[0].set("Score: "+str(int(Scores[0].get()[7:])+1))
        if data[1].get() != "None" and Lives[1] != 0:
            Scores[1].set("Score: "+str(int(Scores[1].get()[7:])+1))
        if data[2].get() != "None" and Lives[2] != 0:
            Scores[2].set("Score: "+str(int(Scores[2].get()[7:])+1))
        if mode == 3:
            pipes[0] = random.randint(-620, -300)
            pipes[3] = random.randint(740, 840)
        elif mode == 5:
            pipes[2] = random.randint(-620, -300)
            pipes[5] = random.randint(740, 840)
        elif mode == 7:
            pipes[1] = random.randint(-620, -300)
            pipes[4] = random.randint(740, 840)
        if mode == len(order):
            mode = 2
    #print(mode)




root = Tk()
root.geometry("800x800")
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
Checkbutton(root, text="Egg bonb", variable=data[4], onvalue=1, offvalue=0).grid(row=3, column=1)
Label(root, text="Lives").grid(row=4, column=0)
w = Scale(root, from_=1, to=10, orient=HORIZONTAL, length=130)
w.grid(row=4, column=1, columnspan=1)
Radiobutton(root, text='Green', variable=data[5], value=0).grid(row=5, column=0)
Radiobutton(root, text='Red', variable=data[5], value=1).grid(row=5, column=1)
Radiobutton(root, text='Dark', variable=data[6], value=0).grid(row=6, column=0)
Radiobutton(root, text='Light', variable=data[6], value=1).grid(row=6, column=1)
Button(root, text="Play", command=selectMapFlappyBird, width=45).grid(row=7, column=0, columnspan=3)

root.mainloop()