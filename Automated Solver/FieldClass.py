from tempfile import TemporaryFile


class Field:
    """
    Every object of this class represents a single cell on the sudoku grid. An object of this class has three main attributes:
    Private Integer Value - The actual value of the cell. This will be the same as the value that is displayed to the user graphically. If the cell has no value (Meaning there is more than one possibility for that cell), its value will be set to 0.
    Private List Possibilities- The possibilities that a cell can take. Unless a cell is specified as a clue, it will start out as the digits from 1-9 (inclusive), as per the rules of sudoku. However, when the cell is inputted as a clue, the only element in the list will be the value of that cell.
    Priate Boolean IsClue - Whether or not the cell is a clue. A clue is defined as a cell that has a single possibility. Clues can be given at the start at the puzzle and are discovered until all cells on the grid are considered clues.
    """
    
    def __init__(self, value=0):
        self.__value = value
        if self.__value != 0:
        #Checks whether or not the cell has a given digit. If it is, then the list of possibilities is set to only the value of that cell and sets the value of the flag isClue to True, but if not, the possibilities is the digits from 1-9 and sets the value of isClue is False.
            self.__possibilities = [value]
            self.__isClue = True
        else:
            self.__possibilities = list(x for x in range(1,10))
            self.__isClue = False
        
    def checkValue(self):
        if len(self.__possibilities) == 1:
        #Checks whether the length of the list of possibilities is 1 (suggesting that the cell only has one possibility). If this is true, it sets the value of the attribute value to the only element of possibilites and changes the boolean isClue to True.
            self.__value = self.__possibilities[0]
            return 1
        else:
            return 0
    
    def getValue(self):
    #Returns the value of the attribute value.
        return self.__value
    
    def isClue(self):
    #Returns the boolean value of the attribute isClue.
        return self.__isClue
    
    def removePossibility(self, digit):
        if len(self.__possibilities) != 1:
        #Checks whether the cell has multiple possibilities or not. If it does, it removes the digit passed into the method as a possibility of that cell. If the digit is not already a possibility in that cell, it prints a message to the command line stating so.
            try:
                self.__possibilities.remove(digit)
                self.checkValue()
                print(f"{digit} has been removed from cell")
            except ValueError:
                print(f"{digit} is not a possibility in cell")
        else:
            print("Cell has an absolute value")
    
    def resetPossibilities(self):
    #Checks whether the cell is a clue. If it is, it will be passed over. If not, it resets the list of possibilities to be the digits from 1-9.
        if self.isClue():
            return 0
        else:
            self.__possibilities = list(x for x in range(1,10))
            self.__value = 0
            return 1
    
    def returnPossibilities(self):
    #Returns the list of possibilities for that specific cell.
        return self.__possibilities