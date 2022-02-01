class Stragies:
    
    def digitInRow(self):
    #Checks within each row of the grid, if a single digit appears in that row, whether it be a clue or a digit that the solver have discovered, it adds it to a list of digits to remove. Then these digits are removed as possibilities from all other cells within that row
        for row in range(9):
        #Loops through 9 times as per the number of rows in a sudoku puzzle
            digitsToRemove = []
            for cell in range(9):
            #Loops through 9 times as per the number of cells in a row of the sudoku Grid
                if self.__grid[row][cell].isClue():
                    digitsToRemove.append(self.__grid[row][cell].getValue())
            for toRemove in range(len(digitsToRemove)):
            #Loops through as per the number of digits that should be removed from each cell within the Grid
                for cell in range(9):
                #Loops through 9 times as per the number of cells in a row of the sudoku Grid
                    self.__grid[row][cell].removePossibility(toRemove)
    
    def digitInColumn(self):
    #Checks within each row of the grid, if a single digit appears in that column, whether it be a clue or a digit that the solver have discovered, it adds it to a list of digits to remove. Then these digits are removed as possibilities from all other cells within that column
        pass
    
    def digitInBox(self):
    #Checks within each row of the grid, if a single digit appears in that box, whether it be a clue or a digit that the solver have discovered, it adds it to a list of digits to remove. Then these digits are removed as possibilities from all other cells within that box
        pass
    
    def singleInRow(self):
    #Iterates through each row of the grid and totals the number of occurances of that digit. Then checks a dictionary of all occurances of each digit, if there is one occurance within that row, it must be the only location of that digit within that row
        pass
    
    def singleInColumn(self):
        #Iterates through each column of the grid and totals the number of occurances of that digit. Then checks a dictionary of all occurances of each digit, if there is one occurance within that column, it must be the only location of that digit within that columnd
        pass
    
    def singleInBox(self):
    #Iterates through each box of the grid and totals the number of occurances of that digit. Then checks a dictionary of all occurances of each digit, if there is one occurance within that box, it must be the only location of that digit within that box
        pass