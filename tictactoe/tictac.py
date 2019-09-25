'''
tictac.py - Tic Tac Toe OOP
using pygme
'''

class Player:
    def __init__(self, piece='X'):
        self.piece = piece

class Board:
    def __init__(self):
        self.board = [
        ['','',''],
        ['','',''],
        ['','','']
        ]

    def display(self, width, height):
        '''Displays the board using pygame'''
        self.width = width
        self.height = height

        pygame.draw.line(DISPLAYSURF, RED, 0, DIS_X)


class Piece:
    def __init__(self):
        pass

class Game:
    def __init__(self):
        pass
