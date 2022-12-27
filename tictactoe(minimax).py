import copy

def play_tic_tac_toe():
  # Initialize the board
  board = [[' ' for _ in range(3)] for _ in range(3)]

  # Define the players
  players = ['X', 'O']

  # Iterate through each player's turn
  for player in itertools.cycle(players):
    # Print the current board
    print_board(board)

    # If it's the AI's turn, get the optimal move
    if player == 'O':
      row, col = get_optimal_move(board, player)
    # If it's the human player's turn, get their move
    else:
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

def get_optimal_move(board, player):
  # Create a copy of the board to perform the minimax algorithm on
  copy_board = copy.deepcopy(board)

  # Initialize the best score and best move to the lowest possible values
  best_score = float('-inf')
  best_move = None

  # Iterate through all the empty spaces on the board
  for row in range(3):
    for col in range(3):
      if copy_board[row][col] == ' ':
        # Make a move in the current empty space
        copy_board[row][col] = player
        # Get the score of the move using the minimax function
        score = minimax(copy_board, player, False)
        # Undo the move
        copy_board[row][col] = ' '
        # If the score is higher than the current best score, update the best score and best move
        if score > best_score:
          best_score = score
          best_move = (row, col)
  
  return best_move

def minimax(board, player, is_maximizing):
  # Check if the current player has won
  if has_won(player, board):
    return 1 if is_maximizing else -1

  # Check if the game is a draw
  if is_draw(board):
    return 0

  # Initialize the best score to the lowest possible value
  best_score = float('-inf') if is_maximizing else float('inf')

  # Iterate through all the empty spaces on the board
  for row in range(3):
    for col in range(3):
      if board[row][col] == ' ':
        # Make a move in the current empty space
        board[row][col] = player
        # Get the score of the move using recursive minimax call
        if is_maximizing:
          score = minimax(board, 'O' if player == 'X' else 'X', False)
          best_score = max(best_score, score)
        else:
          score = minimax(board, 'O' if player == 'X' else 'X', True)
          best_score = min(best_score, score)
        # Undo the move
        board[row][col] = ' '
  
  return best_score

# Start the game
play_tic_tac_toe()

