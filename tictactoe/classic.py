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
        self.cells_filled = 0


    def handle_ruleset(self):
        self.handle_turn()
        self.win_state()



    def handle_turn(self):
        if self.turns_elapsed % 2 == 0:
            self.player_turn = 0
        else:
            self.player_turn = 1


    def check_num_state_changes(self):
        cells_filled = 0
        for row in self.board:
            for cell in row:
                if cell.state:
                    cells_filled += 1

        self.cells_filled = cells_filled


    def pass_player_symbol(self):
        self.turns_elapsed += 1
        return self.players[self.player_turn]







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
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                C.get_event(event, C.pass_player_symbol())
            print(f"{C.turns_elapsed}")
            print(f"{C.board.board[0][0]}")

        C.update(surface)
        pygame.display.update()
