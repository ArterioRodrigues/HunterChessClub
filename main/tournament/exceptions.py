import string


class ExceptionCatch:
    alphanumerics = string.ascii_letters + string.digits

    @staticmethod
    def is_in(given, param_name, error, expected, return_var=True):
        if given in expected:
            if return_var:
                return given
        else:
            raise error(param=param_name, given=given, expected=f'a value in {expected}')

    @staticmethod
    def is_str(given, param_name, error, return_var=True):
        if type(given) == str:
            if return_var:
                return given
        else:
            raise error(param=param_name, given=given, expected=str)

    @staticmethod
    def is_int(given, param_name, error, return_var = True):
        try:
            if int(given) == float(given):
                if return_var:
                    return int(given)
            else:
                raise ValueError
        except ValueError:
            raise error(param=param_name, given=given, expected=int)

    @staticmethod
    def is_nonnegative_int(given, param_name, error, return_var=True):
        given = ExceptionCatch.is_int(given, param_name, error, True)
        if given > 0:
            if return_var:
                return given
        else:
            raise error(param=param_name, given=given, expected="a non-negative integer.")

    @staticmethod
    def is_alphanum(given, param_name, error, extra_allowed_chars='_', allow_empty=False, return_var=True):
        allowed = ExceptionCatch.alphanumerics + extra_allowed_chars
        if allow_empty and given == '':
            if return_var:
                return given
        if type(given) == str and len([c for c in given if c not in allowed]) == 0:
            if return_var:
                return given
        else:
            raise error(param=param_name, given=given, expected="an alphanumeric string")

    @staticmethod
    def check_stack(error, validations):
        for validation in validations:
            given, param_name, exception_to_catch = validation[:3]
            if exception_to_catch is ExceptionCatch.is_in:
                if len(validation) >= 4:
                    ExceptionCatch.is_in(given, param_name, error, validation[3], return_var=False)
            elif exception_to_catch is ExceptionCatch.is_alphanum:
                if len(validation) < 4:
                    ExceptionCatch.is_alphanum(given, param_name, error, return_var=False)
                else:
                    ExceptionCatch.is_alphanum(given, param_name, error, extra_allowed_chars=validation[3],
                                               return_var=False)
            else:
                exception_to_catch(given, param_name, error, return_var=True)
        return True
