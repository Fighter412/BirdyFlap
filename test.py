import tkinter as tk
 
import time
 
def get_time(arg, canvas, var):
    show = time.strftime(f'%I:%M:%S %P')
    canvas.itemconfig(var, text=show)
    arg.after(1000, lambda: get_time(arg, canvas, var))
 
root = tk.Tk()
 
canvas = tk.Canvas(root, width=600, height=500, bg='antiquewhite')
show = time.strftime(f'%I:%M:%S %P')
var = canvas.create_text(300,100, text=show, fill='blue', font=('serif', 20, 'bold'))
canvas.pack()
 
root.after(1000, lambda: get_time(root, canvas, var))
root.mainloop()