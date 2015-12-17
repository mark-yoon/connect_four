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
    else:
      board_copy = copy.deepcopy(board)
      print self.get_move(board_copy, 5, self.player_num)[0]
      return self.get_move(board_copy, 5, self.player_num)[0]

  def minimax(self, board):
    # Performs minimax algorithm on board state tree
    # Max and min values for each state tree
    max_score = sys.maxint
    min_score = -max_score - 1

    # Perform alpha-beta pruning
    if self.is_pruning:
      # TODO
      return
    else:
      # Expand tree from current state node
      for cur_depth in range(self.search_depth):
        max_value = 0
        for cur_col in range(board.x_max):
          # All possible moves (not filled column)
          if not board.cells[cur_col][board.y_max] is 0:
            # Return greatest value path
            if get_value(board, cur_col) > max_value:
              return cur_col

  def random(self, board):
    moves = board.valid_moves()
    return random.choice(moves)

  def naive(self, board):
    # Naive algorithm for ai
    return 1

  # def get_value(self, board, column):
  #   # Gives value of move specified by column on board board
  #   # Applies move column to board (undo move afterwards) then calculates its value
  #   if self.heuristic == 1:
  #     # 4 in a row has value of infinity
  #     # value = #{3 in a row} * 100 +  #{2 in a row} * 10
  #     revert = board

  #     // "Apply move to board"
  #     // "Check value of board"


  def get_move(self, board, depth, player_num):
    if player_num == 1:
      opp_num = 2
    else:
      opp_num = 1

    possible_moves = [0 for i in range(board.x_max)]
    for col in board.valid_moves():
      board_copy = copy.deepcopy(board)
      board_copy.add(col, player_num)
      possible_moves[col] = -self.search(board_copy, depth - 1, opp_num)

    h = max(possible_moves)
    move = possible_moves.index(h)

    return (move, h)

  def search(self, board, depth, player_num):
    if player_num == 1:
      opp_num = 2
    else:
      opp_num = 1

    if depth == 0 or len(board.valid_moves()) == 0 or board.check_win(player_num)[0] or board.check_win(opp_num)[0]:
      return self.eval_board(board, player_num)

    possible_moves = []
    for col in board.valid_moves():
      board_copy = copy.deepcopy(board)
      board_copy.add(col, player_num)
      possible_moves.append(board_copy)

    h = float("-inf")
    for move in possible_moves:
      h = max(h, -self.search(move, depth - 1, opp_num))
    return h

  # Heuristic
  def eval_board(self, board, player_num):
    if player_num == 1:
      opp_num = 2
    else:
      opp_num = 1
    my_fours = board.fours(player_num)
    my_threes = board.threes(player_num)
    my_twos = board.twos(player_num)

    opp_fours = board.fours(opp_num)
    opp_threes = board.threes(opp_num)
    opp_twos = board.twos(opp_num)

    my_score = len(my_fours) * 100000 + len(my_threes) * 1000 + len(my_twos)
    opp_score = len(opp_fours) * 100000 + len(opp_threes) * 1000 + len(opp_twos)
    return my_score - opp_score
