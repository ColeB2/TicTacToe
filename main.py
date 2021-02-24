import os, sys
sys.path.append(os.path.join('.', 'tictactoe'))
import pygame
from pyVariables import *
from game_state import GameState

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
