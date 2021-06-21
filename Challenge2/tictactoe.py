#setup
n = 3
m = 3
board = [["-"] * m for i in range(n)]
play=True
turn=1
empty = "-"
repeat = True
win=False
count=0
#check win
def checkWin(board):
    if (board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X"):
        return True
    elif(board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X"):
        return True
    elif(board[2][0]=="X" and board[0][2]=="X" and board[1][1]=="X"):
        return True
    elif(board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X"):
        return True
    elif(board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X"):
        return True
    elif(board[1][0]=="X" and board[2][0]=="X" and board[0][0]=="X"):
        return True
    elif(board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X"):
        return True
    elif(board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X"):
        return True
    elif (board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O"):
        return True
    elif(board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O"):
        return True
    elif(board[2][0]=="O" and board[0][2]=="O" and board[1][1]=="O"):
        return True
    elif(board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O"):
        return True
    elif(board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O"):
        return True
    elif(board[1][0]=="O" and board[2][0]=="O" and board[0][0]=="O"):
        return True
    elif(board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O"):
        return True
    elif(board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O"):
        return True   
    else:
        return False

#check for draw
def boardCheck(count):
    for i in range (3):
        for j in range (3):
            if board[i][j]!="-":
                count+=1
    if count==9:
        return True
    return False

#game
while play:
    #output board
    repeat=True
    print(123)
    print(456)
    print(789)
    for i in range (3):
        for j in range (3):
            print(board[i][j], end="")
        print()
    if (boardCheck(count)):
        print("It's a draw!")
        break
    #player 1
    if turn==1:
        while repeat:
            pos = input("Enter a corresponding number! \nPlayer 1:")
            pos.lower
            #placement of X on board
            if (pos=='1' and board[0][0]==empty):
                board[0][0]=board[0][0].replace('-',"X")
                repeat=False
            elif (pos=='2' and board[0][1]==empty):
                board[0][1]=board[0][1].replace('-',"X")
                repeat=False
            elif (pos=='3' and board[0][2]==empty):
                board[0][2]=board[0][2].replace('-',"X")
                repeat=False
            elif (pos=='4' and board[1][0]==empty):
                board[1][0]=board[1][0].replace('-',"X")
                repeat=False
            elif (pos=='5' and board[1][1]==empty):
                board[1][1]=board[1][1].replace('-',"X")
                repeat=False
            elif (pos=='6' and board[1][2]==empty):
                board[1][2]=board[1][2].replace('-',"X")
                repeat=False
            elif (pos=='7' and board[2][0]==empty):
                board[2][0]=board[2][0].replace('-',"X")
                repeat=False
            elif (pos=='8' and board[2][1]==empty):
                board[2][1]=board[2][1].replace('-',"X")
                repeat=False
            elif (pos=='9' and board[2][2]==empty):
                board[2][2]=board[2][2].replace('-',"X")
                repeat=False
            #checks for win and changes turns
            if not repeat:
                if checkWin(board):
                    print("Player 1 Won!!")
                    play=False
                    break
                turn=2
    #player 2
    elif turn==2:
        while repeat:
            pos = input("Enter a corresponding number! \nPlayer 2:")
            pos.lower
            #placement of O on board
            if (pos=='1' and board[0][0]==empty):
                board[0][0]=board[0][0].replace('-',"O")
                repeat=False
            elif (pos=='2' and board[0][1]==empty):
                board[0][1]=board[0][1].replace('-',"O")
                repeat=False
            elif (pos=='3' and board[0][2]==empty):
                board[0][2]=board[0][2].replace('-',"O")
                repeat=False
            elif (pos=='4' and board[1][0]==empty):
                board[1][0]=board[1][0].replace('-',"O")
                repeat=False
            elif (pos=='5' and board[1][1]==empty):
                board[1][1]=board[1][1].replace('-',"O")
                repeat=False
            elif (pos=='6' and board[1][2]==empty):
                board[1][2]=board[1][2].replace('-',"O")
                repeat=False
            elif (pos=='7' and board[2][0]==empty):
                board[2][0]=board[2][0].replace('-',"O")
                repeat=False
            elif (pos=='8' and board[2][1]==empty):
                board[2][1]=board[2][1].replace('-',"O")
                repeat=False
            elif (pos=='9' and board[2][2]==empty):
                board[2][2]=board[2][2].replace('-',"O")
                repeat=False
            #checks for win and changes turns
            if not repeat:
                if checkWin(board):
                    print("Player 1 Won!!")
                    play=False
                    break
                turn=1
#game end output of board
for i in range (3):
    for j in range (3):
        print(board[i][j], end="")
    print()
