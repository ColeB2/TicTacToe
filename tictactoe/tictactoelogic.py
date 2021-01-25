from tictacboard import Board, Square

class Game:
    def __init__(self):
        self.b = Board()
        self.b.clear_board()
        self.player_turn = ['O', 'X']
        self.turn = 1 #1 or 0 = 'O' or 'X'
        self.turnnum = 0
        self.game_over = False
        self.score = ['X', 0 , 'O', 0, False]

    def play_game(self):
        pass

    def reset(self):
        if self.game_over == True:
            self.b.clear_board()
            self.turnnum = 0
            self.turn = 1
            self.game_over = False
            self.score[4] = False

    def place_piece(self):
        pass

    def turn_logic(self):
        '''Handles Turn Logic'''
        if self.turnnum % 2 == 0:
            self.turn = 0
        else:
            self.turn = 1
        self.turnnum += 1


    def handle_score_event(self, winner):
        '''Handles a scoring event (A win for either side)''''
        if self.score[4] == False:
            if winner == 'X':
                self.score[1] += 1
                self.score[4] = True
            if winner == 'O':
                self.score[3] += 1
                self.score[4] = True


    def check_win(self):
        '''Checks to see if their is a winner'''
        if self.turnnum >= 5:
            if self.b.three_row():
                self.game_over = True
                self.handle_score_event(self.b.three_row()[1])
        elif self.turnnum == 9 and self.score[4] == False:
            self.game_over = True
