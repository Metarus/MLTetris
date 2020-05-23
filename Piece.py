class Piece:
    def __init__(self, color, variants):
        self.color=color
        self.variants=variants

pieceSet=[
    #O piece
    Piece((245, 242, 66), [
        [[0, 0], [1, 0], [0, 1], [1, 1]]
    ]),
    #I piece
    Piece((133, 255, 237), [
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 0], [2, 0], [3, 0]]
    ]),
    #Z piece
    Piece((255, 0, 0), [
        [[0, 0], [0, 1], [1, 1], [1, 2]],
        [[0, 1], [1, 1], [1, 0], [2, 0]]
    ]),
    #S piece
    Piece((0, 255, 0), [
        [[1, 0], [1, 1], [0, 1], [0, 2]],
        [[0, 0], [1, 0], [1, 1], [2, 1]]
    ]),
    #T piece
    Piece((255, 0, 255), [
        [[0, 1], [1, 0], [1, 1], [1, 2]],
        [[0, 0], [1, 0], [2, 0], [1, 1]],
        [[0, 0], [0, 1], [0, 2], [1, 1]],
        [[0, 1], [1, 1], [2, 1], [1, 0]]
    ]),
    #L piece
    Piece((255, 128, 0), [
        [[1, 0], [1, 1], [1, 2], [0, 2]],
        [[0, 0], [1, 0], [2, 0], [2, 1]],
        [[1, 0], [0, 0], [0, 1], [0, 2]],
        [[0, 0], [0, 1], [1, 1], [2, 1]]
    ]),
    #J piece
    Piece((0, 0, 255), [
        [[0, 0], [1, 0], [1, 1], [1, 2]],
        [[0, 1], [0, 0], [1, 0], [2, 0]],
        [[0, 0], [0, 1], [0, 2], [1, 2]],
        [[0, 1], [1, 1], [2, 1], [2, 0]]
    ])
]
