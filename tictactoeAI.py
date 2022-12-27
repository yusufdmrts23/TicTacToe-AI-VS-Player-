import random

# Constants for the game board
X = "X"
O = "O"
BLANK = " "

# Constants for the AI player
AI = X
HUMAN = O

# The game board represented as a list
board = [BLANK, BLANK, BLANK,
         BLANK, BLANK, BLANK,
         BLANK, BLANK, BLANK]

# Function to display the current state of the game board
def display_board():
  print(f" {board[0]} | {board[1]} | {board[2]} ")
  print("---+---+---")
  print(f" {board[3]} | {board[4]} | {board[5]} ")
  print("---+---+---")
  print(f" {board[6]} | {board[7]} | {board[8]} ")

# Function to make a move on the game board
def make_move(player, index):
  board[index] = player

# Function to check if a player has won the game
def has_won(player):
  # Check rows
  if board[0] == player and board[1] == player and board[2] == player:
    return True
  if board[3] == player and board[4] == player and board[5] == player:
    return True
  if board[6] == player and board[7] == player and board[8] == player:
    return True

  # Check columns
  if board[0] == player and board[3] == player and board[6] == player:
    return True
  if board[1] == player and board[4] == player and board[7] == player:
    return True
  if board[2] == player and board[5] == player and board[8] == player:
    return True

  # Check diagonals
  if board[0] == player and board[4] == player and board[8] == player:
    return True
  if board[2] == player and board[4] == player and board[6] == player:
    return True

  return False

# Function to check if the game is a draw
def is_draw():
  return BLANK not in board

# Function to get a list of valid moves
def get_valid_moves():
  moves = []
  for i in range(9):
    if board[i] == BLANK:
      moves.append(i)
  return moves

# AI function to determine the best move to make
def get_best_move(player):
  # Check if we can win in the next move
  for i in get_valid_moves():
    make_move(player, i)
    if has_won(player):
      make_move(BLANK, i)
      return i

  # Check if the human player can win in the next move and block them
  for i in get_valid_moves():
    make_move(HUMAN, i)
    if has_won(HUMAN):
      make_move(BLANK, i)
      return i
    make_move(BLANK, i)

  # Try to take a corner
  corners = [0, 2, 6, 8]
  for i in corners:
    if board[i] == BLANK:
      return i

  # Try to take the center
  if board[4] == BLANK:
    return 4

  # Take any remaining space
  return get_valid_moves()[0]

# Main game loop
while True:
  # Display the current state of the game board
  display_board()

  # Get the human player's move
  move = int(input("Enter your move (0-8): "))
  if board[move] != BLANK:
    print("Invalid move, try again.")
    continue
  make_move(HUMAN, move)

  # Check if the human player has won
  if has_won(HUMAN):
    display_board()
    print("You won!")
    break

  # Check if the game is a draw
  if is_draw():
    display_board()
    print("It's a draw.")
    break

  # Make the AI's move
  move = get_best_move(AI)
  make_move(AI, move)

  # Check if the AI has won
  if has_won(AI):
    display_board()
    print("The AI won.")
    break

