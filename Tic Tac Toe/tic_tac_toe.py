# Tic Tac Toe Game
# Comments are first attempt

import random,os

def display_board(board):
  os.system('cls')
  print(' {} | {} | {}'.format(board[7],board[8],board[9]))
  print('------------')
  print(' {} | {} | {}'.format(board[4],board[5],board[6]))
  print('------------')
  print(' {} | {} | {}'.format(board[1],board[2],board[3]))
  

def player_input():
  markers_picked = False
  while(markers_picked == False):
    player1 = input("Please pick a marker 'X' or 'O': ").upper()
    player2 = ''
    if player1 == 'X':
      player2 = 'O'
      markers_picked = True
    elif player1 == 'O':
      player2 = 'X'
      markers_picked = True
    else:
      continue
  
  print('Player 1 is ' + player1)
  print('Player 2 is ' + player2)
  return player1,player2

def place_marker(board,marker,position):
  board[position] = marker
  return board

def win_check(board,mark):
  return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
  goes_first = random.randint(1,2)
  if goes_first == 1:
    return "Player 1"
  elif goes_first == 2:
    return "Player 2"


def space_check(board,position):
  return board[position] == ' '

def full_board_check(board):
  # check = False
  # count = 0
  # for space in board:
  #   if space == ' ':
  #     continue
  #   else:
  #     count += 1
  # if count == 10:
  #   check = True
  # return check
  if " " in board[1:]:
    return False
  else:
    return True

def player_choice(board):
  position = 0
  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
    position = int(input("Choose your next position: (1-9): \n"))
  
  return position

def replay():
  # replay_check = input('Do you want to play again? Press Y to continue\n')
  # if replay_check == 'Y' or replay_check == 'y':
  #   return True
  # else:
  #   return False
  return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
  # Reset board

  the_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
  player1_marker, player2_marker = player_input()
  turn = choose_first()
  print(turn + ' will go first.')

  play_game = input('Are you ready to play? Enter Yes or no. ')

  if play_game.lower()[0] == 'y':
    game_on = True
  else:
    game_on = False

  while game_on:
    if turn == 'Player 1':
      # Player1's turn.

      display_board(the_board)
      player1_placement = player_choice(the_board)
      place_marker(the_board,player1_marker,player1_placement)

      if win_check(the_board,player1_marker):
        display_board(the_board)
        print('Congratulations! You have won!')
        game_on = False
      else:
        if full_board_check(the_board):
          display_board(the_board)
          print('The game is a draw!')
          break
        else:
          turn = 'Player 2'
    else:
      # Player2's turn.

      display_board(the_board)
      player2_placement = player_choice(the_board)
      place_marker(the_board,player2_marker,player2_placement)

      if win_check(the_board,player2_marker):
        display_board(the_board)
        print('Congratulations! You have won!')
        game_on = False
      else:
        if full_board_check(the_board):
          display_board(the_board)
          print('The game is a draw!')
          break
        else:
          turn = 'Player 1'

  if not replay():
    break
