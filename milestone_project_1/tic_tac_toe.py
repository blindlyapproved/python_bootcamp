# Here are the requirements:
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
# tic tac toe game
# each player must change sides at every turn
# x or o as input(): ==> no number as input
# after every move, print out the board print(board)
# use numpad to match numbers to the grid 3*3, rasterize them, 1,2,3,4,5,6,7,8,9
# ask player if he wants to be x or o
# ready to play? yes / no 
# while loop, use {} for input in 
# do you want to play again?
# scoreboard would be cool
# 789 - 456 - 123

# firstly we need to create the board with corrensponding numbers
# then upon launching the program, we need to ask the user if they want to start
# player 1 can start and inputs x, player 2 follows inputting 0
# upon condition that on 123, 456, 789 or diagonal, 3 same values can be found player wins

def display_board(board):    
    print(board[7]+"|"+board[8]+"|"+board[9]+"|")
    print("------")
    print(board[4]+"|"+board[5]+"|"+board[6]+"|")
    print("------")
    print(board[1]+"|"+board[2]+"|"+board[3]+"|")


def player_input():
    
    marker = ''
    
    while marker != "X" and marker != "O":
        marker = input("Player 1, choose X or O to start:")
        
    player1 = marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    
    return (player1, player2)

player_input()

def place_marker(board, marker, position):
    
    board = [""]

    for marker in board:
        position = int(input("Place your position"))
        while position in board:
            board.append(position, [0,10])

place_marker()

def win():
    pass


def play_again():
    pass    