from .moveType import N, E, S
class Piece:
    def __init__(self, pieceInstructions):
        self.movements = []
        self.id = pieceInstructions
        for struct in self.id:
            if struct == 'E':
                self.movements.append(E)
            elif struct == 'N':
                self.movements.append(N)
            elif struct == 'S':
                self.movements.append(S)

    def translate(self, start, rotationMod, isMirrored):
        usedCoordinates = []
        x = start['x']
        y = start['y']
        usedCoordinates.append({'x': x, 'y' : y})
        for movement in self.movements:
            preX = movement.x
            preY = movement.y

            if rotationMod == 3:
                preX = preX * -1
                intermediary = preX
                preX = preY
                preY = intermediary
            elif rotationMod == 2:
                preX = preX * -1
                preY = preY * -1
            elif rotationMod == 1:
                preY = preY * -1
                intermediary = preX
                preX = preY
                preY = intermediary

            if isMirrored:
                preX = preX * -1

            x += preX
            y += preY
            usedCoordinates.append({'x': x, 'y' : y})
        return usedCoordinates

