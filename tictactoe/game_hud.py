"""
game_hud.py - The heads up display --> The score, buttons etc in for the main
game state.
"""
from pyVariables import *
from buttons import Button
from symbols import draw_x, draw_o

class HUD:
    def __init__(self):
        pass


    def create_reset_button(self, function=None):
        self.reset_button = Button((RESET_X,RESET_Y,RESET_WIDTH,RESET_HEIGHT),
            function, hover_color=PURPLE2 ,text="Reset")


    def scoreboard(self, surface, score1, score2,
                         score1_symbol=None, score2_symbol=None, **kwargs):
        font = pygame.font.SysFont(None,50)
        text = font.render('SCORE', True, BLACK)
        if score1_symbol and score2_symbol:
            score1_symbol()
            score2_symbol()
        else:
            text = font.render('X', True, BLACK)
            text2 = font.render('O', True, BLACK)

    def get_event(self, event, *args):
        self.reset_button.get_event(event)


    def update(self, surface, *args):
        self.reset_button.update(surface)



if __name__ == "__main__":
    import pygame

    pygame.init()
    surface = pygame.display.set_mode((DIS_X,DIS_Y))
    surface.fill((WHITE2))
    pygame.display.set_caption("Tic Tac Toe")

    H = HUD()
    def f():
        print('Hello World')
    H.create_reset_button(f)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            H.get_event(event)

        H.update(surface)
        pygame.display.update()
