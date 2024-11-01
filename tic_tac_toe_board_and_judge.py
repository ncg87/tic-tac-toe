#%%
import random
import copy
# %%
def DrawBoard(Board):
    for row in Board:
        print("|".join(row))
        print("-" * 5)
#%% 
def IsSpaceFree(Board, i ,j):
    '''
    Parameters: Board is the game board, a 3x3 matrix
                i is the row index, j is the col index
    Return: True or False    
    Description:
        0 <= i, j <= 2
        (1) return False if i or j is invalid (e.g. i = -1 or 100)
        (2) return True  if Board[i][j] is empty (' ')
        (3) return False if Board[i][j] is not empty
        
        think about the order of (1) (2) (3)
        Do NOT use print in this function
    '''
    if i < 0 or i > 2 or j < 0 or j > 2:
        return False
    if Board[i][j] == ' ':
        return True
    return False
#%%
def GetNumberOfChessPieces(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: the number of chess piceces on Board
            i.e. the total number of 'X' and 'O'
    hint: define a counter and use a nested for loop, like this
          for i in 0 to 3
              for j in 0 to 3
                  add one to the counter if Board[i][j] is not empty
    '''
    return sum(1 for row in Board for cell in row if cell != ' ')
#%%
def IsBoardFull(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is fully occupied
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    return GetNumberOfChessPieces(Board) == 9
    
#%%
def IsBoardEmpty(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is empty
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    return GetNumberOfChessPieces(Board) == 0
#%%
def UpdateBoard(Board, Tag, Choice):
    '''
    Parameters: 
        Board is the game board, a 3x3 matrix
        Tag is 'O' or 'X'
        Choice is a tuple (row, col) from HumanPlayer or ComputerPlayer
    Return: None
    Description: 
         Update the Board after a player makes a choice
         Set an element of the Board to Tag at the location (row, col)
    '''
    Board[Choice[0]][Choice[1]] = Tag
#%%
def Judge(Board):
    '''
    Parameter:
         Board is the current game board, a 3x3 matrix
    Return: Outcome, an integer
        Outcome is 0 if the game is still in progress
        Outcome is 1 if player X wins
        Outcome is 2 if player O wins
        Outcome is 3 if it is a tie (no winner)
    Description:
        this funtion determines the Outcome of the game
    hint:
        (1) check if anyone wins, i.e., three 'X' or 'O' in
            top row, middle row, bottom row
            lef col, middle col, right col
            two diagonals
            use a if-statment to check if three 'X'/'O' in a row
        (2) if no one wins, then check if it is a tie
            note: if the board is fully occupied, then it is a tie
        (3) otherwise, the game is still in progress
    '''
    # Check rows, columns, and diagonals
    for i in range(3):
        if Board[i][0] == Board[i][1] == Board[i][2] != ' ':
            return 1 if Board[i][0] == 'X' else 2
        if Board[0][i] == Board[1][i] == Board[2][i] != ' ':
            return 1 if Board[0][i] == 'X' else 2
    if Board[0][0] == Board[1][1] == Board[2][2] != ' ':
        return 1 if Board[0][0] == 'X' else 2
    if Board[0][2] == Board[1][1] == Board[2][0] != ' ':
        return 1 if Board[0][2] == 'X' else 2
    if IsBoardFull(Board):
        return 3
    return 0
