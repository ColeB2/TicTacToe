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
        self.last_player = ''
        self.winner = False

        self.x_score = 0
        self.o_score = 0

    def handle_ruleset(self):
        """Method used to handle overall ruleset. Calls all the major rules of
        the game."""
        self.handle_turn()
        self.win_state()



    def handle_turn(self):
        self.board.click_symbol = self.players[self.board.turn % 2]


    def handle_scoring(self):
        if self.board.last_symbol_placed == 'X':
            self.x_score += 1
        elif self.board.last_symbol_placed == 'O':
            self.o_score += 1



    def win_state(self):
        """
        Loops through the rows required to win a game of tic tac toe, returns
        the result of its findings, True if a row has 3 in a row, false otherwise.
        """
        result = False
        if result == False and self.board.turn >=5:
            for set in self.rows:
                for row in set:
                    result = self.board._check_row(row)
                    if result == True:
                        self.handle_scoring()
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
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            C.get_event(event)
        C.handle_ruleset()


        C.update(surface)
        pygame.display.update()
