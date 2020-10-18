
import pygame
from ChessFoundation import Chessboard
from Chess.constants import *


FPS = 30

myboard = Chessboard()
myboard.printboard()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

def main():
    run = True 
    clock = pygame.time.Clock()
    
    
    while run: 
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                print("Crim")
    
    pygame.quit() 
main()
