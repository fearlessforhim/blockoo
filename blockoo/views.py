from django.shortcuts import render
from django.http import JsonResponse
from django.conf.urls import url
from .player import Player
from .piece import Piece
from .models.PieceModel import PieceModel
from .models.PlayerModel import PlayerModel
from .models.BoardModel import BoardModel
from .board import Board, BoardTranslator, OutOfBoundsError, OccupiedSquareError, SharedEdgeError, NotYourTurnError
from .boardCoordinate import BoardCoordinate
from .shape import ShapeStructs as ss
from .color import Color
import json

def buildInitialState(request):

    PieceModel.objects.all().delete()
    PlayerModel.objects.all().delete()
    BoardModel.objects.all().delete()

    pieces = [
        '',
        'E',
        'EE',
        'EEN',
        'EEE',
        'ENS',
        'NENE',
        'EN',
        'NSN',
        'NEN',
        'ENNE',
        'EEEE',
        'NSEE',
        'NENN',
        'NSNN',
        'NSEN',
        'ENNS',
        'ENSE',
        'EENN',
        'NNSE',
        'SNNS'
    ]

    for p in pieces:
        p = PieceModel(key=p)
        p.save()

    pl1 = PlayerModel(color=Color.R.value, remainingPieces = ",".join(pieces))
    pl1.save()
    pl2 = PlayerModel(color=Color.G.value, remainingPieces = ",".join(pieces))
    pl2.save()
    pl3 = PlayerModel(color=Color.B.value, remainingPieces = ",".join(pieces))
    pl3.save()
    pl4 = PlayerModel(color=Color.Y.value, remainingPieces = ",".join(pieces))
    pl4.save()

    board = []
    for j in range(0, 20):
        board.append([])
        for i in range(0, 20):
            board[j].append({'color': 'gray', 'x': j, 'y': i})

    bm = BoardModel(boardState=json.dumps(board), currentPlayer=0)
    bm.save()

    return JsonResponse({'message': 'Success'}, safe=True)

def getPlayerOrder():
    return [
        'red',
        'blue',
        'yellow',
        'green'
    ]

def index(request):
    players = []

    pieces = [
        Piece(''),
        Piece('E'),
        Piece('EE'),
        Piece('EEN'),
        Piece('EEE'),
        Piece('ENS'),
        Piece('NENE'),
        Piece('EN'),
        Piece('NSN'),
        Piece('NEN'),
        Piece('ENNE'),
        Piece('EEEE'),
        Piece('NSEE'),
        Piece('NENN'),
        Piece('NSNN'),
        Piece('NSEN'),
        Piece('ENNS'),
        Piece('ENSE'),
        Piece('EENN'),
        Piece('NNSE'),
        Piece('SNNS'),
    ]

    players.append(Player('red', pieces))
    players.append(Player('yellow', pieces))
    players.append(Player('blue', pieces))
    players.append(Player('green', pieces))

    return render(request, 'index.html')

def getState(request):
    return JsonResponse(getBoardAsJSON(), safe=False)

def getCurrentPlayerAsJSON():
    board = BoardModel.objects.all().first()
    return board.currentPlayer

def getBoardAsJSON():
    board = BoardModel.objects.all().first()
    boardState = json.loads(board.boardState)
    return boardState

def getPlayerArray():
    players =  PlayerModel.objects.all()
    playerObjs = []
    for player in players:
        playerObj = dict(
            color = player.color,
            remainingPieces = player.remainingPieces,
        )
        playerObjs.append(playerObj)

    return playerObjs

def getPlayers(request):
    players =  PlayerModel.objects.all()
    response = {
        'playerArray': getPlayerArray(),
        'currentPlayer': getCurrentPlayerAsJSON()
    }
    return JsonResponse(response, safe=True)

def passPlayer(request):
    currentPlayer = getCurrentPlayerAsJSON()
    boardModel = BoardModel.objects.all().first()

    if currentPlayer == 3:
        boardModel.currentPlayer = 0
    else:
        boardModel.currentPlayer = currentPlayer + 1

    boardModel.save()
    return JsonResponse({'message': 'Success'}, safe=True)

def handlePost(request):
    body = json.loads(request.body)

    translator = BoardTranslator()
    board = translator.translateJson(getBoardAsJSON())
    currentPlayer = getCurrentPlayerAsJSON()

    xCoord = body["xCoord"]
    yCoord = body["yCoord"]

    color = body["color"]
    piece = body["piece"]

    if color != getPlayerOrder()[currentPlayer]:
        return JsonResponse({'message': 'It is ' + getPlayerOrder()[currentPlayer] + '\'s turn'}, safe=True)

    rotationModifier = body["rotationModifier"]
    isMirrored = body["isMirrored"]
    pieceSet = []
    for playerArray in getPlayerArray():
        if playerArray['color'] == color:
            pieceList = playerArray['remainingPieces'].split(',')
            for pieceInstruction in pieceList:
                pieceSet.append(Piece(pieceInstruction))
    player = Player(color, pieceSet)

    try:
        placedPiece = Piece(piece)

        player.validatePlayerHasPiece(placedPiece)

        board.placePiece(xCoord, yCoord, rotationModifier, isMirrored, placedPiece, color)

        player.removePiece(placedPiece)
        boardModel = BoardModel.objects.all().first()
        boardModel.boardState = json.dumps(board.board)
        if currentPlayer == 3:
            boardModel.currentPlayer = 0
        else:
            boardModel.currentPlayer = currentPlayer + 1

        boardModel.save()
        currentPlayerModel = PlayerModel.objects.filter(color=color).first()
        currentPlayerModel.remainingPieces = player.piecesAsString()
        currentPlayerModel.save()

    except Exception as e:
        return JsonResponse({'message': str(e)}, safe=True)

    return JsonResponse(getBoardAsJSON(), safe=False)

def tests(request):
    p = Piece('')
    coords = p.translate({'x': 0, 'y': 0}, 0, False)
    assert len(coords) == 1
    assert len(coords[0]) == 2
    assert coords[0]['x'] == 0
    assert coords[0]['y'] == 0
    print('passed basic')

    p = Piece('E')
    coords = p.translate({'x': 0, 'y': 0}, 0, False)
    assert len(coords) == 2
    assert coords[0]['x'] == 0
    assert coords[0]['y'] == 0
    assert coords[1]['x'] == 1
    assert coords[1]['y'] == 0
    print('passed single')

    p = Piece('ENS')
    coords = p.translate({'x': 0, 'y': 0}, 0, False)
    assert len(coords) == 4
    assert coords[0]['x'] == 0
    assert coords[0]['y'] == 0
    assert coords[1]['x'] == 1
    assert coords[1]['y'] == 0
    assert coords[2]['x'] == 1
    assert coords[2]['y'] == -1
    assert coords[3]['x'] == 2
    assert coords[3]['y'] == 0
    print('passed combo of all')

    p = Piece('ENS')
    coords = p.translate({'x': 0, 'y': 0}, 1, False)
    assert len(coords) == 4
    assert coords[0]['x'] == 0
    assert coords[0]['y'] == 0
    assert coords[1]['x'] == 0
    assert coords[1]['y'] == 1
    assert coords[2]['x'] == 1
    assert coords[2]['y'] == 1
    assert coords[3]['x'] == 0
    assert coords[3]['y'] == 2
    print('passed rotate 1')

    p = Piece('ENS')
    coords = p.translate({'x': 0, 'y': 0}, 2, False)
    assert len(coords) == 4
    assert coords[0]['x'] == 0
    assert coords[0]['y'] == 0
    assert coords[1]['x'] == -1
    assert coords[1]['y'] == 0
    assert coords[2]['x'] == -1
    assert coords[2]['y'] == 1
    assert coords[3]['x'] == -2
    assert coords[3]['y'] == 0
    print('passed rotate 2')

    p = Piece('ENS')
    coords = p.translate({'x': 0, 'y': 0}, 3, False)
    assert len(coords) == 4
    assert coords[0]['x'] == 0
    assert coords[0]['y'] == 0
    assert coords[1]['x'] == 0
    assert coords[1]['y'] == -1
    assert coords[2]['x'] == -1
    assert coords[2]['y'] == -1
    assert coords[3]['x'] == 0
    assert coords[3]['y'] == -2
    print('passed rotate 3')

    p = Piece('ENS')
    coords = p.translate({'x': 0, 'y': 0}, 0, True)
    assert len(coords) == 4
    assert coords[0]['x'] == 0
    assert coords[0]['y'] == 0
    assert coords[1]['x'] == -1
    assert coords[1]['y'] == 0
    assert coords[2]['x'] == -1
    assert coords[2]['y'] == -1
    assert coords[3]['x'] == -2
    assert coords[3]['y'] == 0
    print('passed mirrored')

    p = Piece('ENS')
    coords = p.translate({'x': 0, 'y': 0}, 1, True)
    assert len(coords) == 4
    assert coords[0]['x'] == 0
    assert coords[0]['y'] == 0
    assert coords[1]['x'] == 0
    assert coords[1]['y'] == 1
    assert coords[2]['x'] == -1
    assert coords[2]['y'] == 1
    assert coords[3]['x'] == 0
    assert coords[3]['y'] == 2
    print('passed rotate 1 Mirrored')

    p = Piece('ENS')
    coords = p.translate({'x': 0, 'y': 0}, 2, True)
    assert len(coords) == 4
    assert coords[0]['x'] == 0
    assert coords[0]['y'] == 0
    assert coords[1]['x'] == 1
    assert coords[1]['y'] == 0
    assert coords[2]['x'] == 1
    assert coords[2]['y'] == 1
    assert coords[3]['x'] == 2
    assert coords[3]['y'] == 0
    print('passed rotate 2 Mirrored')

    p = Piece('ENS')
    coords = p.translate({'x': 0, 'y': 0}, 3, True)
    assert len(coords) == 4
    assert coords[0]['x'] == 0
    assert coords[0]['y'] == 0
    assert coords[1]['x'] == 0
    assert coords[1]['y'] == -1
    assert coords[2]['x'] == 1
    assert coords[2]['y'] == -1
    assert coords[3]['x'] == 0
    assert coords[3]['y'] == -2
    print('passed rotate 3 Mirrored')

    b = Board()

    p = Piece("S")
    coords = p.translate({'x': 19, 'y': 19}, 0, False)
    try:
        b.isValid(coords, '')
        assert False == True
    except OutOfBoundsError:
        assert True == True
    print("passed piece goes out of bounds")

    b.initialize()

    p = Piece("E")
    coords = p.translate({'x': 19, 'y': 19}, 0, False)
    try:
        b.isValid(coords, '')
        assert False == True
    except OutOfBoundsError:
        assert True == True
    print("passed piece goes out of bounds, it failed correctly")

    b.initialize()

    p = Piece('E')
    coords = p.translate({'x': 0, 'y': 0}, 0, False)
    try:
        b.isValid(coords, '')
        assert True == True
    except OutOfBoundsError:
        assert False == True
    print("passed piece stays in bounds")

    b.initialize()

    try:
        b.placePiece(0, 0, 0, False, p, Color.R.value)
        assert True == True
    except OccupiedSquareError:
        assert False == True
    print("passed place a non-overlapping piece")
    try:
        b.placePiece(0, 0, 0, False, p, Color.B.value)
        assert False == True
    except OccupiedSquareError:
        assert True == True
    print("passed placing an overlapping piece, it failed correctly")

    b.initialize()

    p = Piece('')
    b.placePiece(0, 0, 0, False, p, Color.R.value)

    assert b.isEdgesValid(0, 1, Color.R.value) == False
    print("passed placing piece to right with shared edge, it failed correctly")

    assert b.isEdgesValid(1, 0, Color.R.value) == False
    print("passed placing piece to below with shared edge, it failed correctly")

    b.initialize()

    b.placePiece(0, 0, 2, True, Piece('EENN'), Color.R.value)

    assert b.isEdgesValid(1, 2, Color.R.value) == False
    print("passed placing piece to left with shared edge, it failed correctly")

    assert b.isEdgesValid(3, 1, Color.R.value) == False
    print("passed placing piece to right with shared edge, it failed correctly")

    assert b.isEdgesValid(2, 3, Color.R.value) == False
    print("passed placing piece to below with shared edge, it failed correctly")

    assert b.isEdgesValid(3, 3, Color.R.value) == True
    print("passed placing piece")

    b.initialize()

    b.placePiece(0, 0, 1, False, Piece('EENN'), Color.R.value)

    assert b.isEdgesValid(2, 1, Color.R.value) == False
    print("passed placing piece to above with shared edge, it failed correctly")

    assert b.isEdgesValid(3, 1, Color.R.value) == True
    print("passed placing piece NE")

    assert b.isEdgesValid(3, 3, Color.R.value) == True
    print("passed placing piece SE")

    assert b.isTouchingCorner(3, 4, Color.R.value) == False
    print("passed placing a piece not connected to color by corner")

    assert b.isTouchingCorner(3, 3, Color.R.value) == True
    print("passed placing a piece connected to color by corner")

    b.initialize()

    b.placePiece(0, 0, 0, False, p, Color.R.value)
    try:
        b.isEdgesValid(1, 1, Color.R.value)
        assert True == True
    except:
        assert False == True
    print("passed validating edge against edge of board")

    return render(request, 'index.html')