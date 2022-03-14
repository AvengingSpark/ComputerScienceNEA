from tkinter import *
from sudokuGridClass import SudokuGrid

class UI:
    
    def __init__(self):
        
        self.HEIGHT = 765
        self.WIDTH = 765

        
        self.canvasList = []
        self.lineList = []
        self.entryList = []
        
        self.grid = ["0" for f in range(81)]
        
        self.__initGrid()
        
    def __initGrid(self):
            self.root = Tk()
            self.root.title("Sudoku Autosolver")
            self.root.state("zoomed")
            self.root.configure(bg="black")
            
            
    def createCanvas(self, h, w, p, bg="black"):
        self.canvasList.append(Canvas(p, height=h, width=w, bg=bg, bd=0, highlightthickness=0))
        
        
    def createLine(self, coords, w, canvas, colour="black"):
        self.lineList.append(canvas.create_line(coords, width=w, fill=colour))
        
    def placeCanvas(self, canvas, anchorPoint):
        canvas.place(anchor=anchorPoint, relx=0.5, rely=0.505)
        
    def placeCanvasCoords(self, canvas, x, y):
        canvas.place(x=x, y=y)    
        
    def createWindow(self):
        self.root.mainloop()
            
            
            
class sudokuBoard(UI):
    
    def __init__(self):
        super().__init__()
        self.createCanvas(self.WIDTH, self.HEIGHT, self.root)
        self.placeCanvas(self.canvasList[0], CENTER)
        self.createButton(1350, 470, "Autosolve Puzzle", command=lambda: self.autosolve())
        self.createEntry(1350, 350)
        self.createButton(1350, 250, "Enter puzzle", command=lambda: self.updateGrid(self.entryList[0].get()))
        self.createCells()
        for f in range(len(self.canvasList)):
            self.root.bind("<Double-Button-1>", lambda event: self.deselect())
            self.canvasList[f].bind("<Button-1>", lambda event, f=f: self.selected(f))
            self.canvasList[f].bind("<Any-KeyPress>", lambda event, f=f: self.keyTyped(f, event.char, event))
            self.canvasList[f].bind("<BackSpace>", lambda event, f=f: self.deleteNum(f, event))
        self.createWindow()
    
    def createLines(self, num):
        
        bottomLine = (0,85,85,85)
        topLine = (0,0,85,0)
        rightLine=(85,0,85,85)
        leftLine=(0,0,0,85)
        top=False
        bott=False
        l=False
        r=False
        colour="#000957"
        
        if num<= 9:
            self.createLine(topLine, 10, self.canvasList[-1], colour)
            top = True
        
        if num >= 73:
            self.createLine(bottomLine, 10, self.canvasList[-1], colour)
            bott = True
        
        if num%9==0:
            self.createLine(rightLine, 10, self.canvasList[-1], colour)
            r=True
            
        if num%9==1:
            self.createLine(leftLine, 5, self.canvasList[-1], colour)
            
        if num%3==0:
            self.createLine(rightLine, 5, self.canvasList[-1], colour)
            r=True
            
        if num%3==1:
            self.createLine(leftLine, 5, self.canvasList[-1], colour)
            l=True
            
        if (num-1)//9==2:
            self.createLine(bottomLine, 5, self.canvasList[-1], colour)
            bott=True
            
        if (num-1)//9==3:
            self.createLine(topLine, 10, self.canvasList[-1], colour)
            top=True
            
        if (num-1)//9==5:
            self.createLine(bottomLine, 5, self.canvasList[-1], colour)
            bott=True
            
        if (num-1)//9==6:
            self.createLine(topLine, 10, self.canvasList[-1], colour)
            top=True
            
        if not top:
            self.createLine(topLine, 2, self.canvasList[-1], colour)
        if not bott:
            self.createLine(bottomLine, 2, self.canvasList[-1], colour)
        if not l:
            self.createLine(leftLine, 2, self.canvasList[-1], colour)
        if not r:
            self.createLine(rightLine, 2, self.canvasList[-1], colour)
            
    def createCell(self, cellNum, colour):
        self.createCanvas((self.HEIGHT/9), (self.WIDTH/9), self.canvasList[0], colour)
        self.createLines(cellNum)
        
    def createCells(self):
        for f in range(81):
            self.createCell(f+1, "grey")
        
        self.placeCells()
        
    def placeCells(self):
        for f in range(9):
            xCoord = (self.HEIGHT*((f)/9))
            for g in range(9):
                yCoord = (self.WIDTH*((g)/9))
                self.placeCanvasCoords(self.canvasList[(f*9)+g+1], yCoord, xCoord)
                
    def selected(self, f):
        self.canvasList[f].configure(bg="white")
        self.canvasList[f].focus_set()
        for i in range(len(self.canvasList)):
            if self.canvasList[i]["background"] == "white" and f!=i:
                self.canvasList[i].configure(bg="grey")
                
    def deselect(self):
        for f in range(len(self.canvasList)):
            self.canvasList[f].configure(bg="grey")
            
    def keyTyped(self, f, letter, event=None):
        if self.canvasList[f]["background"] == "white" and letter.isdigit() and letter != "0" and len(self.canvasList[f].find_all()) == 4:
            self.canvasList[f].create_text(43,43, text=letter, anchor=CENTER, fill="black", font=("Comic Sans MS", 35), tag="num")
            self.grid[f-1] = letter
        elif len(self.canvasList[f].find_all()) > 4 and letter.isdigit() and letter != "0":
            while len(self.canvasList[f].find_all()) > 4:
                self.canvasList[f].delete(self.canvasList[f].find_all()[-1])
            self.canvasList[f].create_text(43,43, text=letter, anchor=CENTER, fill="black", font=("Comic Sans MS", 35), tag="num")
            self.grid[f-1] = letter
            
    def deleteNum(self, f, event=None):
        while len(self.canvasList[f].find_all()) > 4:
            self.canvasList[f].delete(self.canvasList[f].find_all()[-1])
        self.grid[f-1] = "0"
        
    def returnGrid(self):
        return "".join(self.grid)
    
    def updateGrid(self, puzzle=None):
        for f in range(len(puzzle)):
            self.deleteNum(f+1)
            if puzzle[f] != "0":
                self.canvasList[f+1].create_text(43,43, text=puzzle[f], anchor=CENTER, fill="black", font=("Comic Sans MS", 35), tag="num")
            self.grid[f] = puzzle[f]

    def createEntry(self, x, y):
        entry = Entry(self.root, font=("Comic Sans MS", 7), width=85)
        self.entryList.append(entry)
        entry.place(x=x, y=y)

    def createButton(self, x, y, text, command=None):
        button = Button(self.root, bg="#00f957", activebackground="red", text=text, relief="flat", overrelief="flat", padx="10p", pady="5p", font=("Comic Sans MS", 25), command=command)
        button.place(x=x, y=y)
        
    def autosolve(self):
        puzzle = SudokuGrid(self.returnGrid())
        self.updateGrid(puzzle.mainLoop())
    