"""
game_state.py - Main game state for a game of Tic Tac Toe
"""
import pygame
from pyVariables import *
from classic import ClassicTicTacToe



class GameState:
    def __init__(self):
        self.ruleset = "ClassicTicTacToe"
        self.get_gameset()
        self.run = True




    def handle_win(self):
        if self.GameSet.win_state == True:

    def get_gameset(self):
        if self.ruleset == "ClassicTicTacToe":
            self.GameSet = ClassicTicTacToe()


    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            self.GameSet.get_event(event)


    def main_loop(self):
        pygame.init()
        surface = pygame.display.set_mode((600,600))
        surface.fill((WHITE2))
        pygame.display.set_caption("Tic Tac Toe")

        while self.run:
            self.event_loop()
            self.GameSet.handle_ruleset()
            self.GameSet.update(surface)
            pygame.display.update()





if __name__ == '__main__':
    game = GameState()
    game.main_loop()
