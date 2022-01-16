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

# 2 - Player one uses x's. Player two uses o's.
current_player = "X"


# ------------- Functions ---------------

# Play a game of tic tac toe
def main():

  # Show the initial game board
  display_board()
    
  # Handle a turn
  turn(current_player)

  # Flip to the other player
  flip_player()


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# Handle a turn for an arbitrary player
def turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("Go again.")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  display_board()

  # 2 - Player one uses x's. Player two uses o's.
def flip_player():
  global current_player
  # If the current player was X, make it O
  if current_player == "X":
    current_player = "O"
  # Or if the current player was O, make it X
  elif current_player == "O":
    current_player = "X"

# ------------ Start Execution -------------
# It plays the game.
main()