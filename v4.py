from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

titles = ["Flappy Bird", "Aztec", "Balls"]
fps = 60
gameEnd = False
background = [800, 800]
cursor = [100, 100]
flapStage = 0

def selectMapFlappyBird():
    global root, canvas, bg1, bg2, gr1, gr2, up, mid, down
    root.destroy()
    root = Tk()
    root.geometry("800x600")
    root.title("Flappy Bird")
    root.resizable(False, False)
    canvas = Canvas(root, width = 800, height = 600)
    canvas.pack()
    light = messagebox.askyesno(title=None, message="Use light theme?")
    if light:
        bgPath = Image.open(r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\background-day.png")
    else:
        bgPath = Image.open(r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\background-night.png")
    grPath = Image.open(r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\base.png")
    bgImg = ImageTk.PhotoImage(bgPath)
    grImg = ImageTk.PhotoImage(grPath)
    bg1 = canvas.create_image(0, 0, image = bgImg, anchor="nw")
    bg2 = canvas.create_image(0, 0, image = bgImg, anchor="nw")
    gr1 = canvas.create_image(0, 500, image = grImg, anchor="nw")
    gr2 = canvas.create_image(0, 500, image = grImg, anchor="nw")
    messagebox.showinfo(title=None, message="Click to start")
    upPath = Image.open(r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\yellowbird-upflap.png")
    midPath = Image.open(r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\yellowbird-midflap.png")
    downPath = Image.open(r"C:\Users\seanr\Documents\Programming\School\Collision game\FlappyBirdSprites\yellowbird-downflap.png")
    upImg = ImageTk.PhotoImage(upPath)
    midImg = ImageTk.PhotoImage(midPath)
    downImg = ImageTk.PhotoImage(downPath)
    up = canvas.create_image(100, 300, image = upImg, anchor="nw")
    mid = canvas.create_image(1000, 1000, image = midImg, anchor="nw")
    down = canvas.create_image(1000, 1000, image = downImg, anchor="nw")
    root.config(cursor="none")
    root.bind('<Motion>', motion)
    #root.bind("<Button-1>", start)
    update_window()
    root.mainloop()


def update_window():
    global background, flapStage
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
    background[1] -= 2
    if background[0] == 0:
        background[0] = 800
        background[1] = 800
    elif background[1] == 0:
        background[1] = 800
    root.after(int(1000/fps), update_window)

def selectMapAztec():
    global map
    map = 1
def selectMapBalls():
    global map
    map = 2


def motion(event):
    global cursor
    x, y = event.x, event.y
    cursor = [x-27, y-22]
    #canvas.moveto(img, x-27, y-22)
    #print('{}, {}'.format(x, y))

root = Tk()
root.title("Mode Select")
Button(root, text="Flappy Bird", command=selectMapFlappyBird, width=30).pack()
Button(root, text="Aztec", command=selectMapAztec, width=30).pack()
Button(root, text="Balls", command=selectMapBalls, width=30).pack()

root.mainloop()