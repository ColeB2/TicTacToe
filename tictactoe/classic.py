import pygame
from pyVariables import *
from board import Board
"""
Todo:

"""


class ClassicTicTacToe:
    """
    A class to represent and encapsulate the rules for class 3x3 variation of
        tic tac toe.
    """
    def __init__(self):
        self.board = Board(3, 3, 100, 100, 100, 100)

        self.rows = [self.board.board, self.board.diagonals, self.board.columns]
        self.players = ['X','O']
        self.player_turn = 0
        self.turns_elapsed = 0



    def main_loop(self):
        pass

    def handle_turn(self):
        if event.type == pygame.MOUSEBUTTONUP:
        pass




    def win_state(self):
        """
        Loops through the rows required to win a game of tic tac toe, returns
        the result of its findings, True if a row has 3 in a row, false otherwise.
        """
        result = False
        if result == False:
            for set in self.rows:
                for row in set:
                    result = self.board._check_row(row)
                    if result == True:
                        return result
        return result


    def get_event(self, event, *args):
        self.board.get_event(event, *args)


    def update(self, surface, *args):
        self.board.update(surface, *args)


if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((600,600))
    surface.fill((WHITE2))
    pygame.display.set_caption("Tic Tac Toe Board")

    C = ClassicTicTacToe()

    run = True
    player_turn = "O"
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            C.get_event(event, player_turn)

        C.update(surface)
        pygame.display.update()
