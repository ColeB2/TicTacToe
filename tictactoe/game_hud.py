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
        self.render_text()


    def create_reset_button(self, function=None):
        self.reset_button = Button((PA_X,PA_Y,PA_WIDTH,PA_HEIGHT),
            function, hover_color=PURPLE2 ,text="Play Again")

    def render_font(self):
        self.tie_font = pygame.font.SysFont(None, 100)


    def render_score_text(self, score=(0,0,0)):
        self.x_text = (self.tie_font.render(str(score[0]), True, BLACK, BG_COLOR))
        self.o_text = (self.tie_font.render(str(score[1]), True, BLACK, BG_COLOR))
        self.games_text = (self.tie_font.render(str(score[2]), True, BLACK, BG_COLOR))


    def render_text(self):
        self.text3 = self.tie_font.render('G', True, BLACK, BG_COLOR)
        self.turn_text = self.tie_font.render('Turn: ', True, BLACK, BG_COLOR)


    def blit_text(self, surface):
        surface.blit(self.text3, (420, 520))
        surface.blit(self.x_text,(100, 520))
        surface.blit(self.o_text,(300, 520))
        surface.blit(self.games_text,(480, 520))
        surface.blit(self.turn_text, (150,80))


    def display_turn(self, surface, turn):
        if turn == 'O':
            draw_o(surface, (330,75,80,80))
        elif turn == 'X':
            draw_x(surface, (330,75,80,80), offset=CLASSIC_X_OFFSET)


    def calc_line_endpoints(self, row):
        offset = int(row[0].rect[2]/3 )
        if row[0].rect[0] == row[-1].rect[0]:
            """If row x values are equal, ie vertical line"""
            x1 = row[0].rect[0] + row[0].rect[2]/2
            y1 = row[0].rect[1] + row[0].rect[3]/2 - offset
            x2 = row[-1].rect[0]  + row[0].rect[2]/2
            y2 = row[-1].rect[1] + row[0].rect[3]/2 + offset
        elif row[0].rect[1] == row[-1].rect[1]:
            """If row y values are equal, ie horizontal line"""
            x1 = row[0].rect[0] + row[0].rect[2]/2 - offset
            y1 = row[0].rect[1] + row[0].rect[3]/2
            x2 = row[-1].rect[0] + row[0].rect[2]/2 + offset
            y2 = row[-1].rect[1] + row[0].rect[3]/2
        elif row[0].rect[0] < row[-1].rect[0]:
            """If x1 < x2 ie left-right, top-down diagonal"""
            x1 = row[0].rect[0] + offset
            y1 = row[0].rect[1] + offset
            x2 = row[-1].rect[0] + row[0].rect[2] - offset
            y2 = row[-1].rect[1] + row[0].rect[3] - offset
        elif row[0].rect[0] > row[-1].rect[0]:
            """Other diagonal"""
            x1 = row[0].rect[0] + row[0].rect[2]/2 + offset/2
            y1 = row[0].rect[1] + row[0].rect[2]/2 - offset/2
            x2 = row[-1].rect[0] + row[0].rect[2]/2 - offset/2
            y2 = row[-1].rect[1] + row[0].rect[2]/2 + offset/2
        return x1, y1, x2, y2


    def draw_win_line(self, surface, row):
        x1, y1, x2, y2 = self.calc_line_endpoints(row)
        pygame.draw.line(surface, RED,
            (x1, y1), (x2, y2), 15)


    def get_event(self, event, *args):
        self.reset_button.get_event(event)


    def update(self, surface, score, turn, *args):
        self.reset_button.update(surface)
        draw_x(surface, (0,500,100,100), offset=CLASSIC_X_OFFSET)
        draw_o(surface, (200,500,100,100))
        # self.render_text()
        self.render_score_text(score)
        self.display_turn(surface, turn)
        self.blit_text(surface)



if __name__ == "__main__":
    import pygame

    pygame.init()
    surface = pygame.display.set_mode((DIS_X,DIS_Y))
    surface.fill((BG_COLOR))
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

        surface.fill((BG_COLOR))
        H.update(surface, (6,4,10), turn=turn)
        pygame.display.update()
