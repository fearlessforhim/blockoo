from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import BoardState, Player, PlayerPiece, Piece
from django.http import HttpResponseServerError
from django.template import loader
from .gameStateManager import GameStateManager, Error
from blockoo_engine.player import PlayerDTO
from blockoo_engine.piece import PieceDTO
from blockoo_engine.board import BoardDTO
import json

def index(request):
    return HttpResponse(loader.get_template('index.html').render({}, request)) 
    
def getBoardState(request, board_id):
    try:
        boardState = BoardState.objects.get(id=board_id)

        finalScore = {}

        print(boardState.gameIsOver)

        if boardState.gameIsOver:
            playerDAOs = Player.objects.filter(board_id=board_id)
            for player in playerDAOs:
                playerScore = 0
                for playerPiece in PlayerPiece.objects.filter(player_id=player.id):
                    playerScore = playerScore + len(playerPiece.piece_id)
                
                finalScore[player.color] = playerScore

        return asJsonResponse({"boardState": boardState, "finalScore": finalScore})
    except BoardState.DoesNotExist:
        raise HttpResponseServerError("Unabled to find that board")
    
def getBoardPlayers(request, board_id):
    try:
        playerDAOs = Player.objects.filter(board_id=board_id)

        playerDTOs = []

        for p in playerDAOs:
            playerPieceDAOs = PlayerPiece.objects.filter(player_id=p.id)
            pieceDTOs = []
            for dao in playerPieceDAOs:
                pieceDTOs.append(dao.piece.id)
                
            playerDTOs.append(PlayerDTO(p.id, p.color, pieceDTOs, p.isFinished))

        return asJsonList(playerDTOs)
    except BoardState.DoesNotExist:
        raise HttpResponseServerError("Unable to find players for that board")
        
def placePiece(request, board_id):
    try:
        if request.method != "POST":
            raise HttpResponseServerError("Invalid request")
        
        boardState = BoardState.objects.get(id=board_id)
        playerDAOs = Player.objects.filter(board_id=board_id)

        playersDTOs = []

        for p in playerDAOs:
            playerPieceDAOs = PlayerPiece.objects.filter(player_id=p.id)
            pieceDTOs = []
            for dao in playerPieceDAOs:
                pieceDTOs.append(PieceDTO(dao.piece.id))
                
            playersDTOs.append(PlayerDTO(p.id, p.color, pieceDTOs, p.isFinished))

        requestJson = json.loads(request.body)

        mgr = GameStateManager(boardState, playersDTOs)
        mgr.placePiece(requestJson["posX"], requestJson["posY"], requestJson["rotation"], requestJson["mirrored"], requestJson["piece"], requestJson["player"])
        
        placedPieceDAO = Piece.objects.get(id=requestJson["piece"])
        placedPlayerPieceDAO = PlayerPiece.objects.get(player_id=requestJson["player"], piece_id=placedPieceDAO.id)
        placedPlayerPieceDAO.delete()

        newState = ""
        for r in mgr.myBoard.arr:
            for c in r:
                newState = newState + c + "|"
            newState = newState[:len(newState)-1]
            newState = newState + "\n"

        boardState.boardState = newState[:len(newState)-1]
        boardState.activePlayerInGameId = mgr.activePlayerId
        boardState.save()

        return asJsonResponse({})
    except Exception as e:
        print(e.message)
        return asJsonResponse({"isError": True, "message": e.message})
    
def gameReset(request, board_id):

    #reset board to fresh state
    newBoardDTO = BoardDTO('')
    boardStateDAO = BoardState.objects.get(id=board_id)

    newState = ""
    for r in newBoardDTO.arr:
        for c in r:
            newState = newState + c + "|"
        newState = newState[:len(newState)-1]
        newState = newState + "\n"

    boardStateDAO.boardState = newState[:len(newState)-1]
    boardStateDAO.activePlayerInGameId = 0
    boardStateDAO.gameIsOver = False
    boardStateDAO.save()

    #give all players all pieces
    playerDAOs = Player.objects.filter(board_id=board_id)
    pieceDAOs = Piece.objects.all()
    for player in playerDAOs:
        player.isFinished = False
        playerPieceDAOs = PlayerPiece.objects.filter(player_id=player.id)
        for p in playerPieceDAOs:
            p.delete()

        for piece in pieceDAOs:
            newPlayerPiece = PlayerPiece()
            newPlayerPiece.player_id = player.id
            newPlayerPiece.piece_id = piece.id
            newPlayerPiece.save()
        player.save()

    return asJsonResponse({})

def finishPlayer(request, board_id):
    boardStateDAO = BoardState.objects.get(id=board_id)

    currentPlayerId = boardStateDAO.activePlayerInGameId;

    currentPlayer = Player.objects.get(id=currentPlayerId)
    currentPlayer.isFinished = True
    currentPlayer.save()

    if(currentPlayerId < 3):
        boardStateDAO.activePlayerInGameId = currentPlayerId + 1;
    else:
        boardStateDAO.activePlayerInGameId = 0;

    playerIsStillActive = False
    for player in Player.objects.filter(board_id=board_id):
        playerIsStillActive = not player.isFinished or playerIsStillActive

    boardStateDAO.gameIsOver = not playerIsStillActive

    print(f'Player {currentPlayer.color}')
    print(currentPlayer.isFinished)

    boardStateDAO.save();    

    return asJsonResponse({})

def endGame(request, board_id):
    boardStateDAO = BoardState.objects.get(id=board_id)
    
    
def asJsonResponse(obj):
    rtv = json.loads(json.dumps(obj, default=lambda obj: obj.__dict__))
    if '_state' in rtv:
        rtv.pop('_state')
    return JsonResponse(rtv, safe=False)
    
def asJsonList(obj):
    rtv = []
    for o in obj:
        appended = json.loads(json.dumps(o.__dict__))
        if '_state' in rtv:
            rtv.pop('_state')
        rtv.append(appended)
    
    return JsonResponse(rtv, safe=False)