from copy import deepcopy
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--student', type=str,
                    default='tic_tac_toe')
arg=parser.parse_args()
print(arg)
#%%
exec ("import "+arg.student+" as student")
exec ("from "+arg.student+" import TicTacToeGame, DrawBoard")
exec ("from "+arg.student+" import HumanPlayer as human_player")
#%% test HumanPlayer
Board7 = [['O', 'X', 'O'],
          [' ', 'X', 'X'],
          [' ', 'O', 'X']]
DrawBoard(Board7)
human_player("O", Board7)
#play it and assign the score, max=15. 
#0 if human_player cannot handled/do not check invalid input
score_HumanPlayer=15
#%% test TicTacToeGame
score_TicTacToeGame=10
try:
    from ComputerPlayer_v0 import ComputerPlayer
    student.HumanPlayer= ComputerPlayer
    TicTacToeGame()
except:
    score_TicTacToeGame=0
print("score_TicTacToeGame",score_TicTacToeGame)    
#%% test DrawBoard and ShowOutcome 
#0 if some messages are missing (e.g., who wins the game)
#look at the output and assign the scores
score_ShowOutcome=2
score_DrawBoard=2
#%%
exec ("from "+arg.student+" import IsSpaceFree")
exec ("from "+arg.student+" import GetNumberOfChessPieces")
exec ("from "+arg.student+" import IsBoardFull")
exec ("from "+arg.student+" import IsBoardEmpty")
exec ("from "+arg.student+" import UpdateBoard")
exec ("from "+arg.student+" import Judge")
#%%
Board0 = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]
Board1 = [[' ', ' ', ' '],
          [' ', 'X', ' '],
          [' ', ' ', ' ']]
Board2 = [['O', ' ', ' '],
          [' ', 'X', ' '],
          [' ', ' ', ' ']]
Board3 = [['O', ' ', ' '],
          [' ', 'X', ' '],
          [' ', ' ', 'X']]
Board4 = [['O', ' ', 'O'],
          [' ', 'X', ' '],
          [' ', ' ', 'X']]
Board5 = [['O', 'X', 'O'],
          [' ', 'X', ' '],
          [' ', ' ', 'X']]
Board6 = [['O', 'X', 'O'],
          [' ', 'X', ' '],
          [' ', 'O', 'X']]
Board7 = [['O', 'X', 'O'],
          [' ', 'X', 'X'],
          [' ', 'O', 'X']]
Board8 = [['O', 'X', 'O'],
          ['O', 'X', 'X'],
          [' ', 'O', 'X']]
Board9 = [['O', 'X', 'O'],
          ['O', 'X', 'X'],
          ['X', 'O', 'X']]
#%% test IsSpaceFree
score_IsSpaceFree=5
try:
    for i in range(0, 3):
        for j in range(0, 3):
            if IsSpaceFree(deepcopy(Board0), i, j) != True:
                score_IsSpaceFree=0
                print('score_IsSpaceFree error0')
                break
        if score_IsSpaceFree == 0:
            break
    for i in range(0, 3):
        for j in range(0, 3):
            if IsSpaceFree(deepcopy(Board9), i, j) != False:
                score_IsSpaceFree=0
                print('score_IsSpaceFree error1')
                break
        if score_IsSpaceFree==0:
            break
    for i in range(-100, -1):
        for j in range(-100, -1):
            if IsSpaceFree(deepcopy(Board0), i, j) != False:
                score_IsSpaceFree=0      
                print('score_IsSpaceFree error2')
                break
        if score_IsSpaceFree==0:
            break
except:
    score_IsSpaceFree=0
    print('score_IsSpaceFree error3')
print("score_IsSpaceFree", score_IsSpaceFree)
#%% test GetNumberOfChessPieces 
score_GetNumberOfChessPieces=2
for k in range(0, 10):
    if GetNumberOfChessPieces(deepcopy((eval("Board"+str(k))))) != k:
        score_GetNumberOfChessPieces=0
        break
print("score_GetNumberOfChessPieces", score_GetNumberOfChessPieces )
#%% test IsBoardFull 
score_IsBoardFull=1
if IsBoardFull(Board9) != True:
    score_IsBoardFull=0
for k in range(0, 9):
    if IsBoardFull(deepcopy(eval("Board"+str(k)))) != False:
        score_IsBoardFull=0
        break
print("score_IsBoardFull", score_IsBoardFull)  
#%% test IsBoardEmpy 
score_IsBoardEmpy=1
if IsBoardEmpty(Board0) != True:
    score_IsBoardEmpy=0
for k in range(1, 10):
    if IsBoardEmpty(deepcopy(eval("Board"+str(k)))) != False:
        score_IsBoardEmpy=0
        break
print("score_IsBoardEmpy", score_IsBoardEmpy)  
#%% test UpdateBoard 
score_UpdateBoard=2
try:
    for i in range(0, 3):
        for j in range(0, 3):
            temp=deepcopy(Board0)
            UpdateBoard(temp, "X", (i,j))
            if temp[i][j] != "X":
                score_UpdateBoard=0
                print('UpdateBoard error0')
                break
            temp=deepcopy(Board0)
            UpdateBoard(temp, "O", (i,j))
            if temp[i][j] != "O":
                print('UpdateBoard error1')
                score_UpdateBoard=0
                break
        if score_UpdateBoard==0:
            break
except:
    score_UpdateBoard=0
    print('UpdateBoard error2')
print("score_UpdateBoard", score_UpdateBoard)
#%% test ComputerPlayer_v0
from ComputerPlayer_v0 import ComputerPlayer as computer_player
score_ComputerPlayer_v0=10
for k in range(1, 9):
    board_k=deepcopy(eval("Board"+str(k)))
    i, j=computer_player("X", board_k)
    if (i not in [0, 1, 2]) or (j not in [0, 1, 2]):
        score_ComputerPlayer_v0=0
        print('ComputerPlayer_v0 error0')
        break
    if board_k[i][j] != " ":
        score_ComputerPlayer_v0=0
        print('ComputerPlayer_v0 error1')
        break
    if board_k != eval("Board"+str(k)):
        score_ComputerPlayer_v0=0
        print('ComputerPlayer_v0 error2')
        break
    i, j=computer_player("O", board_k)
    if (i not in [0, 1, 2]) or (j not in [0, 1, 2]):
        score_ComputerPlayer_v0=0
        print('ComputerPlayer_v0 error3')
        break
    if board_k[i][j] != " ":
        score_ComputerPlayer_v0=0
        print('ComputerPlayer_v0 error4')
        break
    if board_k != eval("Board"+str(k)):
        print('ComputerPlayer_v0 error5')
        score_ComputerPlayer_v0=0
        break
print('score_ComputerPlayer_v0', score_ComputerPlayer_v0)
#%% test ComputerPlayer_v1
from ComputerPlayer_v1 import ComputerPlayer as computer_player 
#---------------------------
#evaluate think one-step ahead
score_ComputerPlayer_v1=20
Board = [['X', ' ', ' '],
         [' ', 'O', ' '],
         ['X', ' ', ' ']]
choice=computer_player("O", Board)
if list(choice) != [1,0]:
    print('ComputerPlayer_v1 error0')
    score_ComputerPlayer_v1=0
#%%
Board = [['O', ' ', 'X'],
         [' ', ' ', ' '],
         ['X', ' ', ' ']]
choice=computer_player("O", Board)
if list(choice) != [1,1]:
    print('ComputerPlayer_v1 error1')
    score_ComputerPlayer_v1=0
#%%
Board = [['X', ' ', ' '],
         [' ', 'X', ' '],
         ['O', ' ', ' ']]
choice=computer_player("O", Board)
if list(choice) != [2,2]:
    print('ComputerPlayer_v1 error2')
    score_ComputerPlayer_v1=0
#%%
Board = [['X', ' ', 'X'],
         [' ', 'X', ' '],
         ['O', ' ', 'O']]
choice=computer_player("O", Board)
if list(choice) != [2,1]:
    print('ComputerPlayer_v1 error3')
    score_ComputerPlayer_v1=0
#%%
Board = [['O', ' ', 'X'],
         [' ', 'X', ' '],
         [' ', ' ', 'O']]
choice=computer_player("X", Board)
if list(choice) != [2,0]:
    print('ComputerPlayer_v1 error4')
    score_ComputerPlayer_v1=0
#%%
Board = [['O', 'X', ' '],
         [' ', 'X', ' '],
         [' ', ' ', 'O']]
choice=computer_player("X", Board)
if list(choice) != [2,1]:
    print('ComputerPlayer_v1 error5')
    score_ComputerPlayer_v1=0
#%%
Board = [['X', 'O', ' '],
         ['X', ' ', ' '],
         [' ', ' ', 'O']]
choice=computer_player("X", Board)
if list(choice) != [2,0]:
    print('ComputerPlayer_v1 error6')
    score_ComputerPlayer_v1=0
#%%
Board = [['X', ' ', 'X'],
         ['O', ' ', 'O'],
         [' ', ' ', ' ']]
choice=computer_player("X", Board)
if list(choice) != [0,1]:
    print('ComputerPlayer_v1 error7')
    score_ComputerPlayer_v1=0
print("score_ComputerPlayer_v1", score_ComputerPlayer_v1)
score_ComputerPlayer=score_ComputerPlayer_v0+score_ComputerPlayer_v1
#%% test Judge
#Outcome is 0 if the game is still in progress
#Outcome is 1 if player X wins
#Outcome is 2 if player O wins
#Outcome is 3 if it is a tie (no winner)
score_Judge=10
for k in range(0, 9):
    if Judge(eval("Board"+str(k))) != 0:
        score_Judge=0
        print('Judge error0')
        break
if Judge(Board9) != 3:
    print('Judge error1')
    score_Judge=0
#%%    
Board = [['X', 'X', 'X'],
         ['O', ' ', 'O'],
         [' ', ' ', ' ']]
if Judge(Board) != 1:
    print('Judge error2')
    score_Judge=0
#%%
Board = [[' ', ' ', ' '],
         ['X', 'X', 'X'],
         ['O', ' ', 'O']]
if Judge(Board) != 1:
    print('Judge error3')
    score_Judge=0
#%%
Board = [[' ', ' ', ' '],
         ['O', ' ', 'O'],
         ['X', 'X', 'X']]
if Judge(Board) != 1:
    print('Judge error4')
    score_Judge=0
#%%
Board = [['X', 'O', ' '],
         ['X', ' ', 'O'],
         ['X', ' ', ' ']]
if Judge(Board) != 1:
    print('Judge error5')
    score_Judge=0
#%%
Board = [['O', 'X', ' '],
         [' ', 'X', 'O'],
         [' ', 'X', ' ']]
if Judge(Board) != 1:
    print('Judge error6')
    score_Judge=0
#%%
Board = [['O', ' ', 'X'],
         [' ', ' ', 'X'],
         [' ', 'O', 'X']]
if Judge(Board) != 1:
    print('Judge error7')
    score_Judge=0
#%%
Board = [[' ', ' ', 'X'],
         ['O', 'X', 'O'],
         ['X', ' ', ' ']]
if Judge(Board) != 1:
    print('Judge error8')
    score_Judge=0
#%%
Board = [['X', ' ', ' '],
         ['O', 'X', 'O'],
         [' ', ' ', 'X']]
if Judge(Board) != 1:
    print('Judge error9')
    score_Judge=0
#%%
Board = [['X', 'X', 'O'],
         ['X', 'O', 'O'],
         ['X', 'O', 'X']]
if Judge(Board) != 1:
    print('Judge error10')
    score_Judge=0
#%%
Board = [['X', ' ', 'X'],
         ['X', ' ', ' '],
         ['O', 'O', 'O']]
if Judge(Board) != 2:
    print('Judge error11')
    score_Judge=0
#%%
Board = [['X', ' ', 'X'],
         ['O', 'O', 'O'],
         ['X', ' ', ' ']]
if Judge(Board) != 2:
    print('Judge error12')
    score_Judge=0
#%%    
Board = [['O', 'O', 'O'],
         ['X', ' ', ' '],
         ['X', ' ', 'X']]
if Judge(Board) != 2:
    print('Judge error13')
    score_Judge=0
#%%
Board = [['O', 'X', 'X'],
         ['O', ' ', ' '],
         ['O', ' ', 'X']]
if Judge(Board) != 2:
    print('Judge error14')
    score_Judge=0
#%%
Board = [['X', 'O', 'X'],
         [' ', 'O', ' '],
         [' ', 'O', 'X']]
if Judge(Board) != 2:
    print('Judge error15')
    score_Judge=0
#%%
Board = [['X', 'X', 'O'],
         [' ', ' ', 'O'],
         ['X', ' ', 'O']]
if Judge(Board) != 2:
    print('Judge error16')
    score_Judge=0
#%%
Board = [['O', 'X', 'X'],
         [' ', 'O', ' '],
         ['X', ' ', 'O']]
if Judge(Board) != 2:
    print('Judge error17')
    score_Judge=0
#%%
Board = [['X', 'X', 'O'],
         [' ', 'O', ' '],
         ['O', ' ', 'X']]
if Judge(Board) != 2:
    print('Judge error18')
    score_Judge=0
#%%
Board = [['X', 'X', 'O'],
         ['X', 'O', 'O'],
         ['O', 'X', 'X']]
if Judge(Board) != 2:
    print('Judge error19')
    score_Judge=0
print("Judge: score=", score_Judge)    
#%%
score=(score_TicTacToeGame
       +score_IsSpaceFree
       +score_GetNumberOfChessPieces
       +score_IsBoardFull 
       +score_IsBoardEmpy
       +score_UpdateBoard
       +score_ComputerPlayer
       +score_Judge
       +score_HumanPlayer
       +score_ShowOutcome
       +score_DrawBoard)

print("total score (100)=", score)    
print("This tester may not find all of the bugs in your code")    


