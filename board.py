
class Board(object):
  """
  Board object that holds the board state
  Connect 4 rules state a 6 x 7 board, but can be expansible
  """

  cells = None
  player1_locs = None
  player2_locs = None
  x_max = None
  y_max = None

  def __init__(self, x = 7, y = 6):
    self.x_max = x
    self.y_max = y
    self.cells = [[0 for i in range(self.x_max)] for j in range(self.y_max)]
    self.player1_locs = []
    self.player2_locs = []

  def __str__(self):
    print " 0 1 2 3 4 5 6 "
    for row in reversed(self.cells):
      output = ''
      for cell in row:
        output += '|'
        if cell == 0:
          output += ' '
        elif cell == 1:
          output += 'O'
        elif cell == 2:
          output += 'X'
      output += '|'
      print output
    print "---------------"
    print " 0 1 2 3 4 5 6 "
    return ""

  def check_win(self, player):
    if player == 1:
      nodes = self.player1_locs
    else:
      nodes = self.player2_locs

    for node in nodes:
      x = node[0]
      y = node[1]

      if (x, y + 1) in nodes and (x, y + 2) in nodes and (x, y + 3) in nodes:
        return (True, player, [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)])

      if (x, y - 1) in nodes and (x, y - 2) in nodes and (x, y - 3) in nodes:
        return (True, player, [(x, y), (x, y - 1), (x, y - 2), (x, y - 3)])

      if (x + 1, y) in nodes and (x + 2, y) in nodes and (x + 3, y) in nodes:
        return (True, player, [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)])

      if (x - 1, y) in nodes and (x - 2, y) in nodes and (x - 3, y) in nodes:
        return (True, player, [(x, y), (x - 1, y), (x - 2, y), (x - 3, y)])

      if (x + 1, y + 1) in nodes and (x + 2, y + 2) in nodes and (x + 3, y + 3) in nodes:
        return (True, player, [(x, y), (x + 1, y + 1), (x + 2, y + 2), (x + 3, y + 3)])

      if (x - 1, y + 1) in nodes and (x - 2, y + 2) in nodes and (x - 3, y + 3) in nodes:
        return (True, player, [(x, y), (x - 1, y + 1), (x - 2, y + 2), (x - 3, y + 3)])

      if (x - 1, y - 1) in nodes and (x - 2, y - 2) in nodes and (x - 3, y - 3) in nodes:
        return (True, player, [(x, y), (x - 1, y - 1), (x - 2, y - 2), (x - 3, y - 3)])

      if (x + 1, y - 1) in nodes and (x + 2, y - 2) in nodes and (x + 3, y - 3) in nodes:
        return (True, player, [(x, y), (x + 1, y - 1), (x + 2, y - 2), (x + 3, y - 3)])

    return (False, player, [])

# IMPORTANT NEED TO COUNT DISJOINT SETS

  # def get_connected(self, player):
  #   if player == 1:
  #     my_nodes = self.player1_locs
  #     opp_nodes = self.player2_locs
  #   else:
  #     my_nodes = self.player2_locs
  #     opp_nodes = self.player1_locs

  #   twos = 0
  #   threes = 0
  #   fours = 0

  #   for node in my_nodes:
  #     x = node[0]
  #     y = node[1]

  #     if (x, y + 1) in my_nodes and (x, y + 2) in my_nodes and (x, y + 3) in my_nodes:
  #       fours += 1

  #     if (x + 1, y) in my_nodes and (x + 2, y) in my_nodes and (x + 3, y) in my_nodes:
  #       fours += 1

  #     if (x + 1, y + 1) in my_nodes and (x + 2, y + 2) in my_nodes and (x + 3, y + 3) in my_nodes:
  #       fours += 1

  #     if (x - 1, y + 1) in my_nodes and (x - 2, y + 2) in my_nodes and (x - 3, y + 3) in my_nodes:
  #       fours += 1

  #     # Three node connected components
  #     if (x, y + 1) in my_nodes and (x, y + 2) in my_nodes and (x, y + 3) not in my_nodes and (x, y - 1) not in my_nodes:
  #       threes += 1

  #     if (x + 1, y) in my_nodes and (x + 2, y) in my_nodes and (x + 3, y) not in my_nodes and (x - 1, y) not in my_nodes:
  #       threes += 1

  #     if (x + 1, y + 1) in my_nodes and (x + 2, y + 2) in my_nodes and (x + 3, y + 3) not in my_nodes and (x - 1, y - 1) not in my_nodes:
  #       threes += 1

  #     if (x - 1, y + 1) in my_nodes and (x - 2, y + 2) in my_nodes and (x - 3, y + 3) not in my_nodes and (x + 1, y - 1) not in my_nodes:
  #       threes += 1

  #     if (x, y + 1) in my_nodes and (x, y + 2) not in my_nodes and (x, y - 1) not in my_nodes:
  #       twos += 1

  #     # Two node connected components
  #     if (x + 1, y) in my_nodes and (x + 2, y) not in my_nodes and (x - 1, y) not in my_nodes:
  #       twos += 1

  #     if (x + 1, y + 1) in my_nodes and (x + 2, y + 2) not in my_nodes and (x - 1, y - 1) not in my_nodes:
  #       twos += 1

  #     if (x - 1, y + 1) in my_nodes and (x - 2, y + 2) not in my_nodes and (x + 1, y - 1) not in my_nodes:
  #       twos += 1

  #   return (fours, threes, twos)


  def get_connected(self, player):
    if player == 1:
      my_nodes = self.player1_locs
      opp_nodes = self.player2_locs
    else:
      my_nodes = self.player2_locs
      opp_nodes = self.player1_locs

    all_nodes = my_nodes+opp_nodes

    twos = 0
    threes = 0
    fours = 0

    for node in my_nodes:
      x = node[0]
      y = node[1]

      if (x, y+1) in my_nodes and (x, y+2) in my_nodes and (x, y+3) in my_nodes:
        fours += 1

      if (x+1, y) in my_nodes and (x+2, y) in my_nodes and (x+3, y) in my_nodes:
        fours += 1

      if (x+1, y+1) in my_nodes and (x+2, y+2) in my_nodes and (x+3, y+3) in my_nodes:
        fours += 1

      if (x+1, y-1) in my_nodes and (x+2, y-2) in my_nodes and (x+3, y-3) in my_nodes:
        fours += 1

      # Three node connected components
      if (x, y+1) in my_nodes and (x, y+2) in my_nodes and (x, y+3) not in my_nodes and (x, y-1) not in my_nodes and self.valid((x, y+3), (x, y-1), opp_nodes):
        threes += 1

      if (x+1, y) in my_nodes and (x+2, y) in my_nodes and (x+3, y) not in my_nodes and (x-1, y) not in my_nodes and self.valid((x+3, y), (x-1, y), opp_nodes):
        threes += 1

      if (x+1, y+1) in my_nodes and (x+2, y+2) in my_nodes and (x+3, y+3) not in my_nodes and (x-1, y-1) not in my_nodes and self.valid((x+3, y+3), (x-1, y-1), opp_nodes):
        threes += 1

      if (x+1, y-1) in my_nodes and (x+2, y-2) in my_nodes and (x+3, y-3) not in my_nodes and (x-1, y+1) not in my_nodes and self.valid((x+3, y-3), (x-1, y+1), opp_nodes):
        threes += 1

      # Disjointed connected components
      if (x, y+2) in my_nodes and (x, y+3) in my_nodes and (x, y+4) not in my_nodes:
        threes += 1
      if (x, y+1) in my_nodes and (x, y+3) in my_nodes and (x, y-1) not in my_nodes:
        threes += 1
      if (x+2, y) in my_nodes and (x+3, y) in my_nodes and (x+4, y) not in my_nodes:
        threes += 1
      if (x+1, y) in my_nodes and (x+3, y) in my_nodes  and (x-1, y) not in my_nodes:
        threes += 1
      if (x+2, y+2) in my_nodes and (x+3, y+3) in my_nodes and (x+4, y+4) not in my_nodes:
        threes += 1
      if (x+1, y+1) in my_nodes and (x+3, y+3) in my_nodes and (x-1, y-1) not in my_nodes:
        threes += 1
      if (x+2, y-2) in my_nodes and (x+3, y-3) in my_nodes and (x+4, y-4) not in my_nodes:
        threes += 1
      if (x+1, y-1) in my_nodes and (x+3, y-3) in my_nodes and (x-1, y+1) not in my_nodes:
        threes += 1

      # Two node connected components
      if (x, y+1) in my_nodes and (x, y+2) not in my_nodes and (x, y-1) not in my_nodes and self.valid((x, y+2), (x, y-1), opp_nodes):
        twos += 1

      if (x+1, y) in my_nodes and (x+2, y) not in my_nodes and (x-1, y) not in my_nodes and self.valid((x+2, y), (x-1, y), opp_nodes):
        twos += 1

      if (x+1, y+1) in my_nodes and (x+2, y+2) not in my_nodes and (x-1, y-1) not in my_nodes and self.valid((x+2, y+2), (x-1, y-1), opp_nodes):
        twos += 1

      if (x+1, y-1) in my_nodes and (x+2, y-2) not in my_nodes and (x-1, y+1) not in my_nodes and self.valid((x+2, y-2), (x-1, y+1), opp_nodes):
        twos += 1

      # Disjointed connected components
      if (x, y+2) in my_nodes and (x, y+1) not in all_nodes and (x, y+3) not in my_nodes and (x, y-1) not in my_nodes and self.valid((x, y+3), (x, y-1), opp_nodes):
        twos += 1

      if (x+2, y) in my_nodes and (x+1, y) not in all_nodes and (x+3, y) not in my_nodes and (x-1, y) not in my_nodes and self.valid((x+3, y), (x-1, y), opp_nodes):
        twos += 1

      if (x+2, y+2) in my_nodes and (x+1, y+1) not in all_nodes and (x+3, y+3) not in my_nodes and (x-1, y-1) not in my_nodes and self.valid((x+3, y+3), (x-1, y-1), opp_nodes):
        twos += 1

      if (x+2, y-2) in my_nodes and (x+1, y-1) not in all_nodes and (x+3, y-3) not in my_nodes and (x-1, y+1) not in my_nodes and self.valid((x+3, y-3), (x-1, y+1), opp_nodes):
        twos += 1

    return (fours, threes, twos)

  def valid(self, endp_1, endp_2, opp_nodes):
    # Check if in-bounds
    if self.inbound(endp_1) and self.inbound(endp_2):
      return (endp_1 not in opp_nodes or endp_2 not in opp_nodes)
    elif self.inbound(endp_1):
      return (endp_2 not in opp_nodes)
    elif self.inbound(endp_2):
      return (endp_1 not in opp_nodes)
    else:
      return False

  def inbound(self, endp):
    if endp[0] >= 0 and endp[0] <= 6 and endp[1] >= 0 and endp[1] <= 5:
      return True
    else:
      return False

  def valid_moves(self):
    moves = []
    for x in range(self.x_max):
      if self.cells[self.y_max - 1][x] == 0:
        moves.append(x)
    return moves

  def add(self, x, player):
    for y in range(self.y_max):
      if self.cells[y][x] == 0:
        self.cells[y][x] = player
        if player == 1:
          self.player1_locs.append((x, y))
        else:
          self.player2_locs.append((x, y))
        return (True, x, y)
    return (False, -1, -1)
