"""
game_state.py - Main game state for a game of Tic Tac Toe
"""
from buttons import Button
from classic import ClassicTicTacToe
from game_hud import HUD
import pygame
from pyVariables import *




class GameState:
    def __init__(self, ruleset):
        self.ruleset = ruleset
        self.get_gameset()

        self.run = True
        self.reset = False

        self.H = HUD()
        self.H.create_reset_button(self.reset_button_function)



    def reset_button_function(self):
        """Gameset reset function. Used to reset the board to start a new game"""
        self.GameSet.board.clear_board()
        self.GameSet.game_complete = False
        self.GameSet.game_result = None
        self.GameSet.board.turn = 0
        self.GameSet.players = list(reversed(self.GameSet.players))


    def get_gameset(self):
        """Used to get the ruleset. Set up to add rulesets in the future"""
        if self.ruleset == "ClassicTicTacToe":
            self.GameSet = ClassicTicTacToe()


    def event_loop(self):
        """The Main Event Loop for the game state"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            self.GameSet.get_event(event)
            self.H.get_event(event)

    def update(self, surface, *args):
        """Main update method for game state"""
        self.GameSet.update(surface)
        self.H.update(surface, score=(self.GameSet.x_score,
            self.GameSet.o_score,
            self.GameSet.x_score+self.GameSet.o_score+self.GameSet.tie_score),
            turn=self.GameSet.board.click_symbol,
            game_result=self.GameSet.game_result,
            winning_row = self.GameSet.winning_row,)


    def main_loop(self, surface):
        """Game main loop. Used inside of a while loop, calls the event loop,
        update method, the ruleset as well as pygame.display.update."""
        self.event_loop()
        self.GameSet.handle_ruleset()
        self.update(surface)





if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((DIS_X,DIS_Y))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Tic Tac Toe")


    game = GameState(ruleset="ClassicTicTacToe")
    while game.run:
        surface.fill(BG_COLOR)
        game.main_loop(surface)
        pygame.display.update()
