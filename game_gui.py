from ai import *
from human import *
from board import *
import pygame



  # def play_game(self):
  #   complete = False
  #   while not complete:
  #     print "Player 1's turn!"
  #     self.player1.next_move(self.board)
  #     print self.board
  #     print self.board.check_win(1)
  #     if self.board.check_win(1)[0]:
  #       print "Player 1 wins!"
  #       return 1

  #     print "Player 2's turn!"
  #     self.player2.next_move(self.board)
  #     print self.board
  #     if self.board.check_win(2)[0]:
  #       print "Player 2 wins!"
  #       return 2

# ==============================================================================================================

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init()
size = (800,900)
screen = pygame.display.set_mode(size)
screen.fill(white)
pygame.display.set_caption("Connect 4")
running = True

game_state = 0

def create_text(screen, font_path, size, text, color, center):
  font = pygame.font.Font(font_path, size)
  text = font.render(text, 0, color)
  textpos = text.get_rect()
  textpos.centerx = center[0]
  textpos.centery = center[1]
  screen.blit(text, textpos)

def create_rect(screen, rect, color, center, thickness):
  rectangle = pygame.Rect(rect)
  rectangle.center = center
  pygame.draw.rect(screen, color, rectangle, thickness)
  return rectangle

def init():
  global player1
  global player2
  global board
  global turn
  global victory
  global human
  global ai
  global player1_locs
  global player2_locs

  player1 = Human(1)
  player2 = Human(2)
  board = Board()
  turn = 1
  victory = False
  human = 0
  ai = 0
  player1_locs = []
  player2_locs = []

init()

while running: 
  screen.fill(white)
  if game_state == 0:
    play_rect = create_rect(screen, [10, 10, 200, 100], black, (400, 450), 1)

    create_text(screen, "font/mario.ttf", 25, "PLAY", black, screen.get_rect().center)
    create_text(screen, "font/mario.ttf", 45, "Welcome to Connect 4!", black, (screen.get_rect().centerx, screen.get_rect().centery -200))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if play_rect.collidepoint(event.pos):
          game_state = 1
      pygame.display.update()


  if game_state == 1:
    if turn == 1:
      color = red
    else:
      color = blue

    x_center = 0
    y_center = 900
    game_rects = []
    col = -1

    for i in range(0, 7):
      x_center += 100
      y_center = 900
      col = []
      for j in range(0, 6):
        y_center -= 100
        if (i, j) in player1_locs:
          col.append(create_rect(screen, [10, 10, 99, 99], red, (x_center, y_center), 0))
        elif (i, j) in player2_locs:
          col.append(create_rect(screen, [10, 10, 99, 99], blue, (x_center, y_center), 0))
        col.append(create_rect(screen, [10, 10, 100, 100], black, (x_center, y_center), 1))
      game_rects.append(col)

    if victory:
      create_text(screen, "font/mario.ttf", 25, "Try again?", black, (400, 175))
      try_again = create_rect(screen, [10, 10, 200, 50], black, (400, 175), 1)
      if turn == 1:
        create_text(screen, "font/mario.ttf", 40, "You won!!", black, (400, 100))
      else:
        create_text(screen, "font/mario.ttf", 40, "You lost...", black, (400, 100))
    else:
      if turn == 1:
        create_text(screen, "font/mario.ttf", 25, "Your turn!", black, (400, 100))
      else:
        create_text(screen, "font/mario.ttf", 25, "AI's turn!", black, (400, 100))


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if victory:
          if try_again.collidepoint(event.pos):
            init()
        else:
          for col in range(0, len(game_rects)):
            for rect in game_rects[col]:
              if rect.collidepoint(event.pos):
                add = board.add(col, turn)
                if add[0]:
                  if turn == 1:
                    player1_locs.append((add[1], add[2]))
                  else:
                    player2_locs.append((add[1], add[2]))

                  if board.check_win(turn)[0]:
                    victory = True
                    if turn == 1:
                      human += 1
                    else:
                      ai += 1
                  else:
                    if turn == 1:
                      turn = 2
                    else:
                      turn = 1
                else:
                  # Display invalid column here
                  pass
    pygame.display.update()
