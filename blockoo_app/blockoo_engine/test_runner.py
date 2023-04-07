#!/usr/bin/env python
from board import Board

from piece import Piece
from gameState import GameState, Error, GameOver

gs = GameState()

gs.printGameState()

try:
    gs.placePiece(0, 0, 0, False,"03535", 0)
    gs.placePiece(19, 19, 2, False,"03535", 1)
    gs.placePiece(0, 19, 3, False,"03535", 2)
    gs.placePiece(19, 0, 1, False,"03535", 3)

    print("Round 1 complete")

    gs.placePiece(3, 3, 1, False,"03333", 0)
    gs.placePiece(16, 16, 2, False,"03333", 1)
    gs.placePiece(3, 16, 0, False,"03333", 2)
    gs.placePiece(16, 3, 1, False,"03333", 3)

    print("Round 2 complete")

    gs.placePiece(4, 8, 0, False,"05331", 0)
    gs.placePiece(11, 13, 1, False,"05331", 1)
    gs.placePiece(8, 13, 1, True,"05331", 2)
    gs.placePiece(13, 8, 0, False,"05331", 3)

    print("Round 3 complete")

    gs.placePiece(7, 10, 0, False,"03363", 0)
    gs.placePiece(14, 11, 0, True,"03363", 1)
    gs.placePiece(5, 11, 0, False,"03363", 2)
    gs.placePiece(12, 10, 0, True,"03363", 3)

    print("Round 4 complete")

    gs.placePiece(7, 7, 0, False,"03335", 0)
    gs.placePiece(16, 9, 1, False,"03335", 1)
    gs.placePiece(4, 12, 2, False,"03335", 2)
    gs.placePiece(17, 8, 1, True,"03335", 3)

    print("Round 5 complete")

    gs.placePiece(11, 6, 0, False,"0335", 0)
    gs.placePiece(19, 11, 1, False,"03355", 1)
    gs.placePiece(0, 8, 0, False,"03355", 2)
    gs.placePiece(13, 0, 0, False,"03355", 3)

    print("Round 6 complete")

    gs.placePiece(3, 10, 1, False,"035", 0)
    gs.placePiece(18, 10, 3, False,"033", 1)
    gs.placePiece(8, 17, 2, True,"03353", 2)
    gs.placePiece(9, 9, 2, False,"0335", 3)

    print("Round 7 complete")

    gs.placePiece(0, 12, 3, False,"03336", 0)
    gs.placePiece(17, 7, 3, False,"03365", 1)
    gs.placePiece(3, 18, 1, True,"035", 2)
    gs.placePiece(12, 1, 2, False,"03336", 3)

    print("Round 8 complete")

    gs.placePiece(1, 13, 1, True,"0336", 0)
    gs.placePiece(19, 2, 0, True,"05336", 1)
    gs.placePiece(12, 15, 2, True,"05336", 2)
    gs.placePiece(7, 4, 1, False,"03353", 3)

    print("Round 9 complete")

    gs.placePiece(4, 2, 0, False,"03146", 0)
    gs.placePiece(16, 2, 3, False,"0335", 1)
    gs.placePiece(5, 18, 0, False,"033", 2)
    gs.placePiece(14, 3, 0, True,"03553", 3)

    print("Round 10 complete")

    gs.placePiece(8, 3, 0, False,"03553", 0)
    gs.placePiece(13, 19, 2, True,"03336", 1)
    gs.placePiece(15, 15, 0, False,"03336", 2)
    gs.placePiece(4, 3, 1, True,"0353", 3)

    print("Round 11 complete")

    gs.placePiece(10, 2, 0, False,"03355", 0)
    gs.placePiece(10, 18, 0, False,"03146", 1)
    gs.placePiece(19, 16, 1, False,"0336", 2)
    gs.placePiece(2, 0, 1, True,"05336", 3)

    print("Round 12 complete")

    gs.placePiece(3, 13, 0, False,"03365", 0)
    gs.placePiece(15, 3, 1, False,"03", 1)
    gs.placePiece(14, 12, 1, False,"0", 2)
    gs.placePiece(2, 3, 1, False,"03", 3)

    print("Round 13 complete")

    gs.placePiece(0, 3, 0, False,"0531", 0)
    gs.placePiece(13, 1, 0, False,"0531", 1)
    gs.placePiece(13, 10, 0, False,"0335", 2)
    gs.placePiece(1, 5, 1, False,"03146", 3)

    print("Round 14 complete")

    gs.placePiece(6, 0, 0, False,"0353", 0)
    gs.placePiece(14, 5, 1, True,"0336", 1)
    gs.placePiece(12, 9, 2, False,"03365", 2)
    gs.placePiece(19, 10, 3, False,"0333", 3)

    print("Round 15 complete")

    gs.placePiece(0, 16, 1, False,"03", 0)
    gs.placePiece(6, 19, 0, False,"0333", 1)
    gs.placePiece(10, 6, 2, False,"03", 2)
    gs.placePiece(10, 3, 0, False,"035", 3)

    print("Round 16 complete")

    gs.placePiece(2, 16, 0, False, "0", 0)
    gs.placePiece(9, 12, 0, False, "0", 1)
    gs.placePiece(12, 17, 0, False, "0333", 2)
    gs.placePiece(6, 3, 0, False,"0", 3)

    print("Round 17 complete")

    gs.placePiece(3, 17, 0, False, "0333", 0)
    gs.setPlayerFinished(1)
    gs.setPlayerFinished(2)
    gs.setPlayerFinished(3)

    print("Round 18 complete")

    gs.placePiece(6, 14, 0, False, "033", 0)

    print("Round 19 complete")

    gs.setPlayerFinished(0)
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