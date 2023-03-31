from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import BoardState, Player
from django.http import HttpResponseServerError
from django.template import loader
import json

def index(request):
    return HttpResponse(loader.get_template('index.html').render({}, request))

def getBoardState(request, board_id):
    try:
        boardState = BoardState.objects.get(id=board_id)
        return asJsonResponse(boardState)
    except BoardState.DoesNotExist:
        raise HttpResponseServerError("Unabled to find that board")
    
def getBoardPlayers(request, board_id):
    try:
        players = Player.objects.filter(board_id=board_id)
        return asJsonList(players)
    except BoardState.DoesNotExist:
        raise HttpResponseServerError("Unabled to find players for that board")
        
def placePiece(request, board_id):

    if request.method != "POST":
        raise HttpResponseServerError("Invalid request")
    
    print(json.loads(request.body))

    return asJsonResponse({})

    try:
        boardState = BoardState.objects.get(id=board_id)
        return asJsonList(players)
    except BoardState.DoesNotExist:
        raise HttpResponseServerError("Unabled to find players for that board")
    
def asJsonResponse(obj):
    rtv = json.loads(json.dumps(obj, default=lambda obj: obj.__dict__))
    if '_state' in rtv:
        rtv.pop('_state')
    return JsonResponse(rtv, safe=False)
    
def asJsonList(obj):
    rtv = []
    for o in obj:
        appended = json.loads(json.dumps(o, default=lambda obj: obj.__dict__))
        appended.pop('_state')
        rtv.append(appended)
    
    return JsonResponse(rtv, safe=False)