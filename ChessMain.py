
import pygame as p 
from Chess.ChessFoundation import Chessboard
from Chess.constants import *

FPS = 30

myboard = Chessboard()
myboard.printboard()
WIN = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Chess')
IMAGES = {}

def loadImages():
    pieces = ['wp', 'wC','wN','wB','wK','wQ','bp','bC','bN','bB','bK','bQ']
    for piece in pieces:
        IMAGES[piece] = p.image.load("images/"+piece +".png")
    


def main():
    run = True 
    clock = p.time.Clock()
    
    
    while run: 
        
        clock.tick(FPS)
        
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            if event.type == p.MOUSEBUTTONDOWN: 
                print("Boomer")
    p.quit() 
main()
