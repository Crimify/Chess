import pygame
from .constants import *
#c-castle n-knight b-bishop q-queen k-king p-pawn -blank sqaure 
#a class that stores the information of what the chess looks like throught the game
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
        self.whiteToMove = True 
        
 

 