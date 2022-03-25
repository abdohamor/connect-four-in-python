# --------------------------------------------------- name \ Abdulrahman Muhammad Muhammad ---------------------------------------------------------------------
# --------------------------------------------------- ID   \ 20210581                      ---------------------------------------------------------------------
# --------------------------------------------------- Game number1                         ----------------------------------------------------------------------
# --------------------------------------------------- Connect 4                            ----------------------------------------------------------------------



import numpy as np
import string 
board =np.zeros((7,7),dtype=str)
board[0]=list(string.ascii_uppercase)[:7]
board=np.where(board=='',' ',board)
 

player1_choice =input("please 1 enter your mark (x,o): ").upper()

if player1_choice=='X':
    player2_choice='O'
else:
    player2_choice='X'


print(board)
col_idx={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}
free_cells={'A':6,'B':6,'C':6,'D':6,'E':6,'F':6,'G':6}
idx_col={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G'}

def player1_turn():
    col=input('where to play: ').upper()
    column_index=col_idx[col]
    all_cells=board[1:,column_index]
    empty_cells=(all_cells==' ').sum()
    if empty_cells==6:
        all_cells[-1]=player1_choice
        free_cells[col]-=1
    else:
        all_cells[empty_cells-7]=player1_choice
        free_cells[col]-=1
    print(board)


def player2_turn():
    col=input('where to play: ' ).upper()
    column_index=col_idx[col]
    all_cells=board[1:,column_index]
    empty_cells=(all_cells==' ').sum()
    if empty_cells==6:
        all_cells[-1]=player2_choice
        free_cells[col]-=1
    else:
        
        all_cells[empty_cells-7]=player2_choice
        free_cells[col]-=1
    print(board)


def score(col):
    x_score=0
    o_score=0
    for cell in col:
        if cell =='X':
            x_score+=1
        else:
            if x_score% 4 !=0:
                x_score=x_score - (x_score%4)

        if cell =='O':
            o_score+=1
        else:
            if o_score% 4 !=0:
                o_score=o_score - (o_score%4)
        
    if player1_choice=='X':
        player1_score=x_score//4
        player2_score=o_score//4
    else:
        player2_score=x_score//4
        player1_score=o_score//4



    return player1_score,player2_score
            


for i in range(21):
    player1_turn()
    player2_turn()
print("###game over###")
player1_score_total=0
player2_score_total=0
for row in range(6):
    col=board [row+1]
    player1,player2=score(col)
    player1_score_total+=player1
    player2_score_total+=player2
    if row <4 :
        col =board[1:].diagonal(row)
        player1,player2=score(col)
        player1_score_total+=player1
        player2_score_total+=player2
        
        flipped_board=np.flip(board[1:],axis=0)
        col =flipped_board[1:].diagonal(row)
        player1,player2=score(col)
        player1_score_total+=player1
        player2_score_total+=player2
    else:
        col =board[1:].diagonal(row-6)
        player1,player2=score(col)
        player1_score_total+=player1
        player2_score_total+=player2
        
        flipped_board=np.flip(board[1:],axis=0)
        col =flipped_board[1:].diagonal(row-6)
        player1,player2=score(col)
        player1_score_total+=player1
        player2_score_total+=player2


for column in range(7):
    col=board [1,column]
    player1,player2=score(col)
    player1_score_total+=player1
    player2_score_total+=player2


print("player1 score:  {}".format(str(player1_score_total)))
print("player2 score:  {}".format(str(player2_score_total)))



if player1_score_total>player2_score_total:
    print("player1 wins ")

else:
    print("player2 wins")
