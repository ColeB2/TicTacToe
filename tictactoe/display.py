"""
display-py - The pygame display for tic tac toe game implemented using Python
    and Pygame
"""

import pygame as pg
from pyVariables import *


"""Pygame Code to set up Display Surface"""
pygame.init()
surface = pygame.display.set_mode(DIS_SIZE)
surface.fill(WHITE2)
pygame.display.set_Caption('Tic Tac Toe')


class TicTacToe:
    def __init__(self):
        pass


    def main_loop(self):

if __name__ == '__main__':
    T = TicTacToe()
    T.main_loop()
