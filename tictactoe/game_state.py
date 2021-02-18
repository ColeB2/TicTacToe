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
        self.H.create_reset_button(self.reset_function)

    """HUD"""
    def scoreboard(self):
        pass




    def handle_ruleset(self):
        self.GameSet.handle_ruleset()
        if self.GameSet.game_complete == True:
            self.handle_reset()

    def handle_reset(self):
        print(f"Play Again?")
        print(f"{self.GameSet.x_score} {self.GameSet.o_score} {self.GameSet.tie_score}")

    def reset_function(self):
        self.GameSet.board.clear_board()
        self.GameSet.game_complete = False
        self.GameSet.game_result = None
        self.GameSet.board.turn = 0
        print(f"reset")

    def handle_win_state(self):
        result = self.GameSet.win_state()
        if result == "WIN":
            print(f"{self.GameSet.board.last_symbol_placed} Wins")
            print("Handle Win State")
        elif result == "TIE":
            print("TIE")


    def get_gameset(self):
        if self.ruleset == "ClassicTicTacToe":
            self.GameSet = ClassicTicTacToe()


    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            self.GameSet.get_event(event)
            self.H.get_event(event)

    def update(self, surface, *args):
        self.GameSet.update(surface)
        self.H.update(surface, (self.GameSet.x_score, self.GameSet.o_score, self.GameSet.x_score+self.GameSet.o_score+self.GameSet.tie_score))
        self.handle_ruleset()


    def main_loop(self):
        self.event_loop()
        self.handle_ruleset()
        self.update(surface)
        pygame.display.update()





if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((DIS_X,DIS_Y))
    surface.fill((WHITE2))
    pygame.display.set_caption("Tic Tac Toe")


    game = GameState(ruleset="ClassicTicTacToe")
    while game.run:
        surface.fill(WHITE2)
        game.main_loop()
