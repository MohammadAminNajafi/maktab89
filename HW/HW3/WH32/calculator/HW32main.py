from calculator.logic.HW32parse import *
from calculator.logic.HW32calc import *
from HW32exceptions import *

f = ''
while True:
    inp = input()
    if inp != 'exit':
        try:
            invalid_format_exception_checker(c(inp))
            invalid_number_exception_checker(c(inp))
            invalid_operator_exception_checker(c(inp))
            print(y(c(inp)))
            math = y(c(inp))
            with open('r.txt', 'a+') as f:
                f.write(inp)
                f.write(('\t'))
                f.write(str(math))
                f.write('\n\n')

        except (ZeroDivisionError, AssertionError) as e:
            E = e
            print(e)
            with open('r.txt', 'a+') as f:
                f.write(inp)
                f.write(('\t'))
                f.write((str(E)))
                f.write('\n\n')
    if inp == 'exit':
        break

