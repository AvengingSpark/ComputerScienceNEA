from tkinter import *
from sudokuGridClass import SudokuGrid

class UI:
    
    def __init__(self):
        """
        This class' main attributes are as follows:
        HEIGHT/WIDTH - This specifies the height and width of the main canvas to be placed on the window
        canvas/line/entry/button/text List - These are all where the widgets will be stored to be easier modified or deleted
        Grid - This is where the current state of the sudoku grid will be stored to be inputted into the autosolving classes
        """
        
        self.HEIGHT = 918
        self.WIDTH = 918

        
        self.canvasList = []
        self.lineList = []
        self.entryList = []
        self.buttonList = []
        self.textList = []
        
        self.grid = []
        
        for f in range(81):
            #Sets each value within the grid attribute to be 0. Implies an empty grid
            self.grid.append("0")
                
        self.__initGrid()
        
    def __initGrid(self):
        #Creates a window with a title of Sudoku Autosolver, and is automatically sized to fit the entire monitor
            self.root = Tk()
            self.root.title("Sudoku Autosolver")
            self.root.state("zoomed")
            self.root.configure(bg="black")
            
            
    def createCanvas(self, h, w, p, bg="black"):
        #Creates a canvas of height h, width w, with a parent layer specified. The background of the canvas created can be specified to any hex colour but is automatically set to be black.
        self.canvasList.append(Canvas(p, height=h, width=w, bg=bg, bd=0, highlightthickness=0))
        
        
    def createLine(self, coords, w, canvas, colour="black"):
        #Creates a line which goes from coordinates in the form (x1, x2, y1, y2), has a width w, the layer in which it will be placed specified, and a colour automatically assinged to be black
        self.lineList.append(canvas.create_line(coords, width=w, fill=colour))
        
    def placeCanvas(self, canvas, anchorPoint):
        #Places a canvas using Tkinter's coordinate system at specified anchor point
        canvas.place(anchor=anchorPoint, relx=0.5, rely=0.505)
        
    def placeCanvasCoords(self, canvas, x, y):
        #Places a canvas using Tkinter's coordinate system using specific coordinates to place the canvas
        canvas.place(x=x, y=y)    
    
    def createEntry(self, x, y):
        #Creates and entry form and places it at coordinates x,y
        self.entryList.append(Entry(self.root, font=("OCR A Extended", 7), width=85))
        self.entryList[-1].place(x=x, y=y)

    def createButton(self, x, y, text, command=None):
        #Creates a button with the resulting mehthod when pressed being command and is placed at coordinated x,y.
        self.buttonList.append(Button(self.root, bg="#00f957", activebackground="red", text=text, relief="flat", overrelief="flat", padx="10p", pady="5p", font=("OCR A Extended", 25), command=command))
        self.buttonList[-1].place(x=x, y=y)
        
    def createWindow(self):
        #Displays the window on the user's device
        self.root.mainloop()
            
class SudokuBoard(UI):
    
    def __init__(self):
        super().__init__()

        self.generateGrid()
        self.generateWidgets()
        self.generateCellEventListeners()
        self.createInstruction()
        self.createWindow()
    

    def createLines(self, cellNum):
        """
        Creates lines in a specific location depending on the cell's location on the grid
        The coordinates specified relate to where the line will be placed.
        The thickness of the placed line depends on where the cell is - with the thickest line defining the borders around a cell, and those around each 3x3 grid being less thick and the thinnest defined the borders of all other cells
        """
        bottomLine = (0,self.HEIGHT/9,self.WIDTH/9,self.WIDTH/9)
        topLine = (0,0,self.WIDTH/9,0)
        rightLine=(self.HEIGHT/9,0,self.WIDTH/9,self.WIDTH/9)
        leftLine=(0,0,0,self.WIDTH/9)
        
        top=False
        bott=False
        l=False
        r=False
        colour="#000957"
        
        if cellNum<= 9:
            #If the cell is in the top row
            self.createLine(topLine, 10, self.canvasList[-1], colour)
            top = True
        
        if cellNum >= 73:
            #If the cell is in the bottom row
            self.createLine(bottomLine, 10, self.canvasList[-1], colour)
            bott = True
        
        if cellNum%9==0:
            #If the cell is within the 9th column
            self.createLine(rightLine, 10, self.canvasList[-1], colour)
            r=True
            
        if cellNum%9==1:
            #If the cell is within the 1st column
            self.createLine(leftLine, 10, self.canvasList[-1], colour)
            l=True
            
        if cellNum%3==0 and not r:
            #If the cell is in the third or sixth row
            self.createLine(rightLine, 5, self.canvasList[-1], colour)
            r=True
            
        if cellNum%3==1 and not l:
            #If the cell is in the fourth or seventh row
            self.createLine(leftLine, 5, self.canvasList[-1], colour)
            l=True
            
        if (cellNum-1)//9==2 and not bott:
            #If the cell is in the third column
            self.createLine(bottomLine, 5, self.canvasList[-1], colour)
            bott=True
            
        if (cellNum-1)//9==3 and not top:
            #If the cell is in the fourth column
            self.createLine(topLine, 10, self.canvasList[-1], colour)
            top=True
            
        if (cellNum-1)//9==5 and not bott:
            #If the cell is in the sixth column
            self.createLine(bottomLine, 5, self.canvasList[-1], colour)
            bott=True
            
        if (cellNum-1)//9==6 and not top:
            #If the cell is in the seventh column
            self.createLine(topLine, 10, self.canvasList[-1], colour)
            top=True
            
        #If no lines have yet been created at an edge, create a thin line at those edges
        if not top:
            self.createLine(topLine, 2, self.canvasList[-1], colour)
        if not bott:
            self.createLine(bottomLine, 2, self.canvasList[-1], colour)
        if not l:
            self.createLine(leftLine, 2, self.canvasList[-1], colour)
        if not r:
            self.createLine(rightLine, 2, self.canvasList[-1], colour)
            
    def createCell(self, cellNum, colour):
        #Creates a canvas which has 1/81th the area of the base canvas
        self.createCanvas((self.HEIGHT/9), (self.WIDTH/9), self.canvasList[0], colour)
        self.createLines(cellNum)
        
    def createCells(self):
        #Creates 81 canvases representing a cell
        for f in range(81):
            self.createCell(f+1, "grey")
        
        self.placeCells()
        
    def placeCells(self):
        #Places each of the cells in an order, from left to right and from top to bottom. Similar to writing on a page.
        for f in range(9):
            xCoord = (self.HEIGHT*((f)/9))
            for g in range(9):
                yCoord = (self.WIDTH*((g)/9))
                self.placeCanvasCoords(self.canvasList[(f*9)+g+1], yCoord, xCoord)
                
    def selectedSingle(self, cellNum):
        #Changes a cell's background to be white if a user clicks on it. Changes all other cell's backgrounds to be grey to show that they are not being selected. Overall means that only one cell can be selected at once
        self.canvasList[cellNum].configure(bg="white")
        self.canvasList[cellNum].focus_set()
        for i in range(len(self.canvasList)):
            if self.canvasList[i]["background"] == "white" and cellNum!=i:
                self.canvasList[i].configure(bg="grey")
            
    def selectedMultiple(self, cellNum):
        #Changes a cell's background to be white if a user clicks on it to show as if it has been selected. Allows for multiple cells to be selected as one.
        self.canvasList[cellNum].configure(bg="white")
        self.canvasList[cellNum].focus_set()
            
    def deselect(self):
        #Changes the background of all cells to be grey as to show all cells have been deselected
        for f in range(len(self.canvasList)):
            self.canvasList[f].configure(bg="grey")
            
    def keyTyped(self, letter):
        #Responds to a key press input and write that input to a cell as long as it is a digit and not 0.
        for f in range(len(self.canvasList)):
            if self.canvasList[f]["background"] == "white" and letter.isdigit() and letter != "0" and len(self.canvasList[f].find_all()) == 4:
                #If the cell is selected (background is white), and the key pressed is a digit and the digit is not 0
                self.canvasList[f].create_text(43,43, text=letter, anchor=CENTER, fill="blue", font=("OCR A Extended", 50), tag="digit")
                self.grid[f-1] = letter
            elif len(self.canvasList[f].find_all()) > 4 and letter.isdigit() and letter != "0" and self.canvasList[f]["background"] == "white":
                while len(self.canvasList[f].find_all()) > 4:
                    self.canvasList[f].delete(self.canvasList[f].find_all()[-1])
                self.canvasList[f].create_text(43,43, text=letter, anchor=CENTER, fill="blue", font=("OCR A Extended", 50), tag="digit")
                self.grid[f-1] = letter
        self.checkGrid()
        
    def canCreatePencilMark(self, cellNum):
        if len(self.canvasList[cellNum].find_withtag("digit")) >= 1:
            return False
        else:
            return True
                
    def cornerKey(self, letter):
        #If the control key is held whilst a key is pressed, the digit written to a cell will instead be found towards the top edge of the cell (a corner pencil mark)
        for f in range(len(self.canvasList)):
            if letter.isdigit() and letter != "0" and self.canvasList[f]["background"] == "white" and self.canCreatePencilMark(f):
                self.canvasList[f].create_text(((8.7*int(letter))),13, text=letter, anchor=CENTER, fill="black", font=("OCR A Extended", 12), tag="cornerPencil")
        
    def centreKey(self, letter):
        #If the alt key is held whilst a key is pressed, the digit written to the cell will be a pencil mark found within the centre of a cell
        for f in range(len(self.canvasList)):
            if letter.isdigit() and letter != "0" and self.canvasList[f]["background"] == "white" and self.canCreatePencilMark(f):
                self.canvasList[f].create_text((30+(12*((int(letter)-1)%3))),(30+(12*((int(letter)-1)//3))), text=letter, anchor=CENTER, fill="black", font=("OCR A Extended", 8), tag="centrePencil")
            
    def deleteNum(self):
        #This will delete all digits from the cell
        for f in range(len(self.canvasList)):
            if self.canvasList[f]["background"] == "white":
                while len(self.canvasList[f].find_all()) > 4:
                    self.canvasList[f].delete(self.canvasList[f].find_all()[-1])
                self.grid[f-1] = "0"
                
    def upCell(self, cellNum):
        #Goes up a cell, wraps around each column
        self.canvasList[cellNum].configure(bg="grey")
        self.canvasList[((cellNum-9)%82)].configure(bg="white")
        self.canvasList[((cellNum-9)%82)].focus_set()
    
    def downCell(self, cellNum):
        #Goes down a cell, wraps around each column
        self.canvasList[cellNum].configure(bg="grey")
        self.canvasList[((cellNum+9)%82)].configure(bg="white")
        self.canvasList[((cellNum+9)%82)].focus_set()
        
    def leftCell(self, cellNum):
        #Goes left a cell, wraps around each row
        self.canvasList[cellNum].configure(bg="grey")
        self.canvasList[((cellNum-1)%82)].configure(bg="white")
        self.canvasList[((cellNum-1)%82)].focus_set()
        
    def rightCell(self, cellNum):
        #Goes right a cell, wraps around each row
        self.canvasList[cellNum].configure(bg="grey")
        self.canvasList[((cellNum+1)%82)].configure(bg="white")
        self.canvasList[((cellNum+1)%82)].focus_set()
        
    def upCellSelect(self, cellNum):
        #If the shift key is held whilst a arrow key is pressed, the cell up by one is also selected
        self.canvasList[((cellNum-9)%82)].configure(bg="white")
        self.canvasList[((cellNum-9)%82)].focus_set()
    
    def downCellSelect(self, cellNum):
        #If the shift key is held whilst a arrow key is pressed, the cell down by one is also selected
        self.canvasList[((cellNum+9)%82)].configure(bg="white")
        self.canvasList[((cellNum+9)%82)].focus_set()
        
    def leftCellSelect(self, cellNum):
        #If the shift key is held whilst a arrow key is pressed, the cell left by one is also selected
        self.canvasList[((cellNum-1)%82)].configure(bg="white")
        self.canvasList[((cellNum-1)%82)].focus_set()
        
    def rightCellSelect(self, cellNum):
        #If the shift key is held whilst a arrow key is pressed, the cell right by one is also selected
        self.canvasList[((cellNum+1)%82)].configure(bg="white")
        self.canvasList[((cellNum+1)%82)].focus_set()
        
    def cornerPencilAlert(self):
        #Creates an alert to the user if the control key is held, telling them that the digit entered will be a pencil mark in the "corner" of the cell
        self.textList.append(Label(self.root, bg="red", text="Pencil Marks in corner"))
        self.textList[-1].place(x=100, y=100)
        self.root.bind("<KeyRelease-Control_L>", lambda event: self.deleteText())
        self.root.bind("<KeyRelease-Control_R>", lambda event: self.deleteText())
        
    def centrePencilAlert(self):
        #Creates an alert to the user if the alt key is held, telling them that the digit entered will be a pencil mark in the "centre" of the cell
        self.textList.append(Label(self.root, bg="red", text="Pencil Marks in centre"))
        self.textList[-1].place(x=100, y=100)
        self.root.bind("<KeyRelease-Alt_L>", lambda event: self.deleteText())
        self.root.bind("<KeyRelease-Alt_R>", lambda event: self.deleteText()) 
        
    def deleteText(self):
        #Deletes the pencil markings alert
        for f in range(len(self.textList)):
            self.textList[f].destroy() 
    
    def returnGrid(self):
        #Returns the string as one continuous 81 long string
        temp = "".join(self.grid)
        return temp
    
    def updateGrid(self, puzzle=None):
        #Updates the values of the grid, and the digit displayed according to the puzzle inputted
        if len(puzzle) == 81:
            #Checks that the puzzle 81 digits long
            for f in range(len(puzzle)):
                if len(self.canvasList[f+1].find_all()) > 4:
                    self.canvasList[f+1].delete(self.canvasList[f+1].find_all()[-1])
                if puzzle[f] != "0":
                    self.canvasList[f+1].create_text(43,43, text=puzzle[f], anchor=CENTER, fill="black", font=("OCR A Extended", 35), tag="num")
                self.grid[f] = str(puzzle[f])
        else:
            print("ERROR PUZZLE NOT 81 DIGITS LONG")
    
    def checkGrid(self):
        #Creates an instance of the SudokuGrid class and checks for any clashes within the grid. If there are any clashes, the cells in which clashes occur are highlighted in red.
        puzzle = SudokuGrid(self.returnGrid())
        clashes = puzzle.returnClashes()
        for i in range(len(clashes)):
            for f in range(len(clashes[i])):
                self.canvasList[clashes[i][f]].configure(bg="red")
                
    def clearGrid(self):
        #Clears all values within the grid and sets each value within the grid attribute to be 0 (an empty cell)
        for f in range(len(self.canvasList)):
            while len(self.canvasList[f].find_all()) > 4:
                self.canvasList[f].delete(self.canvasList[f].find_all()[-1])
            self.grid[f-1] = "0"
        
    def autosolve(self):
        #Creates an instance of the SudokuGrid class and attempts to solve the puzzle, when the puzzle is solved, the resulting grid will be displayed on the application.
        puzzle = SudokuGrid(self.returnGrid())
        self.updateGrid(puzzle.mainLoop())
        
        
    def generateGrid(self):
        self.createCanvas(self.WIDTH, self.HEIGHT, self.root)
        self.placeCanvas(self.canvasList[0], CENTER)
        self.createCells()

    def generateWidgets(self):
        self.createButton(1460, 470, "Autosolve Puzzle", command=lambda: self.autosolve())
        self.createEntry(1460, 350)
        self.createButton(1460, 250, "Enter Puzzle", command=lambda: self.updateGrid(self.entryList[0].get()))
        self.createButton(1460, 590, "Check Puzzle", command=lambda: self.checkGrid())
        self.createButton(1460, 710, "Clear Puzzle", command=lambda: self.clearGrid())
        self.root.bind("<Control-Any-KeyPress>", lambda event: self.cornerPencilAlert())
        self.root.bind("<Alt-Any-KeyPress>", lambda event: self.centrePencilAlert())

        
    def generateCellEventListeners(self):
        self.root.bind("<Double-Button-1>", lambda event: self.deselect())
        for f in range(len(self.canvasList)):
            self.canvasList[f].bind("<Button-1>", lambda event, f=f: self.selectedSingle(f))
            self.canvasList[f].bind("<Shift-Button-1>", lambda event, f=f: self.selectedMultiple(f))
            self.canvasList[f].bind("<Up>", lambda event, f=f: self.upCell(f))
            self.canvasList[f].bind("<Down>", lambda event, f=f: self.downCell(f))
            self.canvasList[f].bind("<Left>", lambda event, f=f: self.leftCell(f))
            self.canvasList[f].bind("<Right>", lambda event, f=f: self.rightCell(f))
            self.canvasList[f].bind("<Shift-Up>", lambda event, f=f: self.upCellSelect(f))
            self.canvasList[f].bind("<Shift-Down>", lambda event, f=f: self.downCellSelect(f))
            self.canvasList[f].bind("<Shift-Left>", lambda event, f=f: self.leftCellSelect(f))
            self.canvasList[f].bind("<Shift-Right>", lambda event, f=f: self.rightCellSelect(f))
            self.canvasList[f].bind("<Any-KeyPress>", lambda event: self.keyTyped(event.char))
            self.canvasList[f].bind("<Control-Any-KeyPress>", lambda event: self.cornerKey(event.keysym))
            self.canvasList[f].bind("<Alt-Any-KeyPress>", lambda event: self.centreKey(event.keysym))
            self.canvasList[f].bind("<BackSpace>", lambda event: self.deleteNum())
            
            
    def createInstruction(self):
        text = """
        Welcome to this Sudoku Solver!
        
        {Insert Text Here}
        """
        instructionWindow = Toplevel(self.root, bg="black")
        instructionWindow.title("Welcome to the Sudoku Solver!")
        instructionWindow.lift(self.root)
        instructionWindow.geometry(f"{int(self.HEIGHT//1.5)}x{self.WIDTH}+{self.WIDTH-100}+50")
        Label(instructionWindow, text=text).pack()