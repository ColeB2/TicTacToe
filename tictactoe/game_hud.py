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
        self.hud_font = pygame.font.SysFont(None, 100)
        self.render_static_text()



    def create_reset_button(self, function=None):
        """Creates the reset button"""
        self.reset_button = Button((PA_X,PA_Y,PA_WIDTH,PA_HEIGHT),
            function, hover_color=PURPLE2 ,text="Play Again")


    """"Font/Text Rendering"""
    def render_dynamic_text(self, score=(0,0,0)):
        """Render all dynamic text objects that are subject to change."""
        self.x_text = (self.hud_font.render(str(self.score[0]), True, BLACK, BG_COLOR))
        self.o_text = (self.hud_font.render(str(self.score[1]), True, BLACK, BG_COLOR))
        self.games_text = (self.hud_font.render(str(self.score[2]), True, BLACK, BG_COLOR))


    def render_static_text(self):
        """Renders all static text that doesn't change."""
        self.text3 = self.hud_font.render('G', True, BLACK, BG_COLOR)
        self.turn_text = self.hud_font.render('Turn: ', True, BLACK, BG_COLOR)


    """Main Drawing/Display Functions"""
    def blit_text(self, surface):
        """Blits/Displays all text to the screen."""
        surface.blit(self.text3, (420, 520))
        surface.blit(self.x_text,(100, 520))
        surface.blit(self.o_text,(300, 520))
        surface.blit(self.games_text,(480, 520))
        surface.blit(self.turn_text, (150,80))


    def draw_turn_symbol(self, surface):
        """Displays the symbol of which players turn it is, in the turn section
        """
        if self.turn == 'O':
            draw_o(surface, (330,75,80,80))
        elif self.turn == 'X':
            draw_x(surface, (330,75,80,80), offset=CLASSIC_X_OFFSET)


    def draw_scoreboard_symbols(self, surface):
        """Draws the X/O used in the scoreboard to show X/O respective score
        value"""
        draw_x(surface, (0,500,100,100), offset=CLASSIC_X_OFFSET)
        draw_o(surface, (200,500,100,100))


    def draw_win_line(self, surface):
        if self.game_result == 'WIN':
            x1, y1, x2, y2 = self._calc_line_endpoints(self.winning_row)
            pygame.draw.line(surface, RED, (x1, y1), (x2, y2), 15)

    """Get Functions"""
    def get_score(self, score):
        """Gets the score values needed and calls the render dynamic text which
        uses the score values."""
        self.score = score
        self.render_dynamic_text()

    def get_turn(self, turn):
        """Gets the value which records which players turn it is."""
        self.turn = turn

    def get_game_result(self, result):
        self.game_result = result

    def get_winning_row(self,row):
        self.winning_row = row


    def _calc_line_endpoints(self, row):
        """Internal method used by the draw_win_line method. Calculates the end
        point x,y values of the win line so it can be drawn over top the proper
        row."""
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



    def get_event(self, event, *args):
        """HUDs main get event method"""
        self.reset_button.get_event(event)


    def _draw(self, surface):
        """Internal method, handles the the drawing of objects to the screen.
        Used in the main update method."""
        self.draw_scoreboard_symbols(surface)
        self.draw_win_line(surface)
        self.draw_turn_symbol(surface)
        self.blit_text(surface)


    def update(self, surface, *args, **kwargs):
        """HUDS main update methods"""
        self.reset_button.update(surface)
        self.get_turn(kwargs['turn'])
        self.get_score(kwargs['score'])
        self.get_game_result(kwargs['game_result'])
        self.get_winning_row(kwargs['winning_row'])
        self._draw(surface)



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
