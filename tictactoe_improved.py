board = 20 * "-"
from random import randrange

def evaluate(board):
    """evaluates winner, draw or continue..."""
    if "xxx" in board:
        print("You won!")
        return True
    elif "ooo" in board:
        print("Computer won!")
        return True
    elif "-" not in board:
        print("Draw!")
        return True
    else:
        print("Next move:")
        return False

def move(board, mark, position):
    """returns the game board with the given mark in the given position"""
    if board[position - 1] == "-":
        board2 = board[:position - 1] + mark + board[position:]
        move_ok = True
        return move_ok, board2
    else: 
        print("Position is occupied, choose a different one")
        move_ok = False
        return move_ok, board

def player_move(board):
    """returns a game board with the player's move."""
    while True:
        answer = input("Please choose a position between 1 and 20: ")
        try:
            number = int(answer)
        except ValueError:
            print("This was not a number. Try again!")
            continue
        setposition = number
        if setposition <= 20 and setposition > 0:
            board = move(board, "x", setposition)
            return board
        elif setposition <= 0:
            print("Please insert a positive number")  
        else:
            print("Number too high or wrong input")

def pc_move(board):
    """returns a game board with the computer's move."""
    randommove = randrange(1, 21)
    board = move(board, "o", randommove)
    return board
       
def tic_tac_toe():
    """board game tic tac toe"""
    board = 20 * "-"
    while True:
        move_ok = False
        while not move_ok:  
            move_ok, board = player_move(board)
            print(board)
        if evaluate(board):
            break
        move_ok = False
        while move_ok == False: 
            move_ok, board = pc_move(board)
            print(board)
        if evaluate(board):
            break      

tic_tac_toe()

"""Ideas for optimisation:
check 1) Currently, the input has to be a number. 
If a string is chosen, the program returns an error message.
This should be fixed.
2) As long as the computer chooses completely random positions, it is easy
for the player to win the game.
Better for the computer (and more interesting for the player) would be to select 
a random position first, then if available, choose a position next to another o. 
Only if this is not possible (surrounded by x, or end of row), another random 
position will be selected."""