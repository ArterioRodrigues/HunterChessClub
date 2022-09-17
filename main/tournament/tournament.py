from main.tournament.exceptions import ExceptionCatch as e
from main.tournament.color import Color, WHITE, BLACK, DRAW


class CommHandler:
    def __init__(self):
        pass


class Tournament:
    def __init__(self, name, t_format='swiss', num_rounds=1, display_name=''):
        self.name = name
        self.t_format = t_format
        self.num_rounds = num_rounds
        e.check_stack(error=Tournament.InitializationError, validations=[
            (self.name, 'name', 'is_alphanum', '_ '),
            (self.t_format, 'format', 'match', ['swiss']),
            (self.num_rounds, 'num_rounds', 'is_nonnegative_int')
            ])
        # e.is_alphanum(self.name, 'name', Tournament.InitializationError)
        # e.match(self.t_format, 'format', ['swiss'], Tournament.InitializationError)
        # e.is_int(self.num_rounds, 'num_rounds', Tournament.InitializationError)
        self.display_name = display_name
        if self.display_name:
            self.display_name = e.is_alphanum(display_name, 'display_name', Tournament.InitializationError)
        if not self.display_name:
            self.display_name = ''.join([c for c in self.name if c in e.alphanumerics])
        self.rounds = [[] for _ in range(num_rounds)]

    def set_rounds(self):
        pass

    class Error(Exception):
        pass

    class InitializationError(Error):
        def __init__(self, param, given, expected=None, message=None):
            self.message = f'Tournament.InitializationError: {given} passed to {param}.'
            if expected:
                self.message += f'\nExpected: {expected}\n'
            print(self.message)


class Round:
    def __init__(self, white, black, result):
        self.white = white
        self.black = black
        self.result = result


if __name__ == '__main__':
    try:
        new_tourney = Tournament(' Example Tournament')
        print(new_tourney.display_name)
    except Tournament.InitializationError as E:
        print(E.message)

    print('')

    try:
        new_tourney = Tournament(' Example Tournament', display_name='example_tournament', num_rounds=2.5)
        print(new_tourney.num_rounds)
    except Tournament.InitializationError as E:
        print(E.message)

    print('')

    try:
        new_tourney = Tournament(' Example Tournament', display_name='example_tournament', num_rounds=-90)
        print(new_tourney.num_rounds)
    except Tournament.InitializationError as E:
        print(E.message)

    try:
        new_tourney = Tournament(' Example Tournament', display_name='example_tournament', num_rounds=10, t_format='double_round_robin')
        print(new_tourney.format)
    except Tournament.InitializationError as E:
        print(E.message)

    # new_tourney = Tournament(' Example Tournament', display_name='example!tournament')
    # print(new_tourney.display_name)

    try:
        new_tourney = Tournament('Final Tournament', display_name='example!tournament')
        print(new_tourney.display_name)
    except Tournament.InitializationError as E:
        print(E.message)