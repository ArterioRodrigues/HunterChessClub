from main.tournament.exceptions import ExceptionCatch as e

class Player:
    def __init__(self, display_name, elo='-1', name=None, is_dummy=False, pool=None):
        self.display_name = display_name
        self.elo = -1 if elo == '-1' else elo
        self.name = name
        self.is_dummy = is_dummy
        self.pool = pool
        if elo is not None:
            e.is_int(elo, 'display_name', Player.InitializationError)
        if self.name is None:
            self.name = e.is_str(display_name, 'display_name', Player.InitializationError)[:2]
        e.check_stack(error=Player.InitializationError, validations=[
            (self.name, 'name', 'is_alphanum'),
            (self.elo, 'elo', 'is_int')
        ])
        self.elo = None if elo == -1 else elo

    class Error(Exception):
        pass

    class InitializationError(Error):
        def __init__(self, param, given, expected=None, message=None):
            self.message = f'Player.InitializationError: "{given}" passed to {param}.'
            if expected:
                self.message += f'\nExpected: {expected}\n'