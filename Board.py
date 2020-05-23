import copy

import Piece

class Board:
    def __init__(self):
        self.tiles=[[False for i in range(10)] for j in range(20)]

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
        return True


    def calcScore(self):

        return