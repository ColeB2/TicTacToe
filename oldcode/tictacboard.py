'''
Classes for Tic Tac Toe Board and individual Squares
2nd attempt - Modularize
'''
class Board:
    def __init__(self):
        #self.width = width
        #self.height = height
        self.board = [
        [Square((0,0), ' '),Square((1,0), ' '),Square((2,0), ' ')],
        [Square((0,1), ' '),Square((1,1), ' '),Square((2,1), ' ')],
        [Square((0,2), ' '),Square((1,2), ' '),Square((2,2), ' ')]
        ]


    def clear_board(self):
        for i in range(len(self.board)):
            for square in self.board[i]:
                square.change_state(' ')

    def three_row(self):
        '''Checks to see if their are 3 of the same pieces in a Row
        returns True, Value of the winning piece
        '''
        #Check Columns
        for i in range(len(self.board)):
            if (self.board[0][i].state == \
                self.board[1][i].state == \
                self.board[2][i].state):
                return True, self.board[0][i].state

        #Check Rows
        for i in range(len(self.board)):
            if (self.board[i][0].state == \
                self.board[i][1].state == \
                self.board[i][2].state):
                return True, self.board[i][0].state

        #Check diagonals
        if (self.board[0][0].state == \
            self.board[1][1].state == \
            self.board[2][2].state):
            return True, self.board[0][0].state

        if (self.board[0][2].state == \
            self.board[1][1].state == \
            self.board[2][0].state):
            return True, self.board[0][2].state

class Square:
    def __init__(self, position=(0,0), state=' '):
        self.pos = position
        self.state = state


    def change_state(self, state):
        '''Changes state from blank, to either x or o'''
        self.state = state
