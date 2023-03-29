#coordinate movements are coded for (0,0) being in the top left corner and max (x,y)
# in the bottom right (web page layout)
#M[x] classes are organized around a compass, M1 is north and numbers increase every 45 degrees
# going clockwise

#starting point of all pieces
class M0:
    x = 0
    y = 0

#construct piece North
class M1:
    x = 0
    y = -1

#construct piece NE
class M2:
    x = 1
    y = -1

#construct piece E
class M3:
    x = 1
    y = 0

#construct piece SE
class M4:
    x = 1
    y = 1

#construct piece S
class M5:
    x = 0
    y = 1

#construct piece SW
class M6:
    x = -1
    y = 1

#construct piece W
class M7:
    x = -1
    y = 0

#construct piece NW
class M8:
    x = -1
    y = -1