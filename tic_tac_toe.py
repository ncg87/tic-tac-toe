"""
Course: Python Programming
"""
#%%
def author():
    return None
#%%
import random
import copy
# %% import every function in that module
from tic_tac_toe_board_and_judge import *
from tic_tac_toe_board_and_judge import (DrawBoard, UpdateBoard, 
                                         IsSpaceFree, Judge)
#%%
def HumanPlayer(Tag, Board, N=0):
    '''
    Parameters: 
        Tag is 'X' or 'O'. If Tag is 'X': HumanPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
        N is a dumpy input
    Return: ChoiceOfHumanPlayer, it is a tuple (row, col)
            0 <= row, col <= 2 
    Description:
        This function will NOT return until it gets a valid input from the user
    Attention:
        Board is NOT modified in this function
    hint: 
        a while loop is needed, see HumanPlayer in rock-papper-scissors
        the user needs to input row-index and col-index, where a new chess will be placed
        use int() to convert string to int
        use try-except to handle exceptions if the user inputs some random string
        if (row, col) has been occupied, then ask the user to choose another spot
        if (row, col) is invalid, then ask the user to choose a valid spot
    '''
    while True:
        try:
            row = int(input(f"Player {Tag}, enter your move (row 0-2): "))
            col = int(input(f"Player {Tag}, enter your move (col 0-2): "))
            
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter row and column values between 0 and 2.")
                continue
            
            if IsSpaceFree(Board, row, col):
                return (row, col)
            else:
                print("This space is already occupied. Please choose another spot.")
        
        except ValueError:
            print("Invalid input. Please enter integers for row and column.")

#%%
def ShowOutcome(Outcome, NameX, NameO):
    '''
    Parameters:
        Outcome is from Judge
        NameX is the name of PlayerX who goes first at the beginning
        NameO is the name of PlayerO 
    Return: None
    Description:
        print a meassage about the Outcome
        NameX/NameO may be 'human' or 'computer'
    hint: the message could be
        PlayerX (NameX, X) wins 
        PlayerO (NameO, O) wins
        the game is still in progress
        it is a tie
    '''
    if Outcome == 'X':
        print(f"Player X ({NameX}, X) wins!")
    elif Outcome == 'O':
        print(f"Player O ({NameO}, O) wins!")
    elif Outcome == 'Tie':
        print("The game is a tie!")
    else:
        print("The game is still in progress.")
#%% read but do not modify this function
def Which_Player_goes_first(ComputerPlayer, HumanPlayer):
    '''
    Parameter: None
    Return: two function objects: PlayerX, PlayerO
    Description:
        Randomly choose which player goes first.
        PlayerX/PlayerO is ComputerPlayer or HumanPlayer
    '''
    if random.randint(0, 1) == 0:
        print("Computer player goes first")        
        return ComputerPlayer, HumanPlayer
    else:
        print("Human player goes first")
        return HumanPlayer, ComputerPlayer
#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print("Welcome to Tic Tac Toe Game")
    N=input("Set the steps for ComputerPlayer so that it could think N steps ahead: N=")
    try:
        N = int(N)
        if N < 0:
            print('N < 0, set it to 0')
            N=0
    except:
        print('invalid input, set N to 0')
        N = 0
    #select ComputerPlayer
    if N == 0:
        from ComputerPlayer_v0 import ComputerPlayer
    elif N == 1:
        from ComputerPlayer_v1 import ComputerPlayer    
    else:
        from ComputerPlayer_v2 import ComputerPlayer
    #an empty board
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    # determine the order
    PlayerX, PlayerO = Which_Player_goes_first(ComputerPlayer, HumanPlayer)
    # get the name of each function object
    # NameX and NameO are two strings, which could be 
    #   (1) 'ComputerPlayer' and 'HumanPlayer'    
    #   (2) 'HumanPlayer' and 'ComputerPlayer'
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    #---------------------------------------------------    
    # suggested steps in a while loop:
    # while ???:
    # (1)  get a choice from PlayerX, e.g. ChoiceX=PlayerX('X', Board, N)
    # (2)  update the Board
    # (3)  draw the Board
    # (4)  get the outcome from Judge
    # (5)  show the outcome
    # (6)  if the game is completed (win or tie), then break the loop
    # (7)  get a choice from PlayerO
    # (8)  update the Board
    # (9)  draw the Board
    # (10) get the outcome from Judge
    # (11) show the outcome
    # (12) if the game is completed (win or tie), then break the loop
    #---------------------------------------------------
    # your code starts from here
    NameX = "Computer" if PlayerX == ComputerPlayer else "Human"
    NameO = "Computer" if PlayerO == ComputerPlayer else "Human"

    print(f"PlayerX: {NameX}, PlayerO: {NameO}")
    
    current_player = 'X'
    game_over = False

    while not game_over:
        current_function = PlayerX if current_player == 'X' else PlayerO
        print(f"Getting move for Player{current_player} ({NameX if current_player == 'X' else NameO})")
        choice = current_function(current_player, Board, N)

        print(f"Move: {choice}")

        if choice is None:
            print(f"Error: {NameX if current_player == 'X' else NameO} returned None")
            break

        UpdateBoard(Board, current_player, choice)
        DrawBoard(Board)

        outcome = Judge(Board)
        if outcome != 0:
            game_over = True
            if outcome == 1:
                print(f"Player X ({NameX}) wins!")
            elif outcome == 2:
                print(f"Player O ({NameO}) wins!")
            else:
                print("It's a tie!")
        else:
            current_player = 'O' if current_player == 'X' else 'X'
#%% play the game many rounds until the user wants to quit
# read but do not modify this function
def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print("GameOver")
#%% do not modify anything below
if __name__ == '__main__':
    PlayGame()
