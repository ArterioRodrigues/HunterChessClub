import string

alphanumerics = string.ascii_letters + string.digits


# error-handling class
class E:
    @staticmethod
    def match(given, param_name, expected, error):
        if given in expected:
            return given
        else:
            raise error(param=param_name, given=given, expected=expected)

    @staticmethod
    def is_int(given, param_name, error):
        try:
            if int(given) == float(given):
                return int(given)
            else:
                raise ValueError
        except ValueError:
            raise error(param=param_name, given=given, expected=int)

    @staticmethod
    def is_alphanum(given, param_name, error, extra_allowed_chars='_'):
        allowed = alphanumerics + extra_allowed_chars
        if len([c for c in given if c not in allowed]) == 0:
            return given
        else:
            raise error(param=param_name, given=given, expected="an alphanumeric string")


class CommHandler:
    def __init__(self):
        pass


class Tournament:
    def __init__(self, name, t_format='swiss', num_rounds=1, display_name=''):
        self.name = name
        self.t_format = E.match(t_format, 'format', ['swiss'], Tournament.InitializationError)
        self.num_rounds = E.is_int(num_rounds, 'num_rounds', Tournament.InitializationError)
        self.display_name = display_name
        if self.display_name:
            self.display_name = E.is_alphanum(display_name, 'display_name', Tournament.InitializationError)
        if not self.display_name:
            self.display_name = ''.join([c for c in self.name if c in alphanumerics])
            print(self.display_name)

    class Error(Exception):
        pass

    class InitializationError(Error):
        def __init__(self, param, given, expected=None, message=None):
            self.message = f'InitializationError: {given} passed to {param}.'
            if expected:
                self.message += f'\nExpected: {expected}'


if __name__ == '__main__':
    try:
        new_tourney = Tournament(' Example Tournament')
        print(new_tourney.display_name)
    except Tournament.InitializationError as e:
        print(e.message)

    try:
        new_tourney = Tournament(' Example Tournament', display_name='example_tournament')
        print(new_tourney.display_name)
    except Tournament.InitializationError as e:
        print(e.message)

    try:
        new_tourney = Tournament(' Example Tournament', display_name='example!tournament')
        print(new_tourney.display_name)
    except Tournament.InitializationError as e:
        print(e.message)
