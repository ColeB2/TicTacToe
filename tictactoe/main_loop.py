"""
main_loop.py - main pygame loop for tic tac toe program
State machine ideas and planning taken from
https://github.com/Mekire/pygame-mutiscene-template-with-movie
"""



class Main:
    def __init__(self):
        self.run = True


    def event_loop(self):
        """Main Event Loop processes events and passes them down to the state."""
        for event in pg.event.get()
        if event.type == pg.QUIT:
            self.run = False

        self.state.get_event(event)

    def main_loop(self):
        while self.run:
            pass
