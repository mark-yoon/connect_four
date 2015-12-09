import pygame

white = (255,255,255)
black = (0,0,0)

pygame.init()
size = (800,600)
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

while running: 
  screen.fill(white)
  if game_state == 0:
    play_rect = pygame.Rect([10, 10, 200, 100])
    play_rect.center = (400, 300)
    pygame.draw.rect(screen, black, play_rect, 1)

    create_text(screen, "font/mario.ttf", 25, "PLAY", black, screen.get_rect().center)
    create_text(screen, "font/mario.ttf", 45, "Welcome to Connect 4!", black, (screen.get_rect().centerx, screen.get_rect().centery -200))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if play_rect.collidepoint(event.pos):
          print "Test"
          game_state = 1
      pygame.display.update()


  if game_state == 1:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    pygame.display.update()