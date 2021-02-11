"""
main_loop.py - main pygame loop for tic tac toe program
"""
import pygame
from pyVariables import *
from classic import ClassicTicTacToe



class MainLoop:
    def __init__(self):
        self.GameSet = None
        self.run = True
        self.player_turn = 'X'





    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            self.GameSet.get_event(event, self.player_turn)

    def main_loop(self):
        while run:
            self.GameSet.update(surface)
            pygame.display.update()





if __name__ == '__main__':
