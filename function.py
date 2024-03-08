# File for creating functions
import configure


# Input percentage as decimal and return the 'configure.height' by the percentage
def getHeight(percentage):  # input decimal percentage and returns height
    return configure.WINDOW_HEIGHT * percentage


# Input percentage as decimal and return the 'configure.width' by the percentage

def getWidth(percentage):  # input decimal percentage and returns width
    return configure.WINDOW_WIDTH * percentage
