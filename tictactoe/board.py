import pygame
from pyVariables import *
from cell import Cell



class Board:
    """
    A class to represent a board, or a group of cells in a game of tic tac toe.

    params:
        row_width: Number of cells that makes up the width of board.
        row_height: Number of cells that makes up the height of the board.
        x: The x position of the top left position of the board.
        y: The y position of the top left position of the board.
        cell_width: The width of a single cell.
        cell_height: The height of a single cell.
    """
    def __init__(self, row_width, row_height, x, y, cell_width, cell_height):
        self.width = row_width
        self.height = row_height

        self.x = x
        self.y = y
        self.cell_width = cell_width
        self.cell_height = cell_height

        self.board = []
        self.create_board()
        self.diagonals = []
        self._create_diagonal_rows()
        self.columns = []
        self._create_columns()



    def create_board(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append( Cell( ( self.x + (j*self.cell_width),
                                    self.y + (i*self.cell_height),
                                    self.cell_width,
                                    self.cell_height ),
                                    state=None) )
            self.board.append(row)


    def clear_board(self):
        """Resets the cell state for each cell in the board to its default value
        of None. """
        for row in board:
            for cell in row:
                cell.state = None


    def _check_row(self, row):
        """
        Given a row, checks to see if the state of each cell in the row
        contains the same value. Does so by iterating through each cell in the
        given row, and checking the state of that cell, and returning False if
        any cell in the row does not match the cell state of the first value in
        that row.
        """
        row_value = row[0].state
        same_value = True
        for cell in row:
            if row_value != cell.state:
                same_value = False
                break
        return same_value


    def _create_diagonal_rows(self):
        """Populates the list of both diagonals, and saves them for easier
        checking of each row."""


        """Top Left-Bottom Right diagonal"""
        diagonal_row = []
        for i in range(self.width):
            diagonal_row.append(self.board[i][i])
        self.diagonals.append(diagonal_row)

        """Bottom Left-Top Right diagonal"""
        diagonal_row = []
        for i in range(self.width):
            diagonal_row.append(self.board[i][(self.width-1)-i])
        self.diagonals.append(diagonal_row)


    def _create_columns(self):
        """Populates the coluns list with all the columns, and saves them for
        easier checking of each state value."""
        for i in range(self.width):
            column = []
            for j in range(self.height):
                column.append(self.board[i][j])
            self.columns.append(column)





    def _cell_update(self, surface, *args):
        """calls the update method for each Cell contained in the board"""
        for row in self.board:
            for cell in row:
                cell.update(surface, *args)


    def _cell_get_event(self, event, *args):
        """Calls get_event for each cell in the board"""
        for row in self.board:
            for cell in row:
                cell.get_event(event, *args)


    def get_event(self, event, *args):
        """Boards main get_event method"""
        self._cell_get_event(event, *args)


    def update(self, surface, *args):
        """Boards main update method"""
        self._cell_update(surface, *args)



if __name__ == '__main__':

    pygame.init()
    surface = pygame.display.set_mode((600,600))
    surface.fill((WHITE2))
    pygame.display.set_caption("Tic Tac Toe Board")

    B = Board(4, 4, 100, 100, 100, 100)
    run = True
    player_turn = "O"
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            B.get_event(event, player_turn)

            if event.type == pygame.MOUSEBUTTONUP:
                if player_turn == 'X':
                    player_turn = 'O'
                else:
                    player_turn = 'X'



        B.update(surface)

        pygame.display.update()