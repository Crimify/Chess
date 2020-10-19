
import pygame as p 
from Chess.ChessFoundation import Chessboard
from Chess.constants import *

FPS = 30
p.init()



IMAGES = {}

def loadImages():
    pieces = ['wp', 'wC','wN','wB','wK','wQ','bp','bC','bN','bB','bK','bQ']
    for piece in pieces:
        IMAGES[piece] = p.image.load("images/"+piece+".png")


def main():
    run = True 
    window = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption('Chess')
    clock = p.time.Clock()
    myboard = Chessboard()
    loadImages()
    window.fill(BLACK)
    while run: 
        
        clock.tick(FPS)
        
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            if event.type == p.MOUSEBUTTONDOWN: 
                mouselocation = p.mouse.get_pos()
                print(mouselocation)
        gameFoundation(window, myboard)
        p.display.update()
    p.quit() 


def gameFoundation(window, myboard):
    drawBoard(window)
    drawPieces(window, myboard.board)

def drawBoard(window):
    for row in range(ROWS):
        for col in range(row % 2, ROWS, 2):
            p.draw.rect(window, WHITE, (row*SQ_SIZE, col*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(window, myboard):
    for row in range(ROWS):
        for col in range(COLUMNS):
            piece = myboard[col][row]
            if piece != "--":
                window.blit(IMAGES[piece], (row*SQ_SIZE, col*SQ_SIZE, SQ_SIZE, SQ_SIZE))


main()
