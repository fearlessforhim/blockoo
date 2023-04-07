from .errors import PieceHasBeenPlacedError

class PlayerDTO:

    id = -1
    color = ""
    pieceSet = []
    isFinished = False

    def __init__(self, id, color, pieceSet, isFinished):
        self.id = id
        self.color = color
        self.pieceSet = pieceSet
        self.isFinished = isFinished

    def removePiece(self, pieceCode):
        for pieceObj in self.pieceSet:
            if pieceObj.id == pieceCode:
                self.pieceSet.remove(pieceObj)
                return pieceObj
        raise PieceHasBeenPlacedError(f"Player \"{self.color}\" does not have this piece in their pile: {pieceCode}")

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

    def setPlayerFinished(self):
        self.isFinished = True

    def calculateScore(self):
        rtv = 0
        for p in self.pieceSet:
            rtv = rtv - len(p.id)
        
        return rtv


