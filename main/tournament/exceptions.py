import string


class ExceptionCatch:
    alphanumerics = string.ascii_letters + string.digits

    @staticmethod
    def match(given, param_name, expected, error, return_var = True):
        if given in expected:
            if return_var:
                return given
        else:
            raise error(param=param_name, given=given, expected=expected)

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
            given = validation[0]
            param_name = validation[1]
            error_type = validation[2].lower()
            if error_type == 'match' and len(validation) >= 4:
                ExceptionCatch.match(given, param_name, validation[3], error, return_var=False)
            elif error_type in (str, 'str', 'string', 'is_str'):
                ExceptionCatch.is_str(given, param_name, error, return_var=False)
            elif error_type in (int, 'int', 'integer', 'is_int'):
                ExceptionCatch.is_int(given, param_name, error, return_var=False)
            elif error_type in ('is_nn_i', 'is_nonneg_int', 'is_nonnegative_int', 'is_nonnegative_integer'):
                ExceptionCatch.is_nonnegative_int(given, param_name, error, return_var=False)
            elif error_type in ('an', 'alphanum', 'alphanumeric', 'is_alphanum', 'is_alphanumeric'):
                if len(validation) < 4:
                    ExceptionCatch.is_alphanum(given, param_name, error, return_var=False)
                else:
                    ExceptionCatch.is_alphanum(given, param_name, error, extra_allowed_chars=validation[3], return_var=False)
        return True
