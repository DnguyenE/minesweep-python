from tkinter import *  # importing the package
import configure

root = Tk()

# Configure the settings of the window here:
root.configure(bg="black")
root.geometry(f'{configure.WINDOW_WIDTH}x{configure.WINDOW_HEIGHT}')  # Init. height and width
root.title("Minesweeper")  # Title of window
root.resizable(False, False)  # Making window not resizable

top_frame = Frame(root,
                  bg='grey',
                  width=configure.WINDOW_WIDTH,  # Constant Function
                  height=configure.WINDOW_HEIGHT * 0.15,  # Call of Height function here (15%) of height
                  )

top_frame.place(x=0, y=0)  # No need to change anything here

left_frame = Frame(root,
                   bg='blue',
                   width=configure.WINDOW_WIDTH * 0.15,  # Call on function here to determine the proper width
                   height=612  # Call on height function here (85%) of height
                   )

left_frame.place(x=0, y=108)  # Implement the function to determine the proper coordinate

root.mainloop()  # Creating the window
