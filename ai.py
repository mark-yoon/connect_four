import board
import time
import sys
import random
import copy

class AI(object):

  def __init__(self, player_num, is_pruning, search_depth, heuristic):
    self.player_num = player_num
    # If true, will perform alpha-beta pruning when doing minimax
    self.is_pruning = is_pruning
    # Trees will be created with max depth search_depth
    self.search_depth = search_depth
    # Represents heuristic used in minimax
    self.heuristic = heuristic

  def next_move(self, board):
    # Returns a next move as an integer representing the column
    if self.heuristic == 1:
      return self.random(board)
    # Balanced heuristic
    if self.heuristic == 2:
      board_copy = copy.deepcopy(board)
      return self.minimax(board_copy, self.search_depth, self.player_num, self.balanced)[0]
    if self.heuristic == 3:
      board_copy = copy.deepcopy(board)
      return self.minimax(board_copy, self.search_depth, self.player_num, self.offensive)[0]
    if self.heuristic == 4:
      board_copy = copy.deepcopy(board)
      return self.minimax(board_copy, self.search_depth, self.player_num, self.defensive)[0]

  def random(self, board):
    moves = board.valid_moves()
    return random.choice(moves)

  def minimax(self, board, depth, player_num, heuristic):
    # Set player values
    if player_num == 1:
      opp_num = 2
    else:
      opp_num = 1

    # Start search for each valid move
    possible_moves = [float("-inf") for i in range(board.x_max)]
    for col in board.valid_moves():
      board_copy = copy.deepcopy(board)
      board_copy.add(col, player_num)
      possible_moves[col] = -self.search(board_copy, depth - 1, opp_num, heuristic)

    # Take the move with the highest value
    h = max(possible_moves)
    move = possible_moves.index(h)
    print (move, h)
    return (move, h)

  def search(self, board, depth, player_num, heuristic):
    if player_num == 1:
      opp_num = 2
    else:
      opp_num = 1

    # Check if leaf
    if depth == 0 or len(board.valid_moves()) == 0 or board.check_win(player_num)[0] or board.check_win(opp_num)[0]:
      return heuristic(board, player_num)

    # Get all possible board states from the given board
    possible_moves = []
    for col in board.valid_moves():
      board_copy = copy.deepcopy(board)
      board_copy.add(col, player_num)
      possible_moves.append(board_copy)

    # Run search recursively
    h = float("-inf")
    for move in possible_moves:
      h = max(h, -self.search(move, depth - 1, opp_num, heuristic))
    return h

  # Heuristic
  def balanced(self, board, player_num):
    if player_num == 1:
      opp_num = 2
    else:
      opp_num = 1
    (my_fours, my_threes, my_twos) = board.get_connected(player_num)
    (opp_fours, opp_threes, opp_twos) = board.get_connected(opp_num)

    my_score = my_fours * 1000000 + my_threes * 10000 + my_twos * 10
    opp_score = opp_fours * 1000000 + opp_threes * 10000 + opp_twos * 10
    return my_score - opp_score

  def offensive(self, board, player_num):
    if player_num == 1:
      opp_num = 2
    else:
      opp_num = 1
    (my_fours, my_threes, my_twos) = board.get_connected(player_num)
    (opp_fours, opp_threes, opp_twos) = board.get_connected(opp_num)

    my_score = my_fours * 1000000 + my_threes * 10000 + my_twos * 10
    opp_score = opp_fours * 1000000
    return my_score - opp_score

  def defensive(self, board, player_num):
    if player_num == 1:
      opp_num = 2
    else:
      opp_num = 1
    (my_fours, my_threes, my_twos) = board.get_connected(player_num)
    (opp_fours, opp_threes, opp_twos) = board.get_connected(opp_num)

    my_score = my_fours * 1000000
    opp_score = opp_fours * 1000000 + opp_threes * 10000 + opp_twos * 10
    return my_score - opp_score