from FieldClass import Field
from strategiesClass import Strategies

class SudokuGrid(Strategies):
    """
    Every instance of this class respresents a Sudoku Grid. There should only be one instance of this class at a time. An object of this class has five attributes:
    Private List Grid - The sudoku grid. This will be a 2D list, where each nested list represents a row within the grid, and each element within the nested array points to an instance of the Field class (a cell)
    Private Integer numOfClues - This represents the number of clues that are in the sudoku grid. For a sudoku grid to be solvable, there must be at least 17 clues in the grid. This enables there to be a check whenever a grid is initialised that there are at least 17 clues on the grid.
    Private Dictionary clueLocations - This will represent where every clue is located on the grid. It will be formatted as '"[row][cell]": value'. This will be used when generating the grid to defined what cells can be edited or cannot be edited.
    Private Boolean isSolved - This boolean shows whether the puzzle has been solved or not. Depending on whether all of the cells in the grid have been filled.
    Private Array Boxes - This 3D array represents the 9 3x3 boxes that make up a sudoku grid. Each inital nested array refers to one of the 9 boxes, where the other array is a row in the box and each element in a row points to an instance of the class Field
    """

    def __init__(self, clueLocations):
        #The clueLocations parameter is a dictionary which refers to the different clues in the sudoku grid. 
        self.grid = []
        self.__numOfClues = len(clueLocations)
        self.__clueLocations = clueLocations
        self.__isSolved = False
        #Calls generateGrid method to populate the grid with instances of the class Field.
        self.generateGrid()
        #This represents all of the boxes within the sudoku grid. Each nested list represents one of these boxes where the list inside of that list is one of the three rows within that box.
        self.__boxes = [[self.grid[0][:3], self.grid[1][:3], self.grid[2][:3]], [self.grid[0][3:6], self.grid[1][3:6], self.grid[2][3:6]], [self.grid[0][6:], self.grid[1][6:], self.grid[2][6:]], [self.grid[3][:3], self.grid[4][:3], self.grid[5][:3]], [self.grid[3][3:6], self.grid[4][3:6], self.grid[5][3:6]], [self.grid[3][6:], self.grid[4][6:], self.grid[5][6:]], [self.grid[6][:3], self.grid[7][:3], self.grid[8][:3]], [self.grid[6][3:6], self.grid[7][3:6], self.grid[8][3:6]], [self.grid[6][6:], self.grid[7][6:], self.grid[8][6:]]]
        
    def generateGrid(self):
    #This methods populates the sudoku grid with pointer to instances of the Field class.
        for row in range(9):
            #Loops through 9 times corresponding the 9 row in a sudoku grid
            newRow = []
            for cell in range(9):
                #Loops through 9 times corresponding the 9 cells in a row of the sudoku grid.
                if f"[{row}][{cell}]" in self.__clueLocations:
                    #Checks whether the cell is in the dictionary of clue locations using the same string format - if it is, the instance of the field class for that cell will be considered a clue and have a non-0 value.
                    newRow.append(Field(self.__clueLocations[f"[{row}][{cell}]"]))
                else:
                    newRow.append(Field())
            self.grid.append(newRow)

    def getGrid(self):
    #This function returns the entire Sudoku Grid
        return self.grid
    
    def printGrid(self):
        for row in self.grid:
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
        for row in range(len(self.grid)):
            for cell in range(len(self.grid[row])):
                #Iterates through each row and each cell within each row. If the current cell is not a clue, the possibilities of this cell are reset to the digits 1-9
                if not self.grid[row][cell].isClue():
                    self.grid[row][cell].resetPossibilities()
    
    def checkIfSolved(self):
    #This function returns the value of the Boolean isSolved
        return self.__isSolved
