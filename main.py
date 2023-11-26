from tkinter import *
from cell import Cell
import settings
import utils

#Instantiate root to Tk() which is a window, helps to open up a new window where our game will be.
#Root.mainloop() helps to keep the window open until close button is pressed.
#Everything will go between the root and root.mainloop()
root = Tk()
#Override settings of window
#change background color to black
root.configure(bg="black")
#This is used to customise the window size.
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')

#This sets the title of the window to mineSweeper.
root.title("MineSweeper")

#This avoids the user to change the window size, false for width and false for height.
root.resizable(False, False)

'''
Frames allow us to seperate the window into different sections. In this scenario we have a top_frame where we want to 
have a section at the top. We pass in the root as it is our main window, background color, the width of it and the height of it.
We then decide where to place the top_frame and we give it the axis based on where we want it to start 
'''
top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_percentage(15)
)
top_frame.place(x=0, y=0)

game_Title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Ma Balls',
    font=('',48)
)

game_Title.place(
    x=utils.width_percentage(25), y = 0
)
left_frame = Frame(
    root,
    bg='black',
    width=utils.width_percentage(25),
    height=utils.height_percentage(85),
)
left_frame.place(x=0,y=utils.height_percentage(15))

center_frame = Frame(
    root,
    bg="green",
    width=utils.width_percentage(75),
    height=utils.height_percentage(85)
)
center_frame.place(x=utils.width_percentage(25),y=utils.height_percentage(15))

#Instantiate the cells

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_button_object(center_frame)
        c.cell_btn_object.grid(
            column = x,
            row = y,
        )
#Call the label from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)

Cell.randomize_mines()
#Test to see if we get all cells.
#print(Cell.all)

#Run the window
root.mainloop()