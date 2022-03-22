from sudokuGridClass import SudokuGrid

def main():
  puzzleInput = input("Enter the puzzle as one continous string of digits, where unknown digits are represented by 0s: \n")
  puzzle = SudokuGrid(puzzleInput)
  print("Your puzzle input:")
  puzzle.printGrid()
  input("Press enter to solve")
  puzzle.mainLoop()
  

def hell():
  puzzle = SudokuGrid("000000000000000000000000000000000000000000000000000000000000000000000000000000000")
  puzzle.returnClashes()
  
  
hell()