from tkinter import *  # importing the package
from cell import *
import configure
import function


root = Tk()

# Configure the settings of the window here:
root.configure(bg="black")
root.geometry(f'{configure.WINDOW_WIDTH}x{configure.WINDOW_HEIGHT}')  # Init. height and width
root.title("Minesweeper")  # Title of window
root.resizable(False, False)  # Making window not resizable

top_frame = Frame(root,
                  bg='black',
                  width=configure.WINDOW_WIDTH,  # Constant Function
                  height=function.getHeight(0.25),  # Call of Height function here (15%) of height
                  )

top_frame.place(x=0, y=0)  # No need to change anything here

left_frame = Frame(root,
                   bg='black',
                   width=function.getWidth(0.25),  # Call on function here to determine the proper width
                   height=function.getHeight(0.75)  # Call on height function here (85%) of height
                   )

left_frame.place(x=0, y=function.getHeight(0.25))  # Implement the function to determine the proper coordinate

center_frame = Frame(root,
                     bg='black',
                     width=function.getWidth(0.75),
                     height=function.getHeight(0.75)
                     )

center_frame.place(x=function.getWidth(0.25), y=function.getHeight(0.25))

for x in range(configure.GRID_SIZE):
    for y in range(configure.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=y, row=x
        )

Cell.randomize_mines()

root.mainloop()  # Creating the window
