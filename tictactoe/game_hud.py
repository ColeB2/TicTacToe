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
        self.reset_button = Button((PA_X,PA_Y,PA_WIDTH,PA_HEIGHT),
            function, hover_color=PURPLE2 ,text="Play Again")

    def render_font(self):
        self.tie_font = pygame.font.SysFont(None, 100)


    def render_score_text(self, score=(0,0,0)):
        self.x_text = (self.tie_font.render(str(score[0]), True, BLACK))
        self.o_text = (self.tie_font.render(str(score[1]), True, BLACK))
        self.games_text = (self.tie_font.render(str(score[2]), True, BLACK))


    def render_text(self):
        self.text3 = self.tie_font.render('G', True, BLACK)
        self.turn_text = self.tie_font.render('Turn: ', True, BLACK)


    def blit_text(self, surface):
        surface.blit(self.text3, (420, 520))
        surface.blit(self.x_text,(100, 520))
        surface.blit(self.o_text,(300, 520))
        surface.blit(self.games_text,(480, 520))
        surface.blit(self.turn_text, (150,90))


    def display_turn(self, surface, turn):
        if turn == 'O':
            draw_o(surface, (310,85,80,80))
        elif turn == 'X':
            draw_x(surface, (300,85,80,80), offset=CLASSIC_X_OFFSET)



    def get_event(self, event, *args):
        self.reset_button.get_event(event)


    def update(self, surface, score, turn, *args):
        self.reset_button.update(surface)
        draw_x(surface, (0,500,100,100), offset=CLASSIC_X_OFFSET)
        draw_o(surface, (200,500,100,100))
        self.render_text()
        self.render_score_text(score)
        self.display_turn(surface, turn)
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
    turn = 'X'
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            H.get_event(event)

        surface.fill((WHITE2))
        H.update(surface, (6,4,10), turn=turn)
        pygame.display.update()
