from FieldClass import Field
from strategiesClass import Strategies

class SudokuGrid(Strategies):
    """
    Every instance of this class respresents a Sudoku Grid. There should only be one instance of this class at a time. An object of this class has five attributes:
    Private List Grid - The sudoku __grid. This will be a 2D list, where each nested list represents a row within the __grid, and each element within the nested array points to an instance of the Field class (a cell)
    Private Integer numOfClues - This represents the number of clues that are in the sudoku __grid. For a sudoku __grid to be solvable, there must be at least 17 clues in the __grid. This enables there to be a check whenever a __grid is initialised that there are at least 17 clues on the __grid.
    Private Dictionary clueLocations - This will represent where every clue is located on the __grid. It will be formatted as '"[row][cell]": value'. This will be used when generating the __grid to defined what cells can be edited or cannot be edited.
    Private Boolean isSolved - This boolean shows whether the puzzle has been solved or not. Depending on whether all of the cells in the __grid have been filled.
    Private Array Boxes - This 3D array represents the 9 3x3 boxes that make up a sudoku __grid. Each inital nested array refers to one of the 9 boxes, where the other array is a row in the box and each element in a row points to an instance of the class Field
    """

    def __init__(self, clueLocations):
        #The clueLocations parameter is a dictionary which refers to the different clues in the sudoku __grid. 
        self.__grid = []
        self.__numOfClues = len(clueLocations)
        self.__clueLocations = clueLocations
        self.__isSolved = False
        #Calls generateGrid method to populate the __grid with instances of the class Field.
        self.generateGrid()
        #This represents all of the boxes within the sudoku grid. Each nested list represents one of these boxes where the list inside of that list is one of the three rows within that box.
        self.__boxes = [[self.__grid[0][:3], self.__grid[1][:3], self.__grid[2][:3]], [self.__grid[0][3:6], self.__grid[1][3:6], self.__grid[2][3:6]], [self.__grid[0][6:], self.__grid[1][6:], self.__grid[2][6:]], [self.__grid[3][:3], self.__grid[4][:3], self.__grid[5][:3]], [self.__grid[3][3:6], self.__grid[4][3:6], self.__grid[5][3:6]], [self.__grid[3][6:], self.__grid[4][6:], self.__grid[5][6:]], [self.__grid[6][:3], self.__grid[7][:3], self.__grid[8][:3]], [self.__grid[6][3:6], self.__grid[7][3:6], self.__grid[8][3:6]], [self.__grid[6][6:], self.__grid[7][6:], self.__grid[8][6:]]]
        
    def generateGrid(self):
    #This methods populates the sudoku __grid with pointer to instances of the Field class.
        for row in range(9):
            #Loops through 9 times corresponding the 9 row in a sudoku __grid
            newRow = []
            for cell in range(9):
                #Loops through 9 times corresponding the 9 cells in a row of the sudoku __grid.
                if f"[{row}][{cell}]" in self.__clueLocations:
                    #Checks whether the cell is in the dictionary of clue locations using the same string format - if it is, the instance of the field class for that cell will be considered a clue and have a non-0 value.
                    newRow.append(Field(self.__clueLocations[f"[{row}][{cell}]"]))
                else:
                    newRow.append(Field())
            self.__grid.append(newRow)

    def getGrid(self):
    #This function returns the entire Sudoku Grid
        return self.__grid
    
    def printGrid(self):
        for row in self.__grid:
            tempString = ""
            for cell in row:
                tempString += (f"{cell.getValue()}    ")
            print(tempString, "\n")
    
    def printBoxes(self):
        boxNum = 1
        for box in self.__boxes:
            print(f"Box {boxNum}")
            boxNum += 1
            for row in box:
                output = ""
                for cell in row:
                    output += (f"{cell.getValue()}    ")
                print(output, "\n")
    
    def resetGrid(self):
        for row in range(len(self.__grid)):
            for cell in range(len(self.__grid[row])):
                #Iterates through each row and each cell within each row. If the current cell is not a clue, the possibilities of this cell are reset to the digits 1-9
                if not self.__grid[row][cell].isClue():
                    self.__grid[row][cell].resetPossibilities()
    
    def checkIfSolved(self):
    #This function returns the value of the Boolean isSolved
        return self.__isSolved
    
    
test1 = SudokuGrid({"[0][1]": 4, "[0][2]": 9, "[0][6]": 8, "[0][8]": 7, "[1][4]": 1, "[1][6]": 4, "[2][0]": 3, "[2][2]": 2, "[2][5]": 7, "[2][8]": 6, "[3][1]": 6, "[3][2]": 4, "[3][3]": 7, "[3][4]": 2, "[3][5]": 1, "[3][6]": 5, "[3][7]": 3, "[4][0]": 2, "[4][1]": 8, "[4][2]": 5, "[4][3]": 4, "[4][5]": 9, "[4][6]": 7, "[4][7]": 6, "[5][4]": 8, "[5][6]": 2, "[5][7]": 9, "[6][3]": 3, "[6][5]": 4, "[6][6]": 6, "[7][0]": 4, "[7][2]": 8, "[7][3]": 1, "[7][4]": 6, "[8][1]": 3, "[8][8]": 2})
test1.printBoxes()
input()