
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
    print "Welcome to CS 4701 Connect 4!"
    print "Please refer to Google regarding the rules of this game."
    entity = raw_input("Would you like player 1 to be a computer? [Y/n]")
    while player1 == None:
      if entity.lower() == 'y':
        player1 = AI('o')
      elif entity.lower() == 'n':
        player1 = Human('o')
      else:
        print "Please input a valid option."
        entity = raw_input("Would you like player 1 to be a computer? [Y/n]")

    print "Great!"
    entity2 = raw_input("Would you like player 2 to be a computer? [Y/n]")
    while entity2 == None:
      if entity2.lower() == 'y':
        player2 = AI('x')
      elif entity2.lower() == 'n':
        player2 = Human('x')
      else:
        print "Please input a valid option."
        entity2 = raw_input("Would you like player 1 to be a computer? [Y/n]")
