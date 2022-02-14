from sudokuGridClass import SudokuGrid


# test1 = SudokuGrid({"[0][1]": 4, "[0][2]": 9, "[0][6]": 8, "[0][8]": 7, "[1][4]": 1, "[1][6]": 4, "[2][0]": 3, "[2][2]": 2, "[2][5]": 7, "[2][8]": 6, "[3][1]": 6, "[3][2]": 4, "[3][3]": 7, "[3][4]": 2, "[3][5]": 1, "[3][6]": 5, "[3][7]": 3, "[4][0]": 2, "[4][1]": 8, "[4][2]": 5, "[4][3]": 4, "[4][5]": 9, "[4][6]": 7, "[4][7]": 6, "[5][4]": 8, "[5][6]": 2, "[5][7]": 9, "[6][3]": 3, "[6][5]": 4, "[6][6]": 6, "[7][0]": 4, "[7][2]": 8, "[7][3]": 1, "[7][4]": 6, "[8][1]": 3, "[8][8]": 2})
# test1.printBoxes()
# digitInRowTest = SudokuGrid({"[0][0]": 4, "[0][1]": 3, "[0][2]": 2, "[0][3]": 1, "[0][5]": 9, "[0][6]": 7, "[0][7]": 8, "[0][8]": 5})
# print(digitInRowTest.grid[0][4].returnPossibilities())
# digitInRowTest.printGrid()
# digitInRowTest.digitInRow()
# digitInRowTest.printGrid()
# print(digitInRowTest.grid[0][4].returnPossibilities())


# digitInRowTest = SudokuGrid({"[0][0]": 4, "[0][1]": 1, "[0][2]": 3, "[0][4]": 6, "[0][5]": 2, "[0][6]": 9, "[0][7]": 5, "[0][8]": 7, "[5][0]": 1, "[5][1]": 3, "[5][2]": 6, "[5][3]": 7, "[5][4]": 9, "[5][5]": 4, "[5][7]": 2, "[5][8]": 8})
# print(digitInRowTest.grid[0][3].returnPossibilities())
# print(digitInRowTest.grid[5][6].returnPossibilities())
# digitInRowTest.printGrid()
# digitInRowTest.digitInRow()
# digitInRowTest.printGrid()
# print(digitInRowTest.grid[0][3].returnPossibilities())
# print(digitInRowTest.grid[5][6].returnPossibilities())


# digitInColumnTest = SudokuGrid({"[0][0]": 4, "[1][0]": 1, "[2][0]": 3, "[3][0]": 2, "[5][0]": 9, "[6][0]": 5, "[7][0]": 6, "[8][0]": 7})
# digitInColumnTest.printGrid()
# digitInColumnTest.digitInColumn()
# digitInColumnTest.printGrid()
# digitInColumnTest = SudokuGrid({"[0][0]": 1, "[1][0]": 4, "[3][0]": 9, "[4][0]": 6, "[5][0]": 3, "[6][0]": 2, "[7][0]": 8, "[8][0]": 7, "[0][6]": 4, "[1][6]": 2, "[2][6]": 1, "[3][6]": 9, "[4][6]": 5, "[5][6]": 6, "[7][6]": 8, "[8][6]": 3})
# digitInColumnTest.printGrid()
# digitInColumnTest.digitInColumn()
# digitInColumnTest.printGrid()


# digitInBoxTest = SudokuGrid({"[0][0]": 2, "[0][1]": 8, "[0][2]": 5, "[1][0]": 7, "[1][2]": 4, "[2][0]": 9, "[2][1]": 3, "[2][2]": 1})
# digitInBoxTest.printGrid()
# digitInBoxTest.digitInBox()
# digitInBoxTest.printGrid()
# digitInBoxTest = SudokuGrid({"[0][0]": 7, "[0][1]": 5, "[0][2]": 1, "[1][1]": 3, "[1][2]": 4, "[2][0]": 2, "[2][1]": 8, "[2][2]": 9, "[6][3]": 3, "[6][4]": 4, "[6][5]": 1, "[7][3]": 9, "[7][4]": 6, "[7][5]": 7, "[8][3]": 2, "[8][4]": 8})
# digitInBoxTest.printGrid()
# digitInBoxTest.digitInBox()
# digitInBoxTest.printGrid()


# singleInRowTest = SudokuGrid({"[3][0]": 5, "[3][2]": 9, "[3][3]": 1, "[3][4]": 2, "[3][5]": 8, "[3][7]": 3, "[5][7]": 4})
# singleInRowTest.printGrid()
# print(singleInRowTest.grid[3][1].returnPossibilities())
# print(singleInRowTest.grid[3][6].returnPossibilities())
# print(singleInRowTest.grid[3][8].returnPossibilities())
# singleInRowTest.digitInRow()
# singleInRowTest.digitInColumn()
# singleInRowTest.digitInBox()
# singleInRowTest.printGrid()
# print(singleInRowTest.grid[3][1].returnPossibilities())
# print(singleInRowTest.grid[3][6].returnPossibilities())
# print(singleInRowTest.grid[3][8].returnPossibilities())
# singleInRowTest.singleInRow()
# print("\n"*5)
# singleInRowTest.printGrid()
# print(singleInRowTest.grid[3][1].returnPossibilities())
# print(singleInRowTest.grid[3][6].returnPossibilities())
# print(singleInRowTest.grid[3][8].returnPossibilities())


# singleInColumnTest = SudokuGrid({"[0][0]": 5, "[1][4]": 8, "[2][0]": 7, "[3][0]": 2, "[4][0]": 1, "[6][0]": 3, "[7][0]": 9, "[7][2]": 8})
# singleInColumnTest.printGrid()
# singleInColumnTest.digitInRow()
# singleInColumnTest.digitInColumn()
# singleInColumnTest.digitInBox()
# singleInColumnTest.singleInColumn()
# singleInColumnTest.printGrid()

# singleInBoxTest = SudokuGrid({"[0][0]": 1, "[0][1]": 4, "[0][2]": 5, "[1][1]": 3, "[2][1]": 8, "[2][2]": 9, "[7][0]": 6})
# singleInBoxTest.printGrid()
# singleInBoxTest.digitInRow()
# singleInBoxTest.digitInColumn()
# singleInBoxTest.digitInBox()
# singleInBoxTest.singleInBox()
# singleInBoxTest.printGrid()

# testInput = SudokuGrid("000003600031642800007090004000407098000500006006000702090000507042010000670908400")
# # print(testInput.getGrid())
# testInput.printGrid()

# clashInRowTest = SudokuGrid("040000400000000000200200000000000000001000001000000000000000000000500050000000000")
# clashInRowTest.printGrid()
# clashInRowTest.checkClashesInRow()

clashInColumnTest = SudokuGrid("010400009000002000000000000010000009000400000000002000010002000000000009000400000")
clashInColumnTest.printGrid()
clashInColumnTest.checkClashesInColumn()

input()