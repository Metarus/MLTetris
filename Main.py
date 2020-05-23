import pygame
from Board import Board

pygame.init()

size=[300, 600]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("MLTetris")

done=False
clock=pygame.time.Clock()

board=Board()

while not done:
    for i in range(0, len(board.tiles)):
        for j in range(0, len(board.tiles[i])):
            color=(0, 0, 0)
            if board.tiles[i][j]: color=(255, 255, 255)
            pygame.draw.rect(screen, color, [j*30, i*30, 30, 30])
    pygame.display.flip()
