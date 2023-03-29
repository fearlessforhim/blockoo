#!/usr/bin/env python
from board import Board

from piece import Piece
from gameState import GameState, Error, GameOver

gs = GameState()

gs.printGameState()

try:
    gs.placePiece(0, 0, 0, False,"03535", "green")
    gs.placePiece(19, 19, 2, False,"03535", "red")
    gs.placePiece(0, 19, 3, False,"03535", "blue")
    gs.placePiece(19, 0, 1, False,"03535", "yellow")

    print("Round 1 complete")

    gs.placePiece(3, 3, 1, False,"03333", "green")
    gs.placePiece(16, 16, 2, False,"03333", "red")
    gs.placePiece(3, 16, 0, False,"03333", "blue")
    gs.placePiece(16, 3, 1, False,"03333", "yellow")

    print("Round 2 complete")

    gs.placePiece(4, 8, 0, False,"05331", "green")
    gs.placePiece(11, 13, 1, False,"05331", "red")
    gs.placePiece(8, 13, 1, True,"05331", "blue")
    gs.placePiece(13, 8, 0, False,"05331", "yellow")

    print("Round 3 complete")

    gs.placePiece(7, 10, 0, False,"03363", "green")
    gs.placePiece(14, 11, 0, True,"03363", "red")
    gs.placePiece(5, 11, 0, False,"03363", "blue")
    gs.placePiece(12, 10, 0, True,"03363", "yellow")

    print("Round 4 complete")

    gs.placePiece(7, 7, 0, False,"03335", "green")
    gs.placePiece(16, 9, 1, False,"03335", "red")
    gs.placePiece(4, 12, 2, False,"03335", "blue")
    gs.placePiece(17, 8, 1, True,"03335", "yellow")

    print("Round 5 complete")

    gs.placePiece(11, 6, 0, False,"0335", "green")
    gs.placePiece(19, 11, 1, False,"03355", "red")
    gs.placePiece(0, 8, 0, False,"03355", "blue")
    gs.placePiece(13, 0, 0, False,"03355", "yellow")

    print("Round 6 complete")

    gs.placePiece(3, 10, 1, False,"035", "green")
    gs.placePiece(18, 10, 3, False,"033", "red")
    gs.placePiece(8, 17, 2, True,"03353", "blue")
    gs.placePiece(9, 9, 2, False,"0335", "yellow")

    print("Round 7 complete")

    gs.placePiece(0, 12, 3, False,"03336", "green")
    gs.placePiece(17, 7, 3, False,"03365", "red")
    gs.placePiece(3, 18, 1, True,"035", "blue")
    gs.placePiece(12, 1, 2, False,"03336", "yellow")

    print("Round 8 complete")

    gs.placePiece(1, 13, 1, True,"0336", "green")
    gs.placePiece(19, 2, 0, True,"05336", "red")
    gs.placePiece(12, 15, 2, True,"05336", "blue")
    gs.placePiece(7, 4, 1, False,"03353", "yellow")

    print("Round 9 complete")

    gs.placePiece(4, 2, 0, False,"03146", "green")
    gs.placePiece(16, 2, 3, False,"0335", "red")
    gs.placePiece(5, 18, 0, False,"033", "blue")
    gs.placePiece(14, 3, 0, True,"03553", "yellow")

    print("Round 10 complete")

    gs.placePiece(8, 3, 0, False,"03553", "green")
    gs.placePiece(13, 19, 2, True,"03336", "red")
    gs.placePiece(15, 15, 0, False,"03336", "blue")
    gs.placePiece(4, 3, 1, True,"0353", "yellow")

    print("Round 11 complete")

    gs.placePiece(10, 2, 0, False,"03355", "green")
    gs.placePiece(10, 18, 0, False,"03146", "red")
    gs.placePiece(19, 16, 1, False,"0336", "blue")
    gs.placePiece(2, 0, 1, True,"05336", "yellow")

    print("Round 12 complete")

    gs.placePiece(3, 13, 0, False,"03365", "green")
    gs.placePiece(15, 3, 1, False,"03", "red")
    gs.placePiece(14, 12, 1, False,"0", "blue")
    gs.placePiece(2, 3, 1, False,"03", "yellow")

    print("Round 13 complete")

    gs.placePiece(0, 3, 0, False,"0531", "green")
    gs.placePiece(13, 1, 0, False,"0531", "red")
    gs.placePiece(13, 10, 0, False,"0335", "blue")
    gs.placePiece(1, 5, 1, False,"03146", "yellow")

    print("Round 14 complete")

    gs.placePiece(6, 0, 0, False,"0353", "green")
    gs.placePiece(14, 5, 1, True,"0336", "red")
    gs.placePiece(12, 9, 2, False,"03365", "blue")
    gs.placePiece(19, 10, 3, False,"0333", "yellow")

    print("Round 15 complete")

    gs.placePiece(0, 16, 1, False,"03", "green")
    gs.placePiece(6, 19, 0, False,"0333", "red")
    gs.placePiece(10, 6, 2, False,"03", "blue")
    gs.placePiece(10, 3, 0, False,"035", "yellow")

    print("Round 16 complete")

    gs.placePiece(2, 16, 0, False, "0", "green")
    gs.placePiece(9, 12, 0, False, "0", "red")
    gs.placePiece(12, 17, 0, False, "0333", "blue")
    gs.placePiece(6, 3, 0, False,"0", "yellow")

    print("Round 17 complete")

    gs.placePiece(3, 17, 0, False, "0333", "green")
    gs.setPlayerFinished("red")
    gs.setPlayerFinished("blue")
    gs.setPlayerFinished("yellow")

    print("Round 18 complete")

    gs.placePiece(6, 14, 0, False, "033", "green")

    print("Round 19 complete")

    gs.setPlayerFinished("green")
except GameOver:
    print("Game is finished")

print("")

gs.printGameState()
gs.printPiecesAvailableForPlayers()

myPlayers = gs.players.copy();

myPlayers.sort(key=lambda p:p.calculateScore(), reverse=True)

for p in myPlayers:
    print(f"{p.color} finished with a score of {p.calculateScore()}")

print(f"{myPlayers[0].color} player wins!")