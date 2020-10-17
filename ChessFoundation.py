#!/usr/bin/python3
#c-castle n-knight b-bishop q-queen k-king p-pawn -blank sqaure 

#create a class for the 2d array as a representation for the chess board and pieces 
class foundation():
        def __init__(self):  
            #def- defining the function __init__ and initializing the objects state, object is self 
            # self is a instance of the entire class        
            self.board = [
                ['bC','bN','bB','bQ','bK','bB','bN','bC'],
                ['bp','bp','bp','bp','bp','bp','bp','bp'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['wp','wp','wp','wp','wp','wp','wp','wp'],
                ['wC','wN','wB','wQ','wK','wB','wN','wC']]
            #self.board is creating the array used for the state of the board represented
            #by two characters in a string format

    

