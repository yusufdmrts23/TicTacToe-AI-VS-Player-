import itertools

def play_tic_tac_toe():
  # Initialize the board
  board = [[' ' for _ in range(3)] for _ in range(3)]

  # Define the players
  players = ['X', 'O']

  # Iterate through each player's turn
  for player in itertools.cycle(players):
    # Print the current board
    print_board(board)

    # Get the player's move
    row, col = get_move(player, board)

    # Make the move
    board[row][col] = player

    # Check if the player has won
    if has_won(player, board):
      print(f'{player} has won!')
      break

    # Check if the game is a draw
    if is_draw(board):
      print('The game is a draw!')
      break

def print_board(board):
  print('-' * 13)
  for row in board:
    print('|', *row, '|')
  print('-' * 13)

def get_move(player, board):
  while True:
    try:
      row = int(input(f'{player}, enter row (0-2): '))
      col = int(input(f'{player}, enter col (0-2): '))
      if board[row][col] == ' ':
        return row, col
      print('That space is already occupied. Try again.')
    except ValueError:
      print('Invalid input. Try again.')
    except IndexError:
      print('Invalid indices. Try again.')

def has_won(player, board):
  # Check rows
  for row in board:
    if all(cell == player for cell in row):
      return True

  # Check columns
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True

  # Check diagonals
  if all(board[i][i] == player for i in range(3)):
    return True
  if all(board[i][2-i] == player for i in range(3)):
    return True

def is_draw(board):
  return all(cell != ' ' for row in board for cell in row)

# Start the game
play_tic_tac_toe()
