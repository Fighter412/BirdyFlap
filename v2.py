from tkinter import *
from tkinter import messagebox

# Define collision detection logic
def detect_collision(player_x, player_y, player_width, player_height, rect_x, rect_y, rect_width, rect_height):
    if player_x < rect_x + rect_width and player_x + player_width > rect_x and player_y < rect_y + rect_height and player_y + player_height > rect_y:
        return True
    else:
        return False

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    if x+y > 11000:
        messagebox.showerror(title=None, message="You lost")
        messagebox.showinfo(title=None, message="You lost")
        messagebox.showwarning(title=None, message="You lost")


# Create a Tkinter window and Canvas object
root = Tk()
root.resizable(False, False)
root.title("nahbro")
canvas = Canvas(root, width = 800, height = 600)
canvas.pack()

# Draw rectangles / Polygons on the canvas
rect1 = canvas.create_rectangle(100, 100, 200, 200, fill="red")
poly1 = canvas.create_polygon(300, 300, 400, 300, 350, 250, fill = "blue")

root.bind('<Motion>', motion)
root.mainloop()