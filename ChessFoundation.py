#!/usr/bin/python3
#c-castle n-knight b-bishop q-queen k-king p-pawn -blank sqaure 

#create a class for the 2d array as a representation for the chess board and pieces 
class Chessboard():
    def __init__(self):
        self.board = [
                ['bC','bN','bB','bQ','bK','bB','bN','bC'],
                ['bp','bp','bp','bp','bp','bp','bp','bp'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['wp','wp','wp','wp','wp','wp','wp','wp'],
                ['wC','wN','wB','wQ','wK','wB','wN','wC']]
                
    def printboard(self):
        for row in self.board:
                print(row)

 