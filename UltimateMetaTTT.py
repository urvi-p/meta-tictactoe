#----------------------------------------------------
# This file contains Tic Tac Toe classes
# References: python 3 documentation
# Author: Urvi Patel
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = []
        self.size = 3
        
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        squaresList = []
        for row in self.board:
            for col in row:
                if col == 0:
                    fill = " "
                    squaresList.append(fill)
                else:
                    fill = col
                    squaresList.append(str(fill))
                            
        topLine = "   0   1   2"
        separator = "\n  -----------"
        lineOne ="0  "+squaresList[0]+" | "+squaresList[1]+" | "+squaresList[2]
        lineTwo = "1  "+squaresList[3]+" | "+squaresList[4]+" | "+squaresList[5]
        lineThree = "2  "+squaresList[6]+" | "+squaresList[7]+" | "+squaresList[8]
        print(topLine, "\n"+lineOne, separator, "\n"+lineTwo, separator, "\n"+lineThree)        

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        if self.board[row][col] == 0:
            empty = True
        else:
            empty = False
        return empty
        
    def update(self, row, col, mark):
        '''
        Assigns the integer, mark, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row,col):
            self.board[row][col] = mark
            updated = True
        else:
            updated = False
            
        return updated
        
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''       
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        return True
                   
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # checks each row
        for row in self.board:
            if sum(row) == 15 and all(col!=0 for col in row):
                    return True
        
        # checks each column
        for colIndex in range(self.size):
            col = []
            for row in self.board:
                col.append(row[colIndex])
            if sum(col) == 15 and all(element!=0 for element in col):
                return True
        
        # checks each diagonal
        diag1 = []
        diag2 = []
        for index in range(self.size):
            diag1.append(self.board[index][index])
            diag2.append(self.board[index][2-index])
        diag1Check = sum(diag1) == 15 and all(element!=0 for element in diag1)
        diag2Check = sum(diag2) == 15 and all(element!=0 for element in diag2)
        if diag1Check or diag2Check:
            return True
        
        return False        
    
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: True
        '''
        return True      


class ClassicTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Classic Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = []
        self.size = 3
        
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(' ')
            self.board.append(row)        
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        squaresList = []
        for row in self.board:
            for col in row:
                squaresList.append(str(col))
                    
        topLine = "   0   1   2"
        separator = "\n  -----------"
        lineOne ="0  "+squaresList[0]+" | "+squaresList[1]+" | "+squaresList[2]
        lineTwo = "1  "+squaresList[3]+" | "+squaresList[4]+" | "+squaresList[5]
        lineThree = "2  "+squaresList[6]+" | "+squaresList[7]+" | "+squaresList[8]
        print(topLine, "\n"+lineOne, separator, "\n"+lineTwo, separator, "\n"+lineThree)   

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains an X or O.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        if self.board[row][col] == ' ':
            empty = True
        else:
            empty = False
        return empty
        
    def update(self, row, col, mark):
        '''
        Assigns the string, mark, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row,col):
            self.board[row][col] = mark
            updated = True
        else:
            updated = False
            
        return updated        

    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''        
        for row in self.board:
            for col in row:
                if str(col) == ' ':
                    return False
        return True
                 
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) with 
        matching marks (i.e. 3 Xs  or 3 Os). That line can be horizontal, vertical,
        or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # checks each row
        for row in self.board:
            if all(element == "X" for element in row) or all(element == 'O' for element in row):
                return True
        
        # checks each column
        for colIndex in range(self.size):
            col = []
            for row in self.board:
                col.append(row[colIndex])
            if all(element=="X" for element in col) or all(element == "O" for element in col) :
                return True
        
        # checks each diagonal
        diag1 = []
        diag2 = []
        for index in range(self.size):
            diag1.append(self.board[index][index])
            diag2.append(self.board[index][2-index])
        diag1Win = all(element == "X" for element in diag1) or all(element == "O" for element in diag1) 
        diag2Win = all(element == "X" for element in diag2) or all(element == "O" for element in diag2)
        if diag1Win or diag2Win:
            return True
            
        return False  
    
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: False
        '''
        return False    


class MetaTicTacToe:
    def __init__(self, configFile):
        '''
        Initializes an empty Meta Tic Tac Toe board, based on the contents of a configuration file.
        Inputs: 
           configFile (str) - name of a text file containing configuration information
        Returns: None
        '''       
        self.board = []
        self.size = 3   
        
        file = open(configFile, "r")
        for line in file:
            line = line.strip()
            for element in line:
                element = line.split()
            self.board.append(element)
                            
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''            
        topLine = "   0   1   2"
        separator = "\n  -----------"
        lineOne = "0  "+self.board[0][0]+" | "+self.board[0][1]+" | "+self.board[0][2]
        lineTwo = "1  "+self.board[1][0]+" | "+self.board[1][1]+" | "+self.board[1][2]
        lineThree = "2  "+self.board[2][0]+" | "+self.board[2][1]+" | "+self.board[2][2]
        print(topLine, "\n"+lineOne, separator, "\n"+lineTwo, separator, "\n"+lineThree)        
    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square contains a non-played local game board ("empty"),
        or the result of a played local game board (not "empty").
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        if self.board[row][col] in ['c','n']:
            return True
        else:
            return False
        
    def update(self, row, col, result):
        '''
        Assigns the string, result, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           result (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row,col):
            self.board[row][col] = result
            return True
        else:
            return False
        
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares (i.e. any un-played
        local boards).
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        for row in self.board:
            for col in row:
                if col in ['c','n']:
                    return False
        return True        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) of their
        mark (three Xs for Player 1, three Os for Player 2), or 3 draws. That line
        can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''        
        #check row
        for row in self.board:
            if row[0] in ['X', 'O', 'D']:
                if all(col == row[0] for col in row):
                    return True
                
        #check column
        for colIndex in range(self.size):
            col = []
            for row in self.board:
                col.append(row[colIndex])
            if col[0] in ['X', 'O', 'D']:
                if all(element==col[0] for element in col):
                    return True        
                
        #check diagonal
        diag1 = []
        diag2 = []
        for index in range(self.size):
            diag1.append(self.board[index][index])
            diag2.append(self.board[index][2-index])
        if self.board[1][1] in ['X', 'O', 'D']:
            diag1Win = all(element == diag1[0] for element in diag1)
            diag2Win = all(element == diag2[0] for element in diag2)
            if diag1Win or diag2Win:
                return True
            
        return False               
                   
    def getLocalBoard(self, row, col):
        '''
        Returns the instance of the empty local board at the specified row, col 
        location (i.e. either ClassicTicTacToe or NumTicTacToe).
        Inputs:
           row (int) - row index of square
           col (int) - column index of square
        Returns: instance of appropriate empty local board if un-played; 
                 None if local board has already been played
        '''
        localBoard = None
        if self.board[row][col] == 'c':
            localBoard = ClassicTicTacToe()
        elif self.board[row][col] == 'n':
            localBoard = NumTicTacToe()
            
        return localBoard


if __name__ == "__main__":
    # TEST EACH CLASS THOROUGHLY HERE
    # to test, uncomment the function call at the bottom for the class you want to test
    # and uncomment each test(one at a time)to check if win each row, col, and diag work
    
    def test_NumTicTacToe():
        '''
        Test NumTicTacToe class
        '''        
        # start by creating empty board and checking the contents of the board attribute    
        myBoard = NumTicTacToe()
        print('Contents of board attribute when object first created:')
        print(myBoard.board)
        
        # check if the empty board displays properly
        myBoard.drawBoard()
            
        # check if square is empty
        print("square empty(1,1):",myBoard.squareIsEmpty(1,1))            
    
        # assign a number to an empty square and display
        myBoard.board[1][1] = 5
        myBoard.drawBoard() 
        
        # check if square is empty
        print("square empty(1,1):",myBoard.squareIsEmpty(1,1))
        
        # try to assign a number to a non-empty square
        updateCheck = myBoard.update(1,1,6)
        print("Trying to update '6' at position (1,1)")
        myBoard.drawBoard()  
        print("did it update:", updateCheck)
        
        # check if the board has a winner. 
        if myBoard.isWinner():
            print("Winner")
        else:
            print("not winner")
            
        # check if the board is full. 
        if myBoard.boardFull():
            print("Board Full")
        else:
            print("not full")        
        
        # add values to the board so that any line adds up to 15. Display
        
        ## check if row win
        #myBoard.update(0,0,1)
        #myBoard.update(0,1,1)
        #myBoard.update(0,2,1) 
        #myBoard.update(1,0,2)
        #myBoard.update(1,2,8)
        #myBoard.update(2,1,1)
        #myBoard.update(2,0,1)
        #myBoard.update(2,2,1)
        
        ## check if col win
        #myBoard.update(0,0,1)
        #myBoard.update(0,1,1)
        #myBoard.update(0,2,2) 
        #myBoard.update(1,0,1)
        #myBoard.update(1,2,6) 
        #myBoard.update(2,0,1)
        #myBoard.update(2,1,1)   
        #myBoard.update(2,2,7) 
        
        ## check diagonal win
        #myBoard.update(0,0,2)
        #myBoard.update(0,1,1)
        #myBoard.update(0,2,1)
        #myBoard.update(1,0,1)
        #myBoard.update(1,2,1) 
        #myBoard.update(2,0,1)
        #myBoard.update(2,2,8)
        #myBoard.update(2,1,1)          
        
        myBoard.drawBoard()
        
        # check if the board has a winner
        if myBoard.isWinner():
            print("Winner")
        else:
            print("not winner")
        
        # check if the board is full
        if myBoard.boardFull():
            print("Board Full")
        else:
            print("not full")
            
    def test_ClassicTicTacToe():
        '''
        Test ClassicTicTacToe class
        '''
        # start by creating empty board and checking the contents of the board attribute    
        myBoard = ClassicTicTacToe()
        print('Contents of board attribute when object first created:')
        print(myBoard.board)
        
        # check if the empty board displays properly
        myBoard.drawBoard()
    
        # check if square is empty
        print("square empty(1,1):",myBoard.squareIsEmpty(1,1)) 
        
        # assign a letter to an empty square and display
        myBoard.board[1][1] = "X"
        myBoard.drawBoard() 
        
        # check if square is empty        
        print("square empty(1,1):",myBoard.squareIsEmpty(1,1))
        
        # try to assign a letter to a non-empty square. 
        updateCheck = myBoard.update(1,1,"O")
        print("Trying to update 'O' at position (1,1)")
        myBoard.drawBoard()  
        print("did it update:", updateCheck)
        
        # check if the board has a winner. 
        if myBoard.isWinner():
            print("Winner")
        else:
            print("not winner")
            
        # check if the board is full. 
        if myBoard.boardFull():
            print("Board Full")
        else:
            print("not full")        
        
        # add values to the board so that any line has the same symbols. Display
         
        ## check if row win
        #myBoard.update(0,0,"O")
        #myBoard.update(0,1,"O")
        #myBoard.update(0,2,"O") 
        #myBoard.update(1,0,"O")
        #myBoard.update(1,1,"O")
        #myBoard.update(1,2,"X")
        #myBoard.update(2,0,"X")
        #myBoard.update(2,1,"O")
        #myBoard.update(2,2,"X")
        
        ## check if col win
        #myBoard.update(0,0,"O")
        #myBoard.update(0,1,"X")
        #myBoard.update(0,2,"O") 
        #myBoard.update(1,0,"O")
        #myBoard.update(1,1,"X")
        #myBoard.update(1,2,"X") 
        #myBoard.update(2,0,"X")
        #myBoard.update(2,1,"X")   
        #myBoard.update(2,2,"O")  
        
        ## check diagonal win
        #myBoard.update(0,0,"X")
        #myBoard.update(0,1,"O")
        #myBoard.update(0,2,"O")
        #myBoard.update(1,0,"O")
        #myBoard.update(1,1,"O")
        #myBoard.update(1,2,"O") 
        #myBoard.update(2,0,"O")
        #myBoard.update(2,2,"X")
        #myBoard.update(2,1,"O")        
        
        myBoard.drawBoard()
        
        # check if the board has a winner
        if myBoard.isWinner():
            print("Winner")
        else:
            print("not winner")
        
        # check if the board is full
        if myBoard.boardFull():
            print("Board Full")
        else:
            print("not full")
            
    def test_MetaTicTacToe():
        '''
        Test MetaTicTacToe class
        '''
        # pass in file name initialize configuration file 
        fileName = "MetaTTTconfig.txt"
        myBoard = MetaTicTacToe(fileName)
        
        # check contents of the board when it is first created
        print('Contents of board attribute when object first created:')
        print(myBoard.board)
        
        # check if the board displays properly
        myBoard.drawBoard()
        
        # check if square is empty
        print("square empty(1,1):",myBoard.squareIsEmpty(1,1)) 
        
        # if localBoard hasn't been played, it will return instance of local board.
        if myBoard.getLocalBoard(1,1) == None:
            print("Local board already played at (1,1).")        
        else:
            print("local board at(1,1): ",myBoard.getLocalBoard(1,1))             
            
        # assign a letter to an empty square and display
        print("Update 'D' at (1,1)")
        myBoard.board[1][1] = "D"
        myBoard.drawBoard() 
        
        # test if value of localBoard has been played
        if myBoard.getLocalBoard(1,1) == None:
            print("Local board already played at (1,1).")
        else:
            print("local board at(1,1): ",myBoard.getLocalBoard(1,1))                         
        
        # check if square is empty
        print("square empty(1,1):",myBoard.squareIsEmpty(1,1))
        
        # try to assign a letter to a non-empty square. 
        updateCheck = myBoard.update(1,1,"O")
        print("Trying to update 'O' at position (1,1)")
        myBoard.drawBoard()  
        print("did it update:", updateCheck)
        
        # check if the board has a winner. 
        if myBoard.isWinner():
            print("Winner")
        else:
            print("not winner") 
                 
        # check if the board is full
        if myBoard.boardFull():
            print("Board Full")
        else:
            print("not full")         
    
        # add values to the board so that any line has all the same letters. Display
         
        ## check if row win
        #myBoard.update(0,0,"O")
        #myBoard.update(0,1,"O")
        #myBoard.update(0,2,"O") 
        #myBoard.update(1,0,"O")
        #myBoard.update(1,2,"X")
        #myBoard.update(2,0,"X")
        #myBoard.update(2,1,"O")
        #myBoard.update(2,2,"X")
        
        ## check if col win
        #myBoard.update(0,0,"X")
        #myBoard.update(0,1,"O")
        #myBoard.update(0,2,"D") 
        #myBoard.update(1,0,"X")
        #myBoard.update(1,2,"X") 
        #myBoard.update(2,0,"X")
        #myBoard.update(2,1,"D")   
        #myBoard.update(2,2,"O")  
        
        ## check diagonal win
        #myBoard.update(0,0,"D")
        #myBoard.update(0,1,"O")
        #myBoard.update(0,2,"O")
        #myBoard.update(1,0,"X")
        #myBoard.update(1,2,"D")
        #myBoard.update(2,0,"O")
        #myBoard.update(2,1,"X")
        #myBoard.update(2,2,"D")
             
        myBoard.drawBoard()
        
        # check if the board has a winner
        if myBoard.isWinner():
            print("Winner")
        else:
            print("not winner")
        
        # check if the board is full
        if myBoard.boardFull():
            print("Board Full")
        else:
            print("not full")        

 
    #test_NumTicTacToe()
    #test_ClassicTicTacToe()
    #test_MetaTicTacToe()
