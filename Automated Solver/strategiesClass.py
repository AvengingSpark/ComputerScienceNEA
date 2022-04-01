class Strategies:

    def digitInRow(self):
    #Checks within each row of the grid, if a single digit appears in that row, whether it be a clue or a digit that the solver have discovered, it adds it to a list of digits to remove. Then these digits are removed as possibilities from all other cells within that row
        starterGrid = self.getGridValues()
        for row in range(9):
        #Loops through 9 times as per the number of rows in a sudoku puzzle
            digitsToRemove = []
            for cell in range(9):
            #Loops through 9 times as per the number of cells in a row of the sudoku Grid
                if len(self.grid[row][cell].returnPossibilities()) == 1:
                    digitsToRemove.append(self.grid[row][cell].getValue())
            for toRemove in range(len(digitsToRemove)):
            #Loops through as per the number of digits that should be removed from each cell within the Grid
                for cell in range(9):
                #Loops through 9 times as per the number of cells in a row of the sudoku Grid
                    self.grid[row][cell].removePossibility(digitsToRemove[toRemove])
        if self.getGridValues() == starterGrid:
            return False
        else:
            return True

    def pairInRow(self):
        starterGrid = self.getGridValues()
        for row in range(9):
            pairs = []
            for cell in range(9):
                if len(self.grid[row][cell].returnPossibilities()) == 2:
                    pairs.append(self.grid[row][cell].returnPossibilities())
            toRemove = []
            for possibilities in range(len(pairs)):
                if pairs.count(pairs[possibilities]) == 2:
                    for f in range(len(pairs[possibilities])):
                        if not(pairs[possibilities][f] in toRemove):
                            toRemove.append(pairs[possibilities][f])
            for cell in range(9):
                for digit in range(len(toRemove)):
                    if not (self.grid[row][cell].returnPossibilities() in pairs):
                        self.grid[row][cell].removePossibility(toRemove[digit])
            if self.getGridValues == starterGrid:
                return False
            else:
                return True

    def digitInColumn(self):
    #Checks within each row of the grid, if a single digit appears in that column, whether it be a clue or a digit that the solver have discovered, it adds it to a list of digits to remove. Then these digits are removed as possibilities from all other cells within that column
        starterGrid = self.getGridValues()
        for column in range(9):
        #Loops through 9 times as per the number of columns in a sudoku grid
            digitsToRemove = []
            for cell in range(9):
            #Loops through 9 times as per the number of cells in a column of the sudoku Grid
                if len(self.grid[cell][column].returnPossibilities()) == 1:
                    digitsToRemove.append(self.grid[cell][column].getValue())
            for toRemove in range(len(digitsToRemove)):
            #Loops through as per the number of digits that should be removed from each cell within the Grid
                for cell in range(9):
                #Loops through 9 times as per the number of cells in a column of the sudoku Grid
                    self.grid[cell][column].removePossibility(digitsToRemove[toRemove])
        if self.getGridValues() == starterGrid:
            return False
        else:
            return True

    def pairInColumn(self):
        starterGrid = self.getGridValues()
        for column in range(9):
            pairs = []
            for cell in range(9):
                if len(self.grid[cell][column].returnPossibilities()) == 2:
                    pairs.append(self.grid[cell][column].returnPossibilities())
            toRemove = []
            for possibilities in range(len(pairs)):
                if pairs.count(pairs[possibilities]) == 2:
                    for f in range(len(pairs[possibilities])):
                        if not(pairs[possibilities][f] in toRemove):
                            toRemove.append(pairs[possibilities][f])
            for cell in range(9):
                for digit in range(len(toRemove)):
                    if not (self.grid[cell][column].returnPossibilities() in pairs):
                        self.grid[cell][column].removePossibility(toRemove[digit])
            if self.getGridValues == starterGrid:
                return False
            else:
                return True

    def pairInBox(self):
        starterGrid = self.getGridValues()
        for box in range(9):
            pairs = []
            for row in range(3):
                for cell in range(3):
                    if len(self.boxes[box][row][cell].returnPossibilities()) == 2:
                        pairs.append(self.boxes[box][row][cell].returnPossibilities())
            toRemove = []
            for possibilities in range(len(pairs)):
                if pairs.count(pairs[possibilities]) == 2:
                    for f in range(len(pairs[possibilities])):
                        if not(pairs[possibilities][f] in toRemove):
                            toRemove.append(pairs[possibilities][f])
                for row in range(3):
                    for cell in range(3):
                        for digit in range(len(toRemove)):
                            if not (self.boxes[box][row][cell].returnPossibilities()) in pairs:
                                self.boxes[box][row][cell].removePossibility(toRemove[digit])
        if self.getGridValues == starterGrid:
            return False
        else:
            return True

    def digitInBox(self):
    #Checks within each row of the grid, if a single digit appears in that box, whether it be a clue or a digit that the solver have discovered, it adds it to a list of digits to remove. Then these digits are removed as possibilities from all other cells within that box
        starterGrid = self.getGridValues()
        for box in range(9):
        #Loops through 9 times as per the number of boxes in a sudoku grid, and
            digitsToRemove = []
            for row in range(3):
            #Loops through 3 times as per the number of rows within a box of the sudoku grid
                for cell in range(3):
                #Loops through 3 times as per the number of cells within a row of a box within the Grid
                    if len(self.boxes[box][row][cell].returnPossibilities()) == 1:
                        digitsToRemove.append(self.boxes[box][row][cell].getValue())
            for toRemove in range(len(digitsToRemove)):
            #Loops through as per the number of digits that should be removed from each cell within the Grid
                for row in range(3):
                #Loops through 3 times as per the number of rows within a box of the sudoku grid
                    for cell in range(3):
                    #Loops through 3 times as per the number of cells within a row of a box within the Grid
                        self.boxes[box][row][cell].removePossibility(digitsToRemove[toRemove])
        if self.getGridValues() == starterGrid:
            return False
        else:
            return True

    def singleInRow(self):
    #Iterates through each row of the grid and totals the number of occurances of that digit. Then checks a dictionary of all occurances of each digit, if there is one occurance within that row, it must be the only location of that digit within that row
        starterGrid = self.getGridValues()
        for row in range(9):
        #Loops through 9 times as per the number of rows in the Sudoku Grid and
            occurances = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
            for cell in range(9):
            #Loops through 9 times as per the number of cells in a row of the sudoku Grid
                for possibility in self.grid[row][cell].returnPossibilities():
                    if not self.grid[row][cell].isClue():
                        occurances[possibility].append(f"[{row}][{cell}]")
            for occurance in occurances:
                if len(occurances[occurance]) == 1:
                    for cell in range(9):
                    #Loops through 9 times as per the number of cells in a row of the sudoku Grid
                        if (f"[{row}][{cell}]") == occurances[occurance][0]:
                            for num in range(1,10):
                                if num != occurance:
                                    self.grid[row][cell].removePossibility(num)
        if self.getGridValues() == starterGrid:
            return False
        else:
            return True

    def singleInColumn(self):
    #Iterates through each column of the grid and totals the number of occurances of that digit. Then checks a dictionary of all occurances of each digit, if there is one occurance within that column, it must be the only location of that digit within that columnd
        starterGrid = self.getGridValues()
        for column in range(9):
        #Iterates through 9 times as per the number of columns in a sudoku grid and
            occurances = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
            for cell in range(9):
            #Iterates through 9 times as per the number of cells in a column of the sudoku Grid
                for possibility in self.grid[cell][column].returnPossibilities():
                    if not self.grid[cell][column].isClue():
                        occurances[possibility].append(f"[{cell}][{column}]")
            for occurance in occurances:
                if len(occurances[occurance]) == 1:
                    for cell in range(9):
                    #Iterates through 9 times as per the number of cells in a column of the sudoku Grid
                        if (f"[{cell}][{column}]") == occurances[occurance][0]:
                            for num in range(1,10):
                                if num != occurance:
                                    self.grid[cell][column].removePossibility(num)
        if self.getGridValues() == starterGrid:
            return False
        else:
            return True

    def singleInBox(self):
    #Iterates through each box of the grid and totals the number of occurances of that digit. Then checks a dictionary of all occurances of each digit, if there is one occurance within that box, it must be the only location of that digit within that box
        starterGrid = self.getGridValues()
        for box in range(9):
        #Iterates through 9 times as per the number of boxes in a sudoku grid
            occurances = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
            for row in range(3):
            #Iterates through 3 times as per the number of rows in a box of the sudoku Grid
                for cell in range(3):
                #Iterates through 3 times as per the number of cells in a row of a box within the sudoku Grid
                    for possibility in self.boxes[box][row][cell].returnPossibilities():
                        occurances[possibility].append(f"[{box}][{row}][{cell}]")
            for occurance in occurances:
                if len(occurances[occurance]) == 1:
                    for row in range(3):
                    #Loops through 3 times as per the number of rows in a box of the sudoku Grid
                        for cell in range(3):
                        #Iterates through 3 times as per the number of cell in a row of a box in the sudoku grid
                            if (f"[{box}][{row}][{cell}]") == occurances[occurance][0]:
                                for num in range(1,10):
                                    if num != occurance:
                                        self.boxes[box][row][cell].removePossibility(num)
        if self.getGridValues() == starterGrid:
            return False
        else:
            return True

    def checkClashesInRow(self):
        clash = False
        #Searches through every row of the grid and collects the number of occurances that appear in each row. If a non 0 value appears more than once, a rule of sudoku has been broken
        for row in range(len(self.grid)):
            occurances = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            for cell in range(len(self.grid[row])):
                occurances[self.grid[row][cell].getValue()] += 1
            for occurance in occurances:
                if occurance != 0 and occurances[occurance] > 1:
                    print(f"Clash in row: {row+1}")
        return clash

    def checkClashesInColumn(self):
        clash = False
        #Searches through every column of the grid and collects the number of occurances that appear in each row. If a non 0 value appears more than once, a rule of sudoku has been broken
        for column in range(len(self.grid)):
            occurances = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            for cell in range(len(self.grid[column])):
                occurances[self.grid[cell][column].getValue()] += 1
            for occurance in occurances:
                if occurance != 0 and occurances[occurance] > 1:
                    print(f"Clash in column: {column+1}")
        return clash

    def checkClashesInBox(self):
        clash = False
        for box in range(len(self.boxes)):
            occurances = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            for row in range(len(self.boxes[box])):
                for cell in range(len(self.boxes[box][row])):
                    occurances[self.boxes[box][row][cell].getValue()] += 1
            for occurance in occurances:
                if occurance != 0 and occurances[occurance] > 1:
                    print(f"Clash in box {box+1}")
                    clash = True
        return clash

    def returnClashesInRow(self):
        clash = []
        #Searches through every row of the grid and collects the number of occurances that appear in each row. If a non 0 value appears more than once, a rule of sudoku has been broken
        for row in range(len(self.grid)):
            occurances = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            for cell in range(len(self.grid[row])):
                occurances[self.grid[row][cell].getValue()] += 1
            for occurance in occurances:
                if occurance != 0 and occurances[occurance] > 1:
                    print(f"Clash in row: {row+1}")
                    for cell in range(len(self.grid[row])):
                        if self.grid[row][cell].getValue() == occurance:
                            clash.append(((row)*9)+cell+1)
        if clash != []:
            return clash

    def returnClashesInColumn(self):
        clash = []
        #Searches through every column of the grid and collects the number of occurances that appear in each column. If a non 0 value appears more than once, a rule of sudoku has been broken
        for column in range(len(self.grid)):
            occurances = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            for cell in range(len(self.grid[column])):
                occurances[self.grid[cell][column].getValue()] += 1
            for occurance in occurances:
                if occurance != 0 and occurances[occurance] > 1:
                    print(f"Clash in column: {column+1}")
                    for cell in range(len(self.grid[column])):
                        if self.grid[cell][column].getValue() == occurance:
                            print(f"{(cell*9)+column+1}")
                            clash.append((cell*9)+column+1)
        if clash != []:
            return clash

    def returnClashesInBox(self):
        digits = [[[1,2,3],[10,11,12],[19,20,21]],[[4,5,6],[13,14,15],[22,23,24]],[[7,8,9],[16,17,18],[25,26,27]],[[28,29,30],[37,38,39],[46,47,48]],[[31,32,33],[40,41,42],[49,50,51]],[[34,35,36],[43,44,45],[52,53,54]],[[55,56,57],[64,65,66],[73,74,75]],[[58,59,60],[67,68,69],[76,77,78]],[[61,62,63],[70,71,72],[79,80,81]]]
        clash = []
        #Searches through each box of the grid and collects the number of occurances that appear in each box. If a non 0 value appears more than once, a rule of sudoku has been broken
        for box in range(len(self.boxes)):
            occurances = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            for row in range(len(self.boxes[box])):
                for cell in range(len(self.boxes[box][row])):
                    occurances[self.boxes[box][row][cell].getValue()] += 1
            for occurance in occurances:
                if occurance != 0 and occurances[occurance] > 1:
                    print(f"Clash in box {box+1}")
                    for row in range(len(self.boxes[box])):
                        for cell in range(len(self.boxes[box][row])):
                            if self.boxes[box][row][cell].getValue() == occurance:
                                clash.append(digits[box][row][cell])
        if clash != []:
            return clash


    def checkClashes(self):
        return self.checkClashesInRow() or self.checkClashesInColumn() or self.checkClashesInBox()
    
    def returnClashes(self):
        clashes = []
        row = self.returnClashesInRow()
        column = self.returnClashesInColumn()
        box = self.returnClashesInBox()
        if row != None:
            clashes.append(row)
        if column != None:
            clashes.append(column)
        if box != None:
            clashes.append(box)
        return clashes

    def removeDigits(self):
        self.digitInRow()
        self.digitInColumn()
        self.digitInBox()
        self.pairInRow()
        self.pairInColumn()
        self.pairInBox()