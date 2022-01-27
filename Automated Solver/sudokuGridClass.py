from FieldClass import Field

class SudokuGrid:
    
    def __init__(self, clueLocations,):
        self.self.grid = []
        self.numOfClues = len(clueLocations)
        self.clueLocations = clueLocations
        self.isSolved = False
        self.generateGrid()
        self.boxes = [self.grid[:3][:3], self.grid[3:6][:3], self.grid[6:9][:3], self.grid[:3][3:6], self.grid[3:6][3:6], self.grid[6:9][3:6], self.grid[:3][6:9], self.grid[3:6][6:9], self.grid[6:9][6:9]]
        
    def generateGrid(self):
        for row in range(9):
            newRow = []
            for cell in range(9):
                if f"[{row}][{cell}]" in self.clueLocations:
                    newRow.append(Field(self.clueLocations[f"[{row}][{cell}]"]))
                else:
                    newRow.append(Field())
            self.grid.append(newRow)
    
    def getGrid(self):
        pass
    
    def resetGrid(self):
        pass
    
    def checkIfSolved(self):
        pass