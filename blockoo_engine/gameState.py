#!/usr/bin/env python
from board import Board
from piece import Piece
from player import Player
from termcolor import colored
from colorama import init

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

        self.players.append(Player('green', pieces.copy()))
        self.players.append(Player('red', pieces.copy()))
        self.players.append(Player('blue', pieces.copy()))
        self.players.append(Player('yellow', pieces.copy()))

    def placePiece(self, sourceX, sourceY, rotationMod, isMirrored, pieceCode, color):

        self.preTurnCheck(color)

        player = self.getPlayerByColor(color)
        piece = player.removePiece(pieceCode)

        for i, p in enumerate(self.players):
            if p.color == player.color:
                playerMakingMoveIdx = i

        if playerMakingMoveIdx is None or playerMakingMoveIdx is not self.activePlayerId:
            raise Error(f"It's not your turn, {color}!")
        
        self.myBoard.placePiece(sourceX, sourceY, rotationMod, isMirrored, piece, player.color)

        self.postTurnCheck()

    def preTurnCheck(self, color):
        if not self.gameHasActivePlayer():
            raise GameOver()

        if self.getPlayerByColor(color).isFinished:
            raise Error("Player has passed their turn and cannot play again")

    def postTurnCheck(self):
        if not self.gameHasActivePlayer():
            raise GameOver()

        self.moveToNextTurn()
        

    def getPlayerByColor(self, color):
        for p in self.players:
            if p.color == color:
                return p
        
        raise Error("Could not find player: " + color)

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

    def setPlayerFinished(self, color):
        self.getPlayerByColor(color).isFinished = True

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