import pygame
import random
import copy
from Piece import pieceSet
from Board import Board

pygame.init()

size=[300, 600]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("MLTetris")

done=False
clock=pygame.time.Clock()

board=Board()

pieceCount=0 #will loop between 0-6 and then reset
currentPieceSet=[]

while not done:
    if pieceCount==0:
        tempSet=[]
        for i in range(0, 7):
            tempSet.append(i)
        for i in range(1, len(tempSet)):
            val=random.randint(i, 6)
            temp=tempSet[i-1]
            tempSet[i-1]=tempSet[val]
            tempSet[val]=temp
        currentPieceSet=tempSet

    minScore=[0, 0]
    for i in range(0, 10):
        for j in range(0, len(pieceSet[currentPieceSet[pieceCount]].variants)):
            tempBoard=copy.deepcopy(board) #should be able to create a clone without any errors, if error copy array
            if tempBoard.drop(currentPieceSet[pieceCount], i, j):
                if minScore>tempBoard.calcScore:
                    minScore=[i, j]

    board.drop(currentPieceSet[pieceCount], minScore[0], minScore[1])

    pieceCount=(pieceCount+1)%7

    for i in range(0, len(board.tiles)):
        for j in range(0, len(board.tiles[i])):
            color=(0, 0, 0)
            if board.tiles[i][j]: color=(255, 255, 255)
            pygame.draw.rect(screen, color, [j*30, i*30, 30, 30])
    pygame.display.flip()
