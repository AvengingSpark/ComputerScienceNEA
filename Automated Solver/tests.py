from sudokuGridClass import SudokuGrid


#test1 = SudokuGrid({"[0][1]": 4, "[0][2]": 9, "[0][6]": 8, "[0][8]": 7, "[1][4]": 1, "[1][6]": 4, "[2][0]": 3, "[2][2]": 2, "[2][5]": 7, "[2][8]": 6, "[3][1]": 6, "[3][2]": 4, "[3][3]": 7, "[3][4]": 2, "[3][5]": 1, "[3][6]": 5, "[3][7]": 3, "[4][0]": 2, "[4][1]": 8, "[4][2]": 5, "[4][3]": 4, "[4][5]": 9, "[4][6]": 7, "[4][7]": 6, "[5][4]": 8, "[5][6]": 2, "[5][7]": 9, "[6][3]": 3, "[6][5]": 4, "[6][6]": 6, "[7][0]": 4, "[7][2]": 8, "[7][3]": 1, "[7][4]": 6, "[8][1]": 3, "[8][8]": 2})
#test1.printBoxes()
#digitInRowTest = SudokuGrid({"[0][0]": 4, "[0][1]": 3, "[0][2]": 2, "[0][3]": 1, "[0][5]": 9, "[0][6]": 7, "[0][7]": 8, "[0][8]": 5})
#print(digitInRowTest.grid[0][4].returnPossibilities())
#digitInRowTest.printGrid()
#digitInRowTest.digitInRow()
#digitInRowTest.printGrid()
#print(digitInRowTest.grid[0][4].returnPossibilities())
#input()

digitInColumnTest = SudokuGrid({"[0][0]": 4, "[1][0]": 1, "[2][0]": 3, "[3][0]": 2, "[5][0]": 9, "[6][0]": 5, "[7][0]": 6, "[8][0]": 7})
digitInColumnTest.printGrid()
digitInColumnTest.digitInColumn()
digitInColumnTest.printGrid()
input()