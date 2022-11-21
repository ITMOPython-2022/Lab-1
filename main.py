def esc(code):
    return f'\u001b[{code}m'


def flag_cz():
    for i in range(6):
        if i <= 2:
            # print(BLUE + '  ' * (2 * i + 2) + WHITE + '  ' * (14 - 2 * i) + END)
            print(f'{BLUE}{"  " * (2 * i + 2)}{WHITE}{"  " * (14 - 2 * i)}{END}')
        else:
            print(BLUE + '  ' * (12 - 2 * i) + RED + '  ' * (4 + 2 * i) + END)


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = st * (8 - i) + st
            if i == 9:
                array_in[i][j] = j
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for j in range(10):
            if abs(array_fi[i][0] - res[9 - j]) < st:
                for k in range(9):
                    if 8 - k == j:
                        array_fi[i][k + 1] = 1
    return array_fi


def draw_plot(array_pl):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + '\t' + str(int(array_pl[i][j])) + '\t'
            if array_pl[i][j] == 0:
                line += '  '
            if array_pl[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '\t0\t1 2 3 4 5 6 7 8 9 ' + END)


RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
END = esc(0)

array_plot = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i ** 3
step = round(abs(result[0] - result[9]) / 9, 1)
print(step)

array_init(array_plot, step)
array_fill(array_plot, result, step)

draw_plot(array_plot)

# for i in range(10):
#     print(array_plot[i])
flag_cz()