class Human(object):
  total_wins = 0
  player_num = 0

  def __init__(self, player_num):
    self.total_wins = 0
    self.player_num = player_num

  def next_move(self, board):
    valid = False
    while not valid:
      column = raw_input("Which column would you like your next move to be in?")
      try:
        column = int(column)
        print column
        if column < 0 or column > 6:
          print "Please input a valid integer from 0~6."
        else:
          if not board.add(column, self.player_num):
            print "This is an invalid move. Please try again."
          else:
            valid = True
      except:
        print "Please input a valid integer from 0~6."