#!/usr/bin/env python
from board import Board
from piece import Piece
from player import Player
from termcolor import colored
from colorama import init
import json

init()

class GameState:

    myBoard = Board()
    players = []
    activePlayerId = 0

    def __init__(self):
        pieces = [
            Piece('0'),
            Piece('03'),
            Piece('035'),
            Piece('033'),
            Piece('0333'),
            Piece('0335'),
            Piece('0353'),
            Piece('0531'),
            Piece('0336'),
            Piece('05336'),
            Piece('03333'),
            Piece('03335'),
            Piece('05331'),
            Piece('03353'),
            Piece('03363'),
            Piece('03365'),
            Piece('03355'),
            Piece('03553'),
            Piece('03535'),
            Piece('03146'),
            Piece('03336'),
        ]

        self.players.append(Player(0, 'green', pieces.copy()))
        self.players.append(Player(1, 'red', pieces.copy()))
        self.players.append(Player(2, 'blue', pieces.copy()))
        self.players.append(Player(3, 'yellow', pieces.copy()))

    def placePiece(self, sourceX, sourceY, rotationMod, isMirrored, pieceCode, playerId):

        self.preTurnCheck(playerId)

        player = self.getPlayerById(playerId)
        piece = player.removePiece(pieceCode)

        for i, p in enumerate(self.players):
            if p.color == player.color:
                playerMakingMoveIdx = i

        if playerMakingMoveIdx is None or playerMakingMoveIdx is not self.activePlayerId:
            raise Error(f"It's not your turn, {player.id}!")
        
        self.myBoard.placePiece(sourceX, sourceY, rotationMod, isMirrored, piece, player.color)

        self.postTurnCheck()

    def preTurnCheck(self, playerId):
        if not self.gameHasActivePlayer():
            raise GameOver()

        if self.getPlayerById(playerId).isFinished:
            raise Error("Player has passed their turn and cannot play again")

    def postTurnCheck(self):
        if not self.gameHasActivePlayer():
            raise GameOver()

        self.moveToNextTurn()
        #self.saveGameState()

    def saveGameState(self):
        gameStateObj = {}
        gameStateObj['board']  = self.myBoard
        gameStateObj['players'] = self.players
        gameStateObj['activePlayerId'] = self.activePlayerId
        print(json.dumps(gameStateObj))
        

    def getPlayerById(self, playerId):
        for p in self.players:
            if p.id == playerId:
                return p
        
        raise Error("Could not find player id: " + playerId)

    def printGameState(self):
        for domain in range(len(self.myBoard.arr)):
            for raange in range(len(self.myBoard.arr[domain])):
                print(colored(f"  ", 'black', 'on_'+self.myBoard.arr[domain][raange]["color"]), end = "")
            print("")

    def printPiecesAvailableForPlayers(self):
        for player in self.players:
            for piece in player.pieceSet:
                print(colored(piece.id, 'black', 'on_'+player.color), end = " ")
            print("")

    def moveToNextTurn(self):

        if not self.gameHasActivePlayer():
            return

        while True:
            if self.activePlayerId < len(self.players) - 1:
                self.activePlayerId = self.activePlayerId + 1
            else:
                self.activePlayerId = 0
            
            if not self.players[self.activePlayerId].isFinished:
                break

    def setPlayerFinished(self, playerId):
        self.getPlayerById(playerId).isFinished = True

        self.postTurnCheck()

    def gameHasActivePlayer(self):
        playerIsStillActive = False
        for player in self.players:
            playerIsStillActive = not player.isFinished or playerIsStillActive

        return playerIsStillActive;

class Error(Exception):
    def __init__(self, message):
        self.message = message

class GameOver(Exception):
    def __init__(self):
        pass