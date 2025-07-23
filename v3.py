from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

titles = ["Flappy Bird", "Aztec", "Balls"]
fps = 20

def selectMapFlappyBird():
    global root, canvas, canvasimage2, img
    root.destroy()
    root = Tk()
    root.geometry("800x600")
    root.title("Flappy Bird")
    root.resizable(False, False)
    canvas = Canvas(root, width = 800, height = 600)
    canvas.pack()
    light = messagebox.askyesno(title=None, message="Use light theme?")
    if light:
        bgimg = Image.open(r"C:\Users\seanr\Documents\Programming\School\Collision game\bg.png")
    else:
        bgimg = Image.open(r"C:\Users\seanr\Documents\Programming\School\Collision game\bg2.png")
    canvasimage = ImageTk.PhotoImage(bgimg)
    canvas.create_image(0, 0, image = canvasimage, anchor="nw")
    messagebox.showinfo(title=None, message="Click to start")
    bird = Image.open(r"C:\Users\seanr\Documents\Programming\School\Collision game\bird.png")
    canvasimage2 = ImageTk.PhotoImage(bird)
    img = canvas.create_image(100, 300, image = canvasimage2)
    root.config(cursor="none")
    root.bind('<Motion>', motion)
    root.mainloop()

def selectMapAztec():
    global map
    map = 1
def selectMapBalls():
    global map
    map = 2


def motion(event):
    x, y = event.x, event.y
    canvas.moveto(img, x-27, y-22)
    print('{}, {}'.format(x, y))

root = Tk()
root.title("Mode Select")
Button(root, text="Flappy Bird", command=selectMapFlappyBird, width=30).pack()
Button(root, text="Aztec", command=selectMapAztec, width=30).pack()
Button(root, text="Balls", command=selectMapBalls, width=30).pack()

root.mainloop()