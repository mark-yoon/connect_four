
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
    valid = False
    while not valid:
      entity = raw_input("Would you like player 1 to be a computer? [Y/n]")
      if entity.lower() == 'y':
        player1 = AI('o')
        valid = True
      elif entity.lower() == 'n':
        player1 = Human('o')
        valid = True
      else:
        print "Please input a valid option."

    print "Great!"

    valid = False
    while not valid:
      entity = raw_input("Would you like player 2 to be a computer? [Y/n]")
      if entity.lower() == 'y':
        player2 = AI('x')
        valid = True
      elif entity.lower() == 'n':
        player2 = Human('x')
        valid = True
      else:
        print "Please input a valid option."

    complete = false
    while not complete:
      outcome = self.play_game()
      valid = False
      while not valid:
        again = raw_input("Would you like to play again? [Y/n]")
        if again.lower() == 'y':
          valid = True
        elif again.lower() == 'n':
          print "Thank you for playing!"
          return
        else:
          print "Please input a valid option."


  def play_game(self):
    complete = false
    while not complete:
      print "Player 1's turn!"
      player1.nextmove(board)
      print board
      if board.check_win(1):
        print "Player 1 wins!"
        return 1

      print "Player 2's turn!"
      player2.nextmove(board)
      print board
      if board.check_win(2):
        print "Player 2 wins!"
        return 2
