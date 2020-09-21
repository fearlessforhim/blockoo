import json

class Board:
    def __init__(self):
        self.initialize()

    def placePiece(self, sourceX, sourceY, rotationMod, isMirrored, piece, color):
        coords = piece.translate({'x': sourceX, 'y': sourceY}, rotationMod, isMirrored)
        try:
            self.isValid(coords, color)
            for c in coords:
                self.board[c['y']][c['x']] = {'color': color, 'y': c['x'], 'x': c['y']}

        except OutOfBoundsError:
            pass

    def isValid(self, coordinates, color):

        hasTouchingCorner = False

        for coordinate in coordinates:
            x = coordinate['x']
            y = coordinate['y']

            if x < 0 or x >= 20 or y < 0 or y >= 20:
                raise OutOfBoundsError('The piece travels out of bounds')
            elif self.board[y][x]['color'] != 'gray':
                raise OccupiedSquareError('The piece overlaps another')
            elif not self.isEdgesValid(x, y, color):
                raise SharedEdgeError('Edges are shared by the same color')

            if self.isTouchingCorner(x, y, color):
                hasTouchingCorner = True

        if not hasTouchingCorner:
            raise NotTouchingCornerError('Pieces must either be in the corner of the board or touch a corner of a like color')


    def initialize(self):
        self.board = []
        for j in range(0, 20):
            self.board.append([])
            for i in range(0, 20):
                self.board[j].append({'color': 'gray', 'x': j, 'y': i})

    def isEdgesValid(self, x, y, color):
        try:
            if self.board[y + 1][x]['color'] == color:
                return False
        except IndexError:
            pass
        try:
            if self.board[y][x + 1]['color'] == color:
                return False
        except IndexError:
            pass
        try:
            if self.board[y - 1][x]['color'] == color:
                return False
        except IndexError:
            pass
        try:
            if self.board[y][x - 1]['color'] == color:
                return False
        except IndexError:
            pass

        return True

    def isTouchingCorner(self, x, y, color):
        isTouchingCorner = False

        try:
            if self.board[y + 1][x + 1]['color'] == color:
                isTouchingCorner = True
        except IndexError:
            pass
        try:
            if self.board[y + 1][x - 1]['color'] == color:
                isTouchingCorner = True
        except IndexError:
            pass
        try:
            if self.board[y - 1][x + 1]['color'] == color:
                isTouchingCorner = True
        except IndexError:
            pass
        try:
            if self.board[y - 1][x - 1]['color'] == color:
                isTouchingCorner = True
        except IndexError:
            pass

        if (x == 0 and y == 0) or (x == 19 and y == 0) or (x == 0 and y == 19) or (x == 19 and y == 19):
            isTouchingCorner = True

        return isTouchingCorner

class BoardTranslator:

    def translateJson(self, jsonBoard):
        b = Board()
        for i in range(0, len(jsonBoard)):
            for j in range(0, len(jsonBoard)):
                b.board[i][j] = jsonBoard[i][j]
        return b

class Error(Exception):
    pass


class OutOfBoundsError(Error):
    def __init__(self, message):
        self.message = message


class OccupiedSquareError(Error):
    def __init__(self, message):
        self.message = message


class SharedEdgeError(Error):
    def __init__(self, message):
        self.message = message

class NotTouchingCornerError(Error):
    def __init__(self, message):
        self.message = message

class NotYourTurnError(Error):
    def __init__(self, message):
        self.message = message