
class Game(object):
  """
  Game object that holds the state of the board and players' moves
  """

  board = None
  player1 = None
  player2 = None
  winner = None
  turn_count = None

  def init(self):
    