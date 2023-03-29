from moveType import M0, M1, M2, M3, M4, M5, M6, M7, M8
class Piece:

    id = ""

    def __init__(self, pieceInstructions):
        self.movements = []
        self.id = pieceInstructions
        for struct in self.id:
            if struct == '0':
                self.movements.append(M0)
            elif struct == '1':
                self.movements.append(M1)
            elif struct == '2':
                self.movements.append(M2)
            elif struct == '3':
                self.movements.append(M3)
            elif struct == '4':
                self.movements.append(M4)
            elif struct == '5':
                self.movements.append(M5)
            elif struct == '6':
                self.movements.append(M6)
            elif struct == '7':
                self.movements.append(M7)

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

