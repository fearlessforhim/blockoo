from .shape import ShapeStructs as ss
from .piece import Piece

class Player:

    def __init__(self, color, pieceSet):
        self.color = color
        self.pieceSet = []
        for pieceInstructions in pieceSet:
            self.pieceSet.append(pieceInstructions)

    def removePiece(self, piece):
        for pieceObj in self.pieceSet:
            if pieceObj.id == piece.id:
                self.pieceSet.remove(pieceObj)

    def piecesAsString(self):
        toReturn = ''
        divider = ''
        for piece in self.pieceSet:
            toReturn += divider
            toReturn += piece.id
            divider = ','
        return toReturn

    def validatePlayerHasPiece(self, piece):
        playerHasPlayedPiece = True
        for myPiece in self.pieceSet:
            if piece.id == myPiece.id:
                playerHasPlayedPiece = False

        if playerHasPlayedPiece:
            raise PieceHasBeenPlacedError("This piece has been placed")

class Error(Exception):
    pass

class PieceHasBeenPlacedError(Error):
    def __init__(self, message):
        self.message = message