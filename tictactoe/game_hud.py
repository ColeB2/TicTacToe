"""
game_hud.py - The heads up display --> The score, buttons etc in for the main
game state.
"""
from pyVariables import *
from buttons import Button
from symbols import draw_x, draw_o
import pygame

class HUD:
    def __init__(self):
        self.render_font()


    def create_reset_button(self, function=None):
        self.reset_button = Button((RESET_X,RESET_Y,RESET_WIDTH,RESET_HEIGHT),
            function, hover_color=PURPLE2 ,text="Reset")

    def render_font(self):
        self.tie_font = pygame.font.SysFont("Arial", 25)


    def render_score_text(self, score=(0,0,0)):
        self.x_text = (self.tie_font.render(str(score[0]), True, BLACK))
        self.o_text = (self.tie_font.render(str(score[1]), True, BLACK))
        self.games_text = (self.tie_font.render(str(score[2]), True, BLACK))


    def render_text(self):
        self.text3 = self.tie_font.render('G', True, BLACK)


    def blit_text(self, surface):
        surface.blit(self.text3, (400, 125))
        surface.blit(self.x_text,(200, 125))
        surface.blit(self.o_text,(325, 125))
        surface.blit(self.games_text,(425, 125))



    def get_event(self, event, *args):
        self.reset_button.get_event(event)


    def update(self, surface, score, *args):
        self.reset_button.update(surface)
        draw_x(surface, (150,125,30,30), offset=CLASSIC_X_OFFSET)
        draw_o(surface, (275,125,25,25))
        self.render_text()
        self.render_score_text(score)
        self.blit_text(surface)



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
    # H.create_scoreboard(surface)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            H.get_event(event)

        H.update(surface)
        pygame.display.update()
