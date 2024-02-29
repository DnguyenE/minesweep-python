from tkinter import *  # importing the package
import configure

root = Tk()  # init Tk
root.configure(bg="black")  # changing background
root.geometry(f'{configure.WINDOW_WIDTH}x{configure.WINDOW_HEIGHT}')  # Creating the GUI window
root.title("Minesweeper")
root.resizable(False, False)  # making this window not resizeable

top_frame = Frame(root, bg="grey")

root.mainloop()  # Creating the window


