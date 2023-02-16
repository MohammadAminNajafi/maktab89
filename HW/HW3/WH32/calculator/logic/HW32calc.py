def y(x):
    if x[1] == '+':
        return int(x[0]) + int(x[2])

    if x[1] == '-':
        return int(x[0]) - int(x[2])

    if x[1] == '*':
        return int(x[0]) * int(x[2])

    if x[1] == '/':
        return int(x[0]) / int(x[2])