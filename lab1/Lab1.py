# student name: Umair Mazhar
# student number: 20333308

# A command-line Tic-Tac-Toe game 
from curses.ascii import isdigit
from lib2to3.pgen2.token import GREATER
import random

board = [' '] * 9 # A list of 9 strings, one for each cell, 
                  # will contain ' ' or 'X' or 'O'
played = set()    # A set to keep track of the played cells 

def init() -> None:
    """ prints the banner messages 
        and prints the int0ial board on the screen
    """
    print("Welcome to Tic-Tac-Toe!")
    print("You play X (first move) and computer plays O.")
    print("Computer plays randomly, not strategically.")
    printBoard()

def printBoard() -> None:
    """ prints the board on the screen based on the values in the board list """
    print("\n")
    print("  ",board[0],"|",board[1],"|",board[2],"   0 | 1 | 2")
    print("   --+---+--    --+---+--")
    print("  ",board[3],"|",board[4],"|",board[5],"   3 | 4 | 5")
    print("   --+---+--    --+---+--")
    print("  ",board[6],"|",board[7],"|",board[8],"   6 | 7 | 8")
    print("\n")


def playerNextMove() -> None:
    """ prompts the player for a valid cell number, 
        and prints the info and the updated board;
        error checks that the input is a valid cell number 
    """

    while True: 
        playerInput = input("Next move for X (State a valid cell num):")
        if not (playerInput.isdigit()): #checking if input is a digit
            print("Must be an integer") 
            continue
        elif (int(playerInput) >= 0) and (int(playerInput) <= 8): #checking if input is a cell on the board
            if (int(playerInput) in played):
                print("Must enter a valid cell number")
                continue
            else: #valid 
                print("You chose cell ", playerInput) 
                played.add(int(playerInput)) #add played integer to set so it can't be played again
                board[int(playerInput)] = 'X'
                printBoard();
                return
        else:
            print("Must enter a valid cell number")
            continue
            

def computerNextMove() -> None:
    moveSuccess = False #move is successful if it is valid, invalid move at first
    while moveSuccess == False:
        computerGuess = random.randint(0,8) #pick random place on board to place 
        if computerGuess in played: #if it already is on the board, repeat
            continue    
        else:
            moveSuccess = True
            played.add(computerGuess)   #add cell to set as taken
            board[computerGuess] = "O"  
            print("Computer chose cell ", computerGuess)
            printBoard()

def hasWon(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
    #checking to see if every winning combo is equal to the who being passed in
    if (board[0] == board[1] == board[2] == who or 
        board[3] == board[4] == board[5] == who or
        board[6] == board[7] == board[8] == who or 
        board[0] == board[3] == board[6] == who or 
        board[1] == board[4] == board[7] == who or
        board[2] == board[5] == board[8] == who or
        board[0] == board[4] == board[8] == who or
        board[2] == board[4] == board[6] == who):
        return True
    return False
    
def terminate(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
        it also prints the final messages:
                "You won! Thanks for playing." or 
                "You lost! Thanks for playing." or 
                "A draw! Thanks for playing."  
    """
    allElements = set()
    for x in range(0,9):
        allElements.add(x)
        
    if allElements.issubset(played):
        print("A draw! Thanks for playing")
        return True

    if hasWon(who):
        if who == 'O':
            print('You lost! Thanks for playing.')
        elif who == 'X':
            print('You won! Thanks for playing.')
        return True
    
    return False

    
if __name__ == "__main__":
    # Use as is. 
    init()
    while True:
        playerNextMove()            # X starts first
        if(terminate('X')): break   # if X won or a draw, print message and terminate
        computerNextMove()          # computer plays O
        if(terminate('O')): break   # if O won or a draw, print message and terminate
