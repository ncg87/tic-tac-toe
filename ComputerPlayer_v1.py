#%%
import random
import copy
from tic_tac_toe_board_and_judge import (IsBoardEmpty, IsSpaceFree, Judge)
#%%
def ComputerPlayer(Tag, Board, N=1):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
        N: think N steps ahead, N is not used here
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
            0 <= row, col <= 2 
    Description:
        ComputerPlayer will think 1 step ahead
    Attention:
        Board is NOT modified in this function
    '''
    opponent_tag = 'O' if Tag == 'X' else 'X'
    
    # Check for immediate win
    for i in range(3):
        for j in range(3):
            if IsSpaceFree(Board, i, j):
                temp_board = copy.deepcopy(Board)
                temp_board[i][j] = Tag
                if Judge(temp_board) == (1 if Tag == 'X' else 2):
                    return (i, j)
    
    # Block opponent's win
    for i in range(3):
        for j in range(3):
            if IsSpaceFree(Board, i, j):
                temp_board = copy.deepcopy(Board)
                temp_board[i][j] = opponent_tag
                if Judge(temp_board) == (1 if opponent_tag == 'X' else 2):
                    return (i, j)
    
    # If center is free, take it
    if IsSpaceFree(Board, 1, 1):
        return (1, 1)
    
    # Try to create a fork or block opponent's fork
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    
    # Check for potential forks
    for move in corners + edges:
        if IsSpaceFree(Board, move[0], move[1]):
            temp_board = copy.deepcopy(Board)
            temp_board[move[0]][move[1]] = Tag
            if sum(1 for i in range(3) for j in range(3) if IsSpaceFree(temp_board, i, j) and Judge(copy.deepcopy(temp_board)) == (1 if Tag == 'X' else 2)) >= 2:
                return move
    
    # Take an empty corner
    for corner in corners:
        if IsSpaceFree(Board, corner[0], corner[1]):
            return corner
    
    # Take an empty edge
    for edge in edges:
        if IsSpaceFree(Board, edge[0], edge[1]):
            return edge
    
    # If all else fails, make a random move
    available_moves = [(i, j) for i in range(3) for j in range(3) if IsSpaceFree(Board, i, j)]
    return random.choice(available_moves) if available_moves else (0, 0)