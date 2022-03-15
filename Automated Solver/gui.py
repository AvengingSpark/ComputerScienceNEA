from tkinter import *
from sudokuGridClass import SudokuGrid

class UI:
    
    def __init__(self):
        
        self.HEIGHT = 765
        self.WIDTH = 765

        
        self.canvasList = []
        self.lineList = []
        self.entryList = []
        self.textList = []
        
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
            self.canvasList[f].bind("<Button-1>", lambda event, f=f: self.selectedSingle(f))
            self.canvasList[f].bind("<Up>", lambda event, f=f: self.upCell(f))
            self.canvasList[f].bind("<Down>", lambda event, f=f: self.downCell(f))
            self.canvasList[f].bind("<Left>", lambda event, f=f: self.leftCell(f))
            self.canvasList[f].bind("<Right>", lambda event, f=f: self.rightCell(f))
            self.canvasList[f].bind("<Control-Up>", lambda event, f=f: self.upCellSelect(f))
            self.canvasList[f].bind("<Control-Down>", lambda event, f=f: self.downCellSelect(f))
            self.canvasList[f].bind("<Control-Left>", lambda event, f=f: self.leftCellSelect(f))
            self.canvasList[f].bind("<Control-Right>", lambda event, f=f: self.rightCellSelect(f))
            self.canvasList[f].bind("<Shift-Button-1>", lambda event: self.selecting())
            self.canvasList[f].bind("<Control-Button-1>", lambda event, f=f: self.selectedMultiple(f))
            self.canvasList[f].bind("<Any-KeyPress>", lambda event: self.keyTyped(event.char, event))
            self.root.bind("<Control-Any-KeyPress>", lambda event: self.cornerPencil())
            self.root.bind("<Alt-Any-KeyPress>", lambda event: self.centerPencil())
            self.canvasList[f].bind("<Control-Any-KeyPress>", lambda event: self.cornerKey(event.keysym, event))
            self.canvasList[f].bind("<Alt-Any-KeyPress>", lambda event: self.centerKey(event.keysym, event))
            self.canvasList[f].bind("<BackSpace>", lambda event: self.deleteNum(event))
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
                
    def selectedSingle(self, f):
        self.canvasList[f].configure(bg="white")
        self.canvasList[f].focus_set()
        for i in range(len(self.canvasList)):
            if self.canvasList[i]["background"] == "white" and f!=i:
                self.canvasList[i].configure(bg="grey")
            
    def selectedMultiple(self, f):
        self.canvasList[f].configure(bg="white")
        self.canvasList[f].focus_set()
            
    def deselect(self):
        for f in range(len(self.canvasList)):
            self.canvasList[f].configure(bg="grey")
            
    def keyTyped(self, letter, event=None):
        for f in range(len(self.canvasList)):
            if self.canvasList[f]["background"] == "white" and letter.isdigit() and letter != "0" and len(self.canvasList[f].find_all()) == 4:
                self.canvasList[f].create_text(43,43, text=letter, anchor=CENTER, fill="blue", font=("OCR A Extended", 50), tag="num")
                self.grid[f-1] = letter
            elif len(self.canvasList[f].find_all()) > 4 and letter.isdigit() and letter != "0" and self.canvasList[f]["background"] == "white":
                while len(self.canvasList[f].find_all()) > 4:
                    self.canvasList[f].delete(self.canvasList[f].find_all()[-1])
                self.canvasList[f].create_text(43,43, text=letter, anchor=CENTER, fill="blue", font=("OCR A Extended", 50), tag="num")
                self.grid[f-1] = letter
                
    def cornerKey(self, letter, event=None):
        for f in range(len(self.canvasList)):
            if len(self.canvasList[f].find_all()) >= 4 and letter.isdigit() and letter != "0" and self.canvasList[f]["background"] == "white":
                self.canvasList[f].create_text(((8.7*int(letter))),13, text=letter, anchor=CENTER, fill="black", font=("OCR A Extended", 12), tag="num")
        
    def centerKey(self, letter, event=None):
        for f in range(len(self.canvasList)):
            if len(self.canvasList[f].find_all()) >= 4 and letter.isdigit() and letter != "0" and self.canvasList[f]["background"] == "white":
                self.canvasList[f].create_text((30+(12*((int(letter)-1)%3))),(30+(12*((int(letter)-1)//3))), text=letter, anchor=CENTER, fill="black", font=("OCR A Extended", 8), tag="num")
            
    def deleteNum(self, event=None):
        for f in range(len(self.canvasList)):
            if self.canvasList[f]["background"] == "white":
                while len(self.canvasList[f].find_all()) > 4:
                    self.canvasList[f].delete(self.canvasList[f].find_all()[-1])
                self.grid[f-1] = "0"
                
    def upCell(self, f):
        self.canvasList[f].configure(bg="grey")
        self.canvasList[((f-9)%82)].configure(bg="white")
        self.canvasList[((f-9)%82)].focus_set()
    
    def downCell(self, f):
        self.canvasList[f].configure(bg="grey")
        self.canvasList[((f+9)%82)].configure(bg="white")
        self.canvasList[((f+9)%82)].focus_set()
        
    def leftCell(self, f):
        self.canvasList[f].configure(bg="grey")
        self.canvasList[((f-1)%82)].configure(bg="white")
        self.canvasList[((f-1)%82)].focus_set()
        
    def rightCell(self, f):
        self.canvasList[f].configure(bg="grey")
        self.canvasList[((f+1)%82)].configure(bg="white")
        self.canvasList[((f+1)%82)].focus_set()
        
    def upCellSelect(self, f):
        self.canvasList[((f-9)%82)].configure(bg="white")
        self.canvasList[((f-9)%82)].focus_set()
    
    def downCellSelect(self, f):
        self.canvasList[((f+9)%82)].configure(bg="white")
        self.canvasList[((f+9)%82)].focus_set()
        
    def leftCellSelect(self, f):
        self.canvasList[((f-1)%82)].configure(bg="white")
        self.canvasList[((f-1)%82)].focus_set()
        
    def rightCellSelect(self, f):
        self.canvasList[((f+1)%82)].configure(bg="white")
        self.canvasList[((f+1)%82)].focus_set()
        
    def deleteText(self):
        for f in range(len(self.textList)):
            self.textList[f].destroy()
        
    def cornerPencil(self):
        self.textList.append(Label(self.root, bg="red", text="Pencil Marks in corner"))
        self.textList[-1].place(x=100, y=100)
        self.root.bind("<KeyRelease-Control_L>", lambda event: self.deleteText())
        self.root.bind("<KeyRelease-Control_R>", lambda event: self.deleteText())
        
    def centerPencil(self):
        self.textList.append(Label(self.root, bg="red", text="Pencil Marks in center"))
        self.textList[-1].place(x=100, y=200)
        self.root.bind("<KeyRelease-Alt_L>", lambda event: self.deleteText())
        self.root.bind("<KeyRelease-Alt_R>", lambda event: self.deleteText())  
    
    def returnGrid(self):
        return "".join(self.grid)
    
    def updateGrid(self, puzzle=None):
        for f in range(len(puzzle)):
            if len(self.canvasList[f+1].find_all()) > 4:
                self.canvasList[f+1].delete(self.canvasList[f+1].find_all()[-1])
            if puzzle[f] != "0":
                self.canvasList[f+1].create_text(43,43, text=puzzle[f], anchor=CENTER, fill="black", font=("OCR A Extended", 35), tag="num")
            self.grid[f] = puzzle[f]

    def createEntry(self, x, y):
        entry = Entry(self.root, font=("OCR A Extended", 7), width=85)
        self.entryList.append(entry)
        entry.place(x=x, y=y)

    def createButton(self, x, y, text, command=None):
        button = Button(self.root, bg="#00f957", activebackground="red", text=text, relief="flat", overrelief="flat", padx="10p", pady="5p", font=("OCR A Extended", 25), command=command)
        button.place(x=x, y=y)
        
    def autosolve(self):
        puzzle = SudokuGrid(self.returnGrid())
        self.updateGrid(puzzle.mainLoop())