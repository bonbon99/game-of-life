import random
import pygame
import sys

pygame.init()

def determine_living_neighbors(board, cell): # [x, y]
    living = 0
    x, y = cell
    global BOARD_LENGTH

    if board[(x - 1) % BOARD_LENGTH][y] == 1: # mid left
        living += 1
    if board[(x + 1) % BOARD_LENGTH][y] == 1: # mid right
        living += 1
    if board[(x - 1) % BOARD_LENGTH][(y - 1) % BOARD_LENGTH] == 1: # top left
        living += 1
    if board[x][(y - 1) % BOARD_LENGTH] == 1: # top mid
        living += 1
    if board[(x + 1) % BOARD_LENGTH][(y - 1) % BOARD_LENGTH] == 1: # top right
        living += 1   
    if board[(x - 1) % BOARD_LENGTH][(y + 1) % BOARD_LENGTH] == 1: # bottom left
        living += 1
    if board[x][(y + 1) % 50] == 1: # bottom mid
        living += 1
    if board[(x + 1) % BOARD_LENGTH][(y + 1) % BOARD_LENGTH] == 1: # bottom right
        living += 1
    
    return living

def update_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            living_neighbors = determine_living_neighbors(board, [i, j])
            current = board[i][j]
            if current == 0 and living_neighbors == 3:
                board[i][j] = 1
            elif current == 1 and (living_neighbors <= 1 or living_neighbors > 3):
                board[i][j] = 0

def draw_board(board, screen):
    global BOARD_LENGTH
    global black, white
    
    screen.fill(white)
    for i in range(BOARD_LENGTH):
        for j in range(BOARD_LENGTH):
            pygame.draw.rect(screen, black, (i * 10 + 50, j * 10 + 50, 10, 10), 1)
            if board[i][j] == 1:
                pygame.draw.rect(screen, black, (i * 10 + 50, j * 10 + 50, 10, 10), 0)

BOARD_LENGTH = 50
board = []
ALIVE_CHANCE = 0.05

black = (0, 0, 0)
white = (255, 255, 255)
screen = pygame.display.set_mode((600, 600))
screen.fill(white)

for i in range(BOARD_LENGTH):
    board.append([])
    for j in range(BOARD_LENGTH):
        state = random.randint(1, 1 / ALIVE_CHANCE)
        if state == 1:
            board[i].append(1)
        else:
            board[i].append(0)

for i in range(10000):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit()

    draw_board(board, screen)
    update_board(board)

    pygame.time.delay(500)
    pygame.display.update()
