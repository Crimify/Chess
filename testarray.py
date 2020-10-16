#!/usr/bin/python3
#this is a chess board represented in a array
#c-castle n-knight b-bishop q-queen k-king p-pawn 1-blank sqaure 
board = [['c','n','b','q','k','b','n','c'],['p','p','p','p','p','p','p','p']]

board.insert(2, [1,1,1,1,1,1,1,1])
board.insert(3, board[2])
board.insert(4, board[3])
board.insert(5, board[4])
board.insert(6, board[1])
board.insert(7, board[0])
for row in board:
    for piece in row:
        print(piece,end=" ")
    print()

