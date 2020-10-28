#----------------------------------------------------
# Main Program for Meta Tic Tac Toe
# References: python 3 documentation
# Author: Urvi Patel
#----------------------------------------------------
from UltimateMetaTTT import NumTicTacToe
from UltimateMetaTTT import ClassicTicTacToe
from UltimateMetaTTT import MetaTicTacToe

def main():
    '''
    This function calls the other functions to play the game
    Input: None
    Returns: None
    '''
    newGame=True
    while newGame:    
        # print the header
        line = "----------------------------------"
        print(line,"\nStarting new Meta Tic Tac Toe game","\n"+ line+"\n")
        
        # create instances of metaTicTacToe    
        metaGame = MetaTicTacToe("MetaTTTconfig.txt")
        currentPlayer = 1  # start with player 1
        
        while not metaGame.isWinner():  # continue playing game until a player wins metagame
            #display initial meta board
            metaGame.drawBoard()        
            # ask player for input
            selectedSquare = getPlayerInput(metaGame, currentPlayer) # selectedSquare is a tuple of (row,col)
            
            if metaGame.squareIsEmpty(selectedSquare[0],selectedSquare[1]):
                #depending on which local board is selected, initiate that game
                localBoardInstance = metaGame.getLocalBoard(selectedSquare[0], selectedSquare[1])
                if localBoardInstance.isNum():
                    result = playNumTicTacToe(localBoardInstance, currentPlayer)
                    localResult = whoWon(result)
                    metaGame.update(selectedSquare[0],selectedSquare[1], localResult)
                    currentPlayer = switchPlayer(currentPlayer)
                else:
                    result = playClassicTicTacToe(localBoardInstance, currentPlayer)
                    localResult = whoWon(result)
                    metaGame.update(selectedSquare[0],selectedSquare[1], localResult)
                    currentPlayer = switchPlayer(currentPlayer)
            else:
                print("Error: local game already played.")
                
        # display winning result
        currentPlayer = switchPlayer(currentPlayer)
        metaGame.drawBoard()
        print("Player "+str(currentPlayer)+" wins the Meta Tic Tac Toe game. GOOD GAME!")
        newGame = playAgain()
        
    print("Thanks for playing! Goodbye.")
    
def playAgain():
    '''
    Asks if a new game should be started. A valid answer is any entry that begins
    with y/Y/n/N.
    Inputs: none
    Returns: True if a new game should start; False otherwise
    '''
    playAgain=' ' 
    # validate user's input
    while playAgain[0].upper() not in ['Y', 'N']:
        playAgain=input("Do you want to play another game? (Y/N) ")
    return playAgain[0].upper() == "Y"     
        
def switchPlayer(currentPlayer):
    '''
    This function switches between the two players
    Inputs: currentPlayer(int): either 1 or 2
    Returns: the new player(int)
    '''
    if currentPlayer == 1:
        newPlayer = 2
    else:
        newPlayer = 1
    return newPlayer

def whoWon(result):
    '''
    This function checks who won the local game
    Inputs: result of the local game
    Returns: the correspnding str to display on the meta board
    '''
    if result == "tie":
        return "D"
    elif result == 1:
        return "X"
    elif result ==2:
        return "O"
    
def getPlayerInput(game, currentPlayer):
    '''
    This function gets player the player input to select the square to play
    Inputs: int of current player, instance of local game
    Returns: tuple of selected square (row, col)
    '''
    # get list of numbers that are valid
    boardSize = game.size
    validInput = []
    for number in range(boardSize):
        validInput.append(str(number))
        
    # prompt player to enter row and col, keep prompting until they enter a valid pair
    rowPrompt = "Player "+str(currentPlayer)+", please enter a row:"
    colPrompt= "Player "+str(currentPlayer)+", please enter a column:"   
    rowInput = input(rowPrompt)
    while rowInput not in validInput: 
        rowInput = input("Error: row not in correct range. "+rowPrompt)        
    colInput = input(colPrompt)
    while colInput not in validInput:
        colInput = input("Error: column not in correct range. "+colPrompt)    

    return (int(rowInput),int(colInput))
        
def getNumEntry(turn, player, entries):
    '''
    This function get the valid number response for the Numerical game
    Inputs: which turn it is(int), which player(int), set of already made entries
    Returns: the valid response(int)
    '''
    if turn == 1:
        numDescription = 'odd'
        lowerRange = 1
        upperRange = 9        
    else:
        numDescription = 'even'
        lowerRange = 2
        upperRange = 8         
    prompt = 'Player {}, please enter an {} number ({}-{}): '.format(player, numDescription, lowerRange, upperRange)
    validMove = False
    ifError = ''
    # until the number is valid, keep prompting for a correct response
    while not validMove:
        response = input(ifError+prompt)
        entry = checkValidEntry(turn, entries, response)
        validMove = entry[0]
        ifError = entry[1]
        
    return int(response)  

def checkValidEntry(turn, entries, response):
    '''
    This function checks if the player has entered a valid response
    Input: int of which turn, set() of list of entries, player response(int)
    Returns: list of [if entry is valid(bool), error to display(str)]
    '''
    # append the numbers that are valid for even numbers and odd numbers
    evenMoves = []
    oddMoves = []
    #allMoves = []
    validMove = True
    error = ''
    for number in range(2, 9, 2):
        evenMoves.append(str(number))
        #allMoves.append(str(number))
    for number in range(1,10,2):
        oddMoves.append(str(number)) 
        #allMoves.append(str(number))
    
    # check if the entry has already been previously entered
    if response.isdigit() and int(response) in entries:
        error = "Error: that number has already been entered. "
        validMove = False
    # check if response is odd for turn 1
    elif turn == 1 and response not in oddMoves and response in evenMoves:
        error = "Error: Entry not odd. "
        validMove = False
    # check if response is even for turn 2
    elif turn == 2 and response not in evenMoves and response in oddMoves:
        error = "Error: entry not even. "
        validMove = False      
    elif response not in evenMoves and response not in oddMoves:
        # check is response is out of range
        if response.isdigit():
            error = "Error: entry not in range. "
            validMove = False
        else:
            error = "Error: invalid entry. "
            validMove = False
            
    return [validMove, error]  

def isNumGameOver(numGame, player):
    '''
    This function checks if the Numerical Game is over
    Inputs: instance of NumericalTicTacToe, player(int)
    Returns: list of [if game over(bool, which player won(str)]
    '''
    gameOver = [False,'']
    #check if win
    if numGame.isWinner():
        print()
        numGame.drawBoard()
        print("Player "+str(player)+" wins. Congrats!")
        gameOver = [True, player]
    #check if board is full
    elif numGame.boardFull():
        print()
        numGame.drawBoard()
        print("It's a tie.")
        gameOver = [True,"tie"]
    
    return gameOver
        
def playNumTicTacToe(numGame, player):
    '''
    This function manages the game play for local boards of NumTicTacToe
    Inputs: the instance of NumerialTicTacToe, player(int)
    Returns: which player won(str)
    '''
    print("------------------------------------", "\nThis is a Numerical Tic Tac Toe.\n")
    gameOver = False
    entries = set()
    turn = 1
    while not gameOver:
        numGame.drawBoard()
        # ask for user input
        userEntry = getNumEntry(turn, player, entries)
        coord = getPlayerInput(numGame, player)       
        # update board and check if game continues
        if numGame.update(coord[0],coord[1], userEntry):
            entries.add(userEntry)
            result = isNumGameOver(numGame, player)
            gameOver = result[0]
            player = switchPlayer(player)  
            turn = switchPlayer(turn)
        else:
            print("Error: could not make move!")
        print()
        
    return result[1]  
    
def switchMarks(mark):
    '''
    This function switches the symbol for the Classic Game
    Inputs: current symbol(str)
    Returns: new symbol(str)
    '''
    if mark == 'X':
        mark = 'O'
    else:
        mark = 'X'
    return mark

def isClassicGameOver(classicGame, player):
    '''
    This function check is the Classic Game is over
    Inputs: instance of ClassicTicTacToe, player(int)
    Returns: list of [if game is over(bool), who won(str)]
    '''
    gameOver = [False, '']
    # check if win
    if classicGame.isWinner():
        print()
        classicGame.drawBoard()
        print("Player "+str(player)+" wins. Congrats!")
        gameOver = [True, player]
    # check if board full
    elif classicGame.boardFull():
        print()
        classicGame.drawBoard()
        print("It's a tie.")
        gameOver = [True, "tie"]

    return gameOver
    
    
def playClassicTicTacToe(classicGame, player):
    '''
    This function manages the game play for local boards of ClassicTicTacToe
    Inputs: instance of ClassicTicTacToe, player(int)
    Returns: which player won(str)
    '''    
    print("------------------------------------", "\nThis is a Classical Tic Tac Toe.\n")
    gameOver = False
    mark = 'X'
    while not gameOver:
        classicGame.drawBoard()
        # ask for user input
        coord = getPlayerInput(classicGame, player)
        # update board and check if game continues
        if classicGame.update(coord[0], coord[1], mark):
            mark = switchMarks(mark)
            result = isClassicGameOver(classicGame, player)
            gameOver = result[0]
            player = switchPlayer(player)
        else:
            print("Error: could not make move!")  
        print()
        
    return result[1]
            
   
        
main()