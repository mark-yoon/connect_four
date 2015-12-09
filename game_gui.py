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

pygame.init()
size = (800,700)
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

player1 = Human(1)
player2 = Human(2)
board = Board()

while running: 
  screen.fill(white)
  if game_state == 0:
    play_rect = create_rect(screen, [10, 10, 200, 100], black, (400, 350), 1)

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

    x_center = 0
    y_center = 0

    for i in range(0, 7):
      x_center += 100
      y_center = 0
      for j in range(0, 6):
        y_center += 100
        print "x center: " + str(x_center)
        create_rect(screen, [10, 10, 100, 100], black, (x_center, y_center), 1)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    pygame.display.update()
