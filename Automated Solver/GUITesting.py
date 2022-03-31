from gui import *
from tkinter import *

def respond():
    print("Hello World!")

test1 = UI()
test1.createCanvas(100,100,test1.root, bg="red")
test1.createCanvas(100,100,test1.root, bg="green")
test1.placeCanvas(test1.canvasList[0], CENTER)
test1.placeCanvasCoords(test1.canvasList[1], 760,760)
test1.createEntry(900,900)
test1.createButton(900,800,"Press Me!", respond)
test1.createWindow()