'''
tictac.py - Tic Tac Toe OOP impementation
using pygame to display
'''

import pygame
from pygame.locals import *
import sys

##COLORS
from pyColor import *
_BGCOLOR = WHITE


pygame.init()

FPS = 15 #frames per second setting
fps_clock = pygame.time.Clock()

DIS_X = 500
DIS_Y = 500
DIS_SIZE = (DIS_X, DIS_Y)
DISPLAYSURF = pygame.display.set_mode(DIS_SIZE)

pygame.display.set_caption('Tic Tac Toe')

'''CLASSES'''
class Board:
    def __init__(self, display_width, display_height):
        self.width = display_width
        self.height = display_height
        self.board = [
        [Square((0,0), ' '),Square((1,0), ' '),Square((2,0), ' ')],
        [Square((0,1), ' '),Square((1,1), ' '),Square((2,1), ' ')],
        [Square((0,2), ' '),Square((1,2), ' '),Square((2,2), ' ')]
        ]

    def display_grid(self):
        '''Displays the playing grid using pygame.draw.line()'''
        ##Gridlines
        ##TOP DOWN
        pygame.draw.line(DISPLAYSURF, BLACK,
                (0+200, 0+100), (0+200, DIS_Y-100), 5)
        pygame.draw.line(DISPLAYSURF, BLACK,
                (DIS_X-200, 0+100),  (DIS_X-200, DIS_Y-100), 5)
        ##LEFT-RIGHT LINES
        pygame.draw.line(DISPLAYSURF, BLACK,
                (0+100, 0+200), (DIS_X-100, 0+200), 5)
        pygame.draw.line(DISPLAYSURF, BLACK,
                (0+100, DIS_Y-200), (DIS_X-100, DIS_Y-200), 5)

        ##box around Grid
        pygame.draw.line(DISPLAYSURF, BLACK,
                (0+100, 0+100), (DIS_X-100, 0+100), 5)
        pygame.draw.line(DISPLAYSURF, BLACK,
                (0+100, 0+100), (0+100, DIS_Y-100), 5)
        pygame.draw.line(DISPLAYSURF, BLACK,
                (DIS_X-100, 0+100), (DIS_X-100, DIS_Y-100), 5)
        pygame.draw.line(DISPLAYSURF, BLACK,
                (DIS_X-100, DIS_Y-100), (0+100, DIS_Y-100), 5)

    def display_squares(self):
        for i in range(len(self.board)):
            for square in self.board[i]:
                square.display()


    def clear_board(self):
        for i in range(len(self.board)):
            for square in self.board[i]:
                square.state = ' '

    def three_row(self, square1, square2, square3):
        if square1.state == square2.state == square3.state and \
                square1.state != ' ':
            return True
        else:
            return False


class Square:
    def __init__(self, position=(0,0), state=' '):
        self.pos = position
        self.state = state
        self.corners = [0,0,0,0]
        self.calc_corners()

    def calc_corners(self):
        '''
        calculates pixels placement of each corner of the square
        Used for mouse controls
        self.corners[X1, X2, Y1, Y2]
        '''
        self.corners[0] = self.pos[0]*100 + 100
        self.corners[1] = self.pos[0]*100 + 200
        self.corners[2] = self.pos[1]*100 + 100
        self.corners[3] = self.pos[1]*100 + 200

    def display(self):
        '''
        Display piece on board, based on position
        sc - scale - used to move piece based on position
        os - offset - used to offset piece in center of grid space
        OS - offset - used to place the Grid: DISPLAYSURF - GRIDSIZE
        '''
        GRID_SIZE = 300
        GRID_X = 300
        GRID_Y = 300
        OS = (DIS_X - GRID_SIZE) / 2
        sc = (GRID_SIZE)/3
        os = ((GRID_SIZE)/3)/4
        X = (GRID_X)/3 - os
        Y = (GRID_Y)/3 - os
        if self.state == 'X':
            pygame.draw.line(DISPLAYSURF, BLACK,
                    (sc*self.pos[0] + os + OS,
                     sc*self.pos[1] + os + OS),
                    (sc*self.pos[0] + X + OS,
                     sc*self.pos[1] + Y + OS),5)
            pygame.draw.line(DISPLAYSURF, BLACK,
                    (sc*self.pos[0] + os + OS,
                     sc*self.pos[1] + Y + OS),
                    (sc*self.pos[0] + X + OS,
                     sc*self.pos[1] + os + OS),5)
        elif self.state == 'O':
            pygame.draw.circle(DISPLAYSURF, RED,
                    (int(sc * self.pos[0] + 2*os + OS),
                     int(sc * self.pos[1] + 2*os + OS)), 30, 5)
        else:
            pass


class Game:
    def __init__(self):
        self.b = Board(DIS_X, DIS_Y)
        self.b.clear_board()
        self.turn = ['O', 'X']
        self.turnnum = 0
        self.turn_num = 1
        self.game_over = False
        self.score = ['X', 0, 'O', 0, False]

    def play_game(self):
        self.b.display_grid()
        self.b.display_squares()
        if not self.game_over:
            self.place_piece()
            self.mouse_controls()
            self.display_turn()

        self.check_win()
        self.reset_button()
        self.display_score()



    def place_piece(self):
        '''
        Places pieces using numpad as input
        789 - Top Row || 456 - Middle Row || 123 - Bottom Row
        '''
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_KP7)  and self.b.board[0][0].state == ' ':
                self.b.board[0][0].state = self.turn[self.turn_num]
                self.handle_turn()
            elif (event.key == pygame.K_KP8)and self.b.board[0][1].state == ' ':
                self.b.board[0][1].state = self.turn[self.turn_num]
                self.handle_turn()
            elif (event.key == pygame.K_KP9)and self.b.board[0][2].state == ' ':
                self.b.board[0][2].state = self.turn[self.turn_num]
                self.handle_turn()
            elif (event.key == pygame.K_KP4)and self.b.board[1][0].state == ' ':
                self.b.board[1][0].state = self.turn[self.turn_num]
                self.handle_turn()
            elif (event.key == pygame.K_KP5)and self.b.board[1][1].state == ' ':
                self.b.board[1][1].state = self.turn[self.turn_num]
                self.handle_turn()
            elif (event.key == pygame.K_KP6)and self.b.board[1][2].state == ' ':
                self.b.board[1][2].state = self.turn[self.turn_num]
                self.handle_turn()
            elif (event.key == pygame.K_KP1)and self.b.board[2][0].state == ' ':
                self.b.board[2][0].state = self.turn[self.turn_num]
                self.handle_turn()
            elif (event.key == pygame.K_KP2)and self.b.board[2][1].state == ' ':
                self.b.board[2][1].state = self.turn[self.turn_num]
                self.handle_turn()
            elif (event.key == pygame.K_KP3)and self.b.board[2][2].state == ' ':
                self.b.board[2][2].state = self.turn[self.turn_num]
                self.handle_turn()

    def mouse_controls(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for row in range(len(self.b.board)):
            for square in self.b.board[row]:
                if square.corners[0] < mouse[0] < square.corners[1] and \
                    square.corners[2] < mouse[1] < square.corners[3]:
                    if square.state == ' ':
                        if click[0] == 1:
                            square.state = self.turn[self.turn_num]
                            self.handle_turn()






    def reset_button(self):
        '''Play Again Button, triggers only after game ends'''
        #Reset Button Prompt
        if self.game_over == True:
            font2 = pygame.font.SysFont(None, 25)
            text2 = font2.render('Press Spacebar to Play Again', True, BLACK)
            text_rect2 = text2.get_rect(center=(DIS_X/2,90))
            DISPLAYSURF.blit(text2, (text_rect2))
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_SPACE):
                self.b.clear_board()
                self.turnnum = 0
                self.turn_num = 1
                self.game_over = False
                self.score[4] = False


    def handle_turn(self):
        '''
        Handles turn order using turnnum and turn_num variables
        self.turn_num = 0 or 1, 0 = O turn, 1 = X turn
        self.turnnum = number of turns elapsed during game
        '''
        if self.turnnum % 2 == 0:
            self.turn_num = 0
        elif self.turnnum % 2 != 0:
            self.turn_num = 1
        self.turnnum += 1

    def display_turn(self):
        font = pygame.font.SysFont(None, 100)
        text = font.render('TURN: ', True, BLACK)
        DISPLAYSURF.blit(text, (0,0))
        if self.turn[self.turn_num] == 'X':
            pygame.draw.line(DISPLAYSURF, BLACK,
                    (DIS_X/2 - 25,
                     0+5),
                    (DIS_X/2 + 25,
                     0+55),5)
            pygame.draw.line(DISPLAYSURF, BLACK,
                    (DIS_X/2 - 25,
                     0+55),
                    (DIS_X/2 + 25,
                     0+5),5)
        elif self.turn[self.turn_num] == 'O':
            pygame.draw.circle(DISPLAYSURF, RED,
                    (int(DIS_X/2),
                     int(0+35)), 30, 5)

    def display_score(self):
        font = pygame.font.SysFont(None, 50)
        text = font.render('SCORE:', True, BLACK)
        DISPLAYSURF.blit(text, (0, DIS_Y-99))

        pygame.draw.line(DISPLAYSURF, BLACK,
                (5, int(DIS_Y-55)),(55, int(DIS_Y-5)),5)
        pygame.draw.line(DISPLAYSURF, BLACK,
                (5, int(DIS_Y-5)),(55, int(DIS_Y-55)),5)
        pygame.draw.circle(DISPLAYSURF, RED,
                (int(DIS_X/2), int(DIS_Y-35)), 30, 5)
        DISPLAYSURF.blit(text, (0, DIS_Y-99))
        #values
        font2 = pygame.font.SysFont(None, 100)
        text1 = font2.render(' :' + str(self.score[1]), True, BLACK)
        text2 = font2.render(':' + str(self.score[3]), True, BLACK)
        DISPLAYSURF.blit(text1, (5+50, int(DIS_Y-65)))
        DISPLAYSURF.blit(text2, (int(DIS_X/2+50), int(DIS_Y-65)))

    def score_event(self, winner):
        '''Displays win message at top of screen, and handles score update'''
        font = pygame.font.SysFont(None, 100)
        text = font.render(str(winner) + ' WINS!', True, BLACK)
        DISPLAYSURF.blit(text, (0,0))
        if self.score[4] == False:
            if winner == 'X':
                self.score[1] += 1
                self.score[4] = True
            elif winner == 'O':
                self.score[3] += 1
                self.score[4] = True

    def check_win(self):
        if self.turnnum >= 5:
            #check COLUMNS
            for i in range(len(self.b.board)):
                if self.b.three_row(self.b.board[0][i],
                    self.b.board[1][i], self.b.board[2][i]):
                    self.score_event(self.b.board[0][i].state)
                    self.game_over = True
                    pygame.draw.line(DISPLAYSURF, RED,
                     (i * 100 + 150, 0 + 110),
                     (i * 100 + 150, DIS_Y - 110), 10)
            #check ROWS
            for i in range(len(self.b.board)):
                if self.b.three_row(self.b.board[i][0],
                   self.b.board[i][1], self.b.board[i][2]):
                    self.score_event(self.b.board[i][0].state)
                    self.game_over = True
                    pygame.draw.line(DISPLAYSURF, RED,
                    (0 + 110, i * 100 + 150),
                    (DIS_X - 110, i * 100 + 150), 10)
            #check diagonals
            if self.b.three_row(self.b.board[0][0], self.b.board[1][1],
                    self.b.board[2][2]):
                    self.score_event(self.b.board[0][0].state)
                    self.game_over = True
                    pygame.draw.line(DISPLAYSURF, RED,
                    (0+110, 0 + 110),
                    (DIS_X-110, DIS_Y-110),10)
            if self.b.three_row(self.b.board[0][2], self.b.board[1][1],
                    self.b.board[2][0]):
                    self.score_event(self.b.board[0][2].state)
                    self.game_over = True
                    pygame.draw.line(DISPLAYSURF, RED,
                    (0 + 110, DIS_Y - 110),
                    (DIS_X - 110, 0 + 110),10)
        if self.turnnum == 9 and self.score[4] == False:
            self.game_over = True
            font = pygame.font.SysFont(None, 100)
            text = font.render('DRAW!', True, BLACK)
            text_rect = text.get_rect(center=(DIS_X/2,50))
            DISPLAYSURF.blit(text, (text_rect))



g = Game()

while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(_BGCOLOR)
    g.play_game()

    pygame.display.update()
