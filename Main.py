import pygame
import random
import copy
import Network
import numpy as np
from Piece import pieceSet
from Board import Board

pygame.init()

size=[300, 600]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("MLTetris")

done=False
clock=pygame.time.Clock()

board=Board()

sampleSize=20
sampleCycle=0

score=0
highScore=0

holdPiece=0

genNum=0
variantNum=0

net=Network.NeuralNetwork([4, 1])

pieceCount=0 #will loop between 0-6 and then reset
currentPieceSet=[]
dead=False

while not done:

    for i in range(0, 10):
        if board.tiles[0][i]:
            dead=True

    if dead:
        sampleCycle += 1
        if sampleCycle >= sampleSize:
            if score > highScore:
                highScore = score
                net.bestVals()
                genNum += 1
                variantNum = 0
                text = open("wb.txt", 'w')
                text.write(str(net.wb))
                text.close()
                print("New Generation")
            print("Generation:", genNum, "Variant:", variantNum, "High:", round(highScore*10)/10, "Last:", round(score*10)/10)
            net.nudge(10*np.power(1.1, variantNum/10000))
            variantNum+=1
            sampleCycle=0
            score=0
        score+=board.lines/sampleSize
        board.__init__()
        dead=False

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

    minScore=999999999 #will set it to the first board regardless
    bestParams=[0, 0]
    for k in range(0, 2):
        if k==0:
            piece=currentPieceSet[pieceCount]
        else:
            piece=holdPiece
        for i in range(0, 10):
            for j in range(0, len(pieceSet[piece].variants)):
                tempBoard=copy.deepcopy(board) #should be able to create a clone without any errors, if error copy array
                if tempBoard.drop(piece, i, j):
                    boardScore=net.func(tempBoard.calcScore())[0]
                    if minScore>boardScore:
                        minScore=boardScore
                        bestParams=[i, j, k]

    board.drop(currentPieceSet[pieceCount] if bestParams[2]==0 else holdPiece, bestParams[0], bestParams[1])
    if bestParams[2]==1:
        holdPiece=currentPieceSet[pieceCount]

    pieceCount=(pieceCount+1)%7

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            for i in range(0, len(board.tiles)):
                for j in range(0, len(board.tiles[i])):
                    color=(0, 0, 0)
                    if board.tiles[i][j]: color=(255, 255, 255)
                    pygame.draw.rect(screen, color, [j*30, i*30, 30, 30])
            clock.tick(15)

    pygame.display.flip()
