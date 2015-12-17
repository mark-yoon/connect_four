from ai import *
from human import *
from board import *
import pygame


# Constant definitions =========================================================
# Color definitions
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Game state enum types
MENU = 0
SUBMENU = 1
HUMAN_AI = 2
AI_AI = 3


# Heuristic enum types
RANDOM = 1
MINIMAX = 2


# Function definitions =========================================================
# Initialize the game variables
def init():
  global player2
  global board
  global turn
  global invalid_move
  global victory
  global player1_locs
  global player2_locs

  player2 = AI(2, False, 3, MINIMAX)
  board = Board()
  turn = 1
  victory = 0
  player1_locs = []
  player2_locs = []
  invalid_move = False

# Function to create a text string in the game
def create_text(screen, font_path, size, text, color, center):
  font = pygame.font.Font(font_path, size)
  text = font.render(text, 0, color)
  textpos = text.get_rect()
  textpos.centerx = center[0]
  textpos.centery = center[1]
  screen.blit(text, textpos)

# Function to create a rectangle in the game
def create_rect(screen, rect, color, center, thickness):
  rectangle = pygame.Rect(rect)
  rectangle.center = center
  pygame.draw.rect(screen, color, rectangle, thickness)
  return rectangle

def main_menu():
  center = screen.get_rect().center

  play_rect = create_rect(screen, [10, 10, 200, 80], black, (400, 450), 1)
  watch_rect = create_rect(screen, [20, 10, 200, 80], black, (400, 550), 1)

  create_text(screen, "font/mario.ttf", 25, "PLAY", black, center)
  create_text(screen, "font/mario.ttf", 25, "WATCH", black, (center[0], center[1]+100))
  create_text(screen, "font/mario.ttf", 45, "Welcome to Connect 4!", black, (screen.get_rect().centerx, screen.get_rect().centery -200))

  return (play_rect, watch_rect)

def draw_game_boxes(x_center, y_center):
  game_rects = []
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
      else:
        col.append(create_rect(screen, [10, 10, 100, 100], black, (x_center, y_center), 1))
    game_rects.append(col)
  return game_rects

def draw_game_text(victory, turn, invalid_move):
  if invalid_move:
    if turn == 1:
      create_text(screen, "font/mario.ttf", 25, "Your turn!", black, (400, 100))
    else:
      create_text(screen, "font/mario.ttf", 25, "AI's turn!", black, (400, 100))
    create_text(screen, "font/mario.ttf", 25, "Invalid move!", black, (400, 175))
    create_text(screen, "font/mario.ttf", 25, "Human: " + str(human), black, (115 , 230))
    create_text(screen, "font/mario.ttf", 25, "AI: " + str(ai), black, (700 , 230))
  elif victory != 0:
    create_text(screen, "font/mario.ttf", 25, "Try again?", black, (400, 175))
    try_again = create_rect(screen, [10, 10, 200, 50], black, (400, 175), 1)
    if victory == 1:
      create_text(screen, "font/mario.ttf", 40, "You won!!", black, (400, 100))
    else:
        create_text(screen, "font/mario.ttf", 40, "You lost...", black, (400, 100))
    create_text(screen, "font/mario.ttf", 25, "Human: " + str(human), black, (115 , 230))
    create_text(screen, "font/mario.ttf", 25, "AI: " + str(ai), black, (700 , 230))
    return try_again
  else:
    if turn == 1:
      create_text(screen, "font/mario.ttf", 25, "Your turn!", black, (400, 100))
    else:
      create_text(screen, "font/mario.ttf", 25, "AI's turn!", black, (400, 100))
    create_text(screen, "font/mario.ttf", 25, "Human: " + str(human), black, (115 , 230))
    create_text(screen, "font/mario.ttf", 25, "AI: " + str(ai), black, (700 , 230))

# Main =========================================================================

# Initialize the game screen
pygame.init()
size = (800,900)
screen = pygame.display.set_mode(size)
screen.fill(white)
pygame.display.set_caption("Connect 4")
running = True
game_state = 0

# Initialize the game states
init()
human = 0
ai = 0

while running:
  screen.fill(white)
  # Main menu screen
  if game_state == MENU:
    buttons = main_menu()
    play_rect = buttons[0]
    watch_rect = buttons[1]
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if play_rect.collidepoint(event.pos):
          game_state = HUMAN_AI
        elif watch_rect.collidepoint(event.pos):
          game_state = SUBMENU
      pygame.display.update()

  # Play submenu screen
  elif game_state == SUBMENU:
    print 'hi'

  # Play game scene
  elif game_state == HUMAN_AI:
    game_rects = draw_game_boxes(0, 900)
    try_again = draw_game_text(victory, turn, invalid_move)
    pygame.display.update()

    if turn == 1:
      # Human turn
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          # If player has won, if user clicks try again, reinitialize game
          if victory:
            if try_again.collidepoint(event.pos):
              init()
          else:
            # Check which column was clicked
            for col in range(0, len(game_rects)):
              for rect in game_rects[col]:
                if rect.collidepoint(event.pos):
                  # Add player move to board
                  add = board.add(col, 1)
                  # If valid move, append location
                  if add[0]:
                    invalid_move = False
                    player1_locs.append((add[1], add[2]))
                    # If win, mark victory as true, change turn otherwise
                    if board.check_win(turn)[0]:
                      victory = turn
                      human += 1
                    else:
                      turn = 2
                  else:
                    invalid_move = True

    elif turn == 2:
      # Bot turn
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      col = player2.next_move(board)
      print board
      add = board.add(col, 2)
      if add[0]:
        invalid_move = False
        player2_locs.append((add[1], add[2]))
        if board.check_win(turn)[0]:
          victory = turn
          ai += 1
          turn = 1
        else:
          turn = 1

    pygame.display.update()
