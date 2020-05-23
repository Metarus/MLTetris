import copy
import Piece
import numpy as np

class Board:
    def __init__(self):
        self.tileColors=[[(0, 0, 0) for i in range(10)] for j in range(20)]
        self.tiles=[[False for i in range(10)] for j in range(20)]
        self.lines=0

    def drop(self, piece, horizontal, rotation):
        tempTiles=copy.deepcopy(Piece.pieceSet[piece].variants[rotation])
        for i in range(0, 4):
            tempTiles[i][1]+=horizontal
            if tempTiles[i][1]>=10:
                return False
        falling=True
        while falling:
            for i in range(0, 4):
                if tempTiles[i][0]==19:
                    falling=False
                elif self.tiles[tempTiles[i][0]+1][tempTiles[i][1]]:
                    falling=False
            if falling:
                for i in range(0, 4):
                    tempTiles[i][0]+=1
        for i in range(0, 4):
            self.tiles[tempTiles[i][0]][tempTiles[i][1]]=True
            self.tileColors[tempTiles[i][0]][tempTiles[i][1]]=Piece.pieceSet[piece].color
        for i in range(0, len(self.tiles)):
            fullLine=True
            for j in range(0, 10):
                if not self.tiles[i][j]:
                    fullLine=False
                    break
            if fullLine:
                for j in range(i, 0, -1):
                    self.tiles[j]=copy.deepcopy(self.tiles[j-1])
                    self.tileColors[j]=copy.deepcopy(self.tileColors[j-1])
                self.lines+=1
        return True


    def calcScore(self):
        highestTiles=[]
        for i in range(0, len(self.tiles[0])):
            found=False
            height=0
            while not found:
                if self.tiles[height][i]:
                    found=True
                    highestTiles.append(height)
                elif height==19:
                    found=True
                    highestTiles.append(20)
                else:
                    height+=1

        lowestHole=[]
        for i in range(0, len(self.tiles[0])):
            found=False
            height=19
            while not found:
                if not self.tiles[height][i]:
                    found=True
                    lowestHole.append(height)
                elif height==0:
                    found=True
                    lowestHole.append(-1)
                else:
                    height-=1

        netInputs=[0, 0, 0, 0]
        for i in range(0, len(highestTiles)-1):
            netInputs[0]+=np.power(highestTiles[i]-highestTiles[i+1], 2)

        for i in range(0, len(highestTiles)):
            netInputs[1]+=lowestHole[i]-highestTiles[i]+1

        highest=0
        for i in range(1, len(highestTiles)):
            if highestTiles[highest]<highestTiles[i]:
                highest=i
        netInputs[2]=20-highestTiles[highest]

        parityBlocks=[0, 0]
        for i in range(0, len(self.tiles)):
            for j in range(0, len(self.tiles[i])):
                if self.tiles[i][j]:
                    parityBlocks[(i+j)%2]+=1
        netInputs[3]=np.abs(parityBlocks[0]-parityBlocks[1])
        return netInputs
