def range(start:int, stop:int, step:int = 1):
    if not all(map(lambda x: isinstance(x, int), [start, stop, step])):
        raise TypeError('Allarguments must be integers.')

    if start <= stop and step < 0:
        raise ValueError('Stop must be greater than start when step is positive')

    if step == 0:
        raise ValueError("Step cannot be zero.")

    if start >= stop and step > 0:
        raise ValueError("Stop must be less than start when step is negative.")

    c = start
    while (c < stop and step > 0) or (c > stop and step < 0):
        yield c
        c += step

for i in range(1, 10, 3):
    print(i)



