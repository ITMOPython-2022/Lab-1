def plot_function(func, start, end):


    spot1 = f'\x1b[48;5;{1}m{" "}\x1b[0m'
    spot2 = f'\x1b[48;5;{2}m{" "}\x1b[0m'
    AXIS = f'\x1b[48;5;{1}m{" "}\x1b[0m'
    GRAPH = f'\x1b[48;5;{2}m{" "}\x1b[0m'


    y_values = {}


    for x in range(start, end + 1):
        y = func(x)
        y_values[y] = x

    # Определяем максимальное значение y
    max_y = max(y_values.keys())

    # Строим график
    for y in range(max_y, 0, -1):
        if y in y_values:
            x = y_values[y]
            print(y, ' ' * (3 - len(str(y))), spot1 * (x - 1) + spot2)

    print(0, ' ', spot2 + spot1 * (end - start), 'x')
    print('   ', ' '.join(str(i) for i in range(start, end + 1)))


plot_function(lambda x: x**2, 0, 10)