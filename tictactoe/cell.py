import pygame
from pyVariables import *
from symbols import draw_x, draw_o



class Cell:
    """
    A class to represent a single Cell in a game of tic tac toe.

    params:
        rect: Tutple of integer values -> (left, top, width, height)
        state: State of Cell -> blank -> ' '. 'X' or 'O'
        """
    def __init__(self, rect, state=None):
        self.rect = pygame.Rect(rect)
        self.state = state

        self.clicked = False
        self.hovered = True
        self.hover_color = (LIGHT_GREEN)
        self.run_on_release = False



    def __str__(self):
        return f"Cell Rect: {self.rect} Cell State: {self.state}"



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

        if self.clicked:
            color = self.hover_color
        elif self.hovered:
            color = self.hover_color


        pygame.draw.rect(surface, color, self.rect, width=0)
        if self.state:
            if self.state == 'X':
                draw_x(surface, self.rect, offset=CLASSIC_X_OFFSET)
            elif self.state == 'O':
                draw_o(surface, self.rect)





if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((600,600))
    surface.fill((WHITE2))
    pygame.display.set_caption("Tic Tac Toe Cell")

    """Create the Cells"""
    cell1 = Cell(rect=(100,100,100,100), state=None)
    cell2 = Cell(rect=(200,100,100,100), state=None)
    cell3 = Cell(rect=(100,200,100,100), state=None)
    cell4 = Cell(rect=(200,200,100,100), state=None)
    cells = [cell1, cell2, cell3, cell4]

    """More Pygame Loop"""
    run = True
    player_turn = ['X','O']
    turn = 0

    """Main Loop"""
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            """Call get_event for all cells, --> Board method"""
            for cell in cells:
                cell.get_event(event)
                """Handle click function stuff"""
                if cell.clicked == True and cell.state == None:
                    turn +=1
                    symbol = turn % 2
                    cell.state = player_turn[symbol]

        for CELL in cells:
            CELL.update(surface)
        pygame.display.update()
