from ai import *
from human import *
from board import *
import pygame

class Game(object):
  """
  Game object that holds the state of the board and players' moves
  """

  board = None
  player1 = None
  player2 = None
  winner = None
  turn_count = None

  def __init__(self):
    print "Welcome to CS 4701 Connect 4!"
    print "Please refer to Google regarding the rules of this game."
    valid = False
    while not valid:
      entity = raw_input("Would you like player 1 to be a computer? [Y/n]")
      if entity.lower() == 'y':
        self.player1 = AI()
        valid = True
      elif entity.lower() == 'n':
        self.player1 = Human(1)
        valid = True
      else:
        print "Please input a valid option."

    print "Great!"

    valid = False
    while not valid:
      entity = raw_input("Would you like player 2 to be a computer? [Y/n]")
      if entity.lower() == 'y':
        self.player2 = AI()
        valid = True
      elif entity.lower() == 'n':
        self.player2 = Human(2)
        valid = True
      else:
        print "Please input a valid option."

    print "Great!"

    complete = False
    while not complete:
      self.board = Board()
      print self.board
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
    complete = False
    while not complete:
      print "Player 1's turn!"
      self.player1.next_move(self.board)
      print self.board
      print self.board.check_win(1)
      if self.board.check_win(1)[0]:
        print "Player 1 wins!"
        return 1

      print "Player 2's turn!"
      self.player2.next_move(self.board)
      print self.board
      if self.board.check_win(2)[0]:
        print "Player 2 wins!"
        return 2


if __name__ == "__main__":
    game = Game()