def invalid_format_exception_checker(z):
    assert len(z) == 3, 'Invalid Format Error'


def invalid_number_exception_checker(z):
        assert z[0].isdigit() and z[2].isdigit(), 'Invalid Number Error'


def invalid_operator_exception_checker(z):
        assert z[1] in ["+", "-", "*", "/"], 'Invalid Operator Error'


