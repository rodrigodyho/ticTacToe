"""
*
Assignment: 
W02 Prove: Developer - Solo Code Submission (Tic tac toe)

1 - The game is played on a grid that is three squares by three squares.
2 - Player one uses x's. Player two uses o's.
3 - Players take turns putting their marks in empty squares.
4 - The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
5 - If all nine squares are full and neither player has three in a row, the game ends in a draw.

Author = Rodrigo Lima
*Credits = Python for absolute beginners 2019 - TIC TAC TOE project (where
I learned how to do this project.)
"""

# --------- Global Variables -----------

# 1- The game is played on a grid that is three squares by three squares.
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# ------------- Functions ---------------

# Play a game of tic tac toe
def main():

  # Show the initial game board
  display_board()


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

# ------------ Start Execution -------------
# It plays the game.
main()