import board
import time
import sys
import random

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
    elif self.heuristic == 2:
      return self.naive(board)
    else:
      return self.minimax(board)

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


