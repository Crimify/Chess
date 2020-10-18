#!/usr/bin/python3
import pygame as p
from ChessFoundation import Chessboard
from Chess.constants import *


FPS = 30

WIN = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Chess')


def main():
    run = True 
    clock = p.time.Clock()
    
    while run: 
        clock.tick(FPS)
        
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            if event.type == p.MOUSEBUTTONDOWN: 
                pass 
    p.quit() 
