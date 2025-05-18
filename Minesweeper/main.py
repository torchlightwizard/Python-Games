from tkinter import *
from settings.globals import HEIGHT, WIDTH,GRIDSIZE
from utils.settings_mod import hperc, wperc
from components.cell import Cell


# Init
root = Tk()


# Window Settings
root.configure(bg="black")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Minesweeper")
root.resizable(False, False)


# Flexbox type shit
top_frame = Frame(
    root,
    bg="black",
    width=WIDTH,
    height=hperc(25),
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg="black",
    width=wperc(25),
    height=hperc(75)
)
left_frame.place(x=0, y=hperc(25))

center_frame = Frame(
    root,
    bg="black",
    width=wperc(75),
    height=hperc(75)
)
center_frame.place(x=wperc(25), y=hperc(25))


# Elements
for y in range(GRIDSIZE):
    for x in range(GRIDSIZE):
        c = Cell(x+1, y+1)
        c.new_btn(center_frame).btn.grid(row=y, column=x)
        
print(Cell.all)
# Window Run
root.mainloop()

