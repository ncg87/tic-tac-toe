import random
import copy
from tic_tac_toe_board_and_judge import (IsBoardEmpty, IsSpaceFree, Judge)

def ComputerPlayer(Tag, Board, N):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
        N: think N steps ahead, N >= 2
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)
            0 <= row, col <= 2 
    Description:
        ComputerPlayer will think N steps ahead
    Attention:
        Board is NOT modified in this function
    '''
    def minimax(board, depth, is_maximizing, alpha, beta):
        score = Judge(board)
        if score == 1:
            return 10 - depth
        elif score == 2:
            return depth - 10
        elif score == 3:
            return 0
        
        if depth == N:
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if IsSpaceFree(board, i, j):
                        board[i][j] = 'X'
                        score = minimax(board, depth + 1, False, alpha, beta)
                        board[i][j] = ' '
                        best_score = max(score, best_score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if IsSpaceFree(board, i, j):
                        board[i][j] = 'O'
                        score = minimax(board, depth + 1, True, alpha, beta)
                        board[i][j] = ' '
                        best_score = min(score, best_score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

    if IsBoardEmpty(Board):
        return (random.randint(0, 2), random.randint(0, 2))

    best_score = float('-inf') if Tag == 'X' else float('inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')

    for i in range(3):
        for j in range(3):
            if IsSpaceFree(Board, i, j):
                temp_board = copy.deepcopy(Board)
                temp_board[i][j] = Tag
                score = minimax(temp_board, 0, Tag == 'O', alpha, beta)
                
                if Tag == 'X':
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
                    alpha = max(alpha, best_score)
                else:
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
                    beta = min(beta, best_score)
                
                if beta <= alpha:
                    break

    return best_move if best_move else (random.randint(0, 2), random.randint(0, 2))