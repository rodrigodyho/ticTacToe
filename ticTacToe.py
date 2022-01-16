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

# Lets us know if the game is over yet
still_playing = True

# Tells us who the winner is
winner = None

# 2 - Player one uses x's. Player two uses o's.
current_player = "X"


# ------------- Functions ---------------

# Play a game of tic tac toe
def main():

  # Show the initial game board
  display_board()

  # Loop until the game stops (winner or draw)
  while still_playing:

    # Handle a turn
    turn(current_player)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()
  
  # Since the game is over, print the winner or draw
  if winner == "X" or winner == "O":
    print(winner + " won. Good game! Thanks for playing!")

#5 -When the game ends in a draw.
  elif winner == None:
    print("draw.")


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

#4 - The first player to get three of their marks in a 
# row (vertically, horizontally, or diagonally) is the winner.
#---------------------------------------------------------
# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_draw()


# Check to see if somebody has won
def check_for_winner():
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  global still_playing
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    still_playing = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():
  global still_playing
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    still_playing = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # 5 - If all nine squares are full and neither player has three in a row, the game ends in a draw.
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  global still_playing
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    still_playing = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or return None if there was no winner
  else:
    return None


# Check if there is a draw
def check_for_draw():
  global still_playing
  # If board is full
  if "-" not in board:
    still_playing = False
    return True
  # Else there is no draw
  else:
    return False


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