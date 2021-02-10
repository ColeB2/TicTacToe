import pygame
from pyVariables import *



class Cell:
    """
    A class to represent a single Cell in a game of tic tac toe.

    params:
        rect: Tutple of integer values -> (top, left, width, height)
        state: State of Cell -> blank -> ' '. 'X' or 'O'
        """
    def __init__(self, rect, state=None):
        self.rect = pygame.Rect(rect)
        self.state = state

        self.clicked = False
        self.hovered = True
        self.hover_color = (LIGHT_GREEN)
        self.player_symbol = None
        self.run_on_release = False

    def __str__(self):
        return f"Cell Rect: {self.rect} Cell State: {self.state}"



    """Drawing Functions"""
    def draw_x(self, surface):
        """
        Draws the X over the cell. Does so by drawing two lines in X shape.
        1st line --> Top left, to bottom right.
        2nd line --> Top right, to bottom left.
        X_OFFSET --> Offset the X/Cross needs on each corner of the cell to
            fit nicely within it."""
        X_OFFSET = int(self.rect[2] * 0.20)
        pygame.draw.line(surface, BLACK,
                (self.rect[0] + X_OFFSET,
                 self.rect[1] + X_OFFSET),
                (self.rect[0] + self.rect[2] - X_OFFSET,
                 self.rect[1] + self.rect[3] - X_OFFSET),  5)
        pygame.draw.line(surface, BLACK,
                (self.rect[0] + self.rect[2] - X_OFFSET,
                 self.rect[1] + X_OFFSET),
                (self.rect[0] + X_OFFSET,
                 self.rect[1] + self.rect[3] - X_OFFSET),5)


    def draw_o(self, surface):
        """
        Draws the O/Naught over top of the cell. Does so by drawing a circle,
        given a center tuple, and a radius.
        center --> rect[0] + rect[2]/2 --> X value + half width,
                   rect[1] + rect[3]/2 --> Y value + half height,
        radius --> rect[3]/3 --> Height / 3
        """
        pygame.draw.circle(surface, RED,
            (int(self.rect[0] + self.rect[2]/2),
            int(self.rect[1] + self.rect[3]/2) ),
            int(self.rect[3]/3), O_THICKNESS)


    """Cell State and State Functions"""
    def change_state(self, player_symbol):
        """Displays the cell on the board."""
        if self.state == None:
            self.state = player_symbol


    """Event Handler"""
    def get_event(self, event, *args):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._handle_click(*args)
        elif event.type == pygame.MOUSEBUTTONUP and event.button ==1:
            self._handle_release(*args)


    """Internal Methods"""
    def _handle_click(self, *args):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.clicked = True
            if not self.run_on_release:
                self.change_state(*args)


    def _handle_release(self, *args):
        if self.clicked and self.run_on_release:
            self.change_state(*args)
        self.clicked = False


    def _handle_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.hovered == False:
                self.hovered = True
        else:
            self.hovered = False


    def update(self, surface, *args):
        color = GRAY
        self._handle_hover()

        if self.clicked and self.hover_color:
            color = self.hover_color
        elif self.hovered and self.hover_color:
            color = self.hover_color


        pygame.draw.rect(surface, color, self.rect, width=0)
        if self.state:
            if self.state == 'X':
                self.draw_x(surface)
            elif self.state == 'O':
                self.draw_o(surface)





if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((600,600))
    surface.fill((WHITE2))
    pygame.display.set_caption("Tic Tac Toe Cell")

    def X():
        return 'X'
    def O():
        return 'O'



    cell = Cell(rect=(100,100,100,100), state=None)
    cell2 = Cell(rect=(200,100,100,100), state=None)
    cell3 = Cell(rect=(100,200,100,100), state=None)
    cell4 = Cell(rect=(200,200,100,100), state=None)
    run = True
    player_turn = "O"
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            cell.get_event(event, player_turn)
            cell2.get_event(event, player_turn)
            cell3.get_event(event, player_turn)
            cell4.get_event(event, player_turn)

            if event.type == pygame.MOUSEBUTTONUP:
                if player_turn == 'X':
                    player_turn = 'O'
                else:
                    player_turn = 'X'

        cell.update(surface)
        cell2.update(surface)
        cell3.update(surface)
        cell4.update(surface)
        pygame.display.update()