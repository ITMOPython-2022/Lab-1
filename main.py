RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

'''for i in range(6):
    if i < 3:
        print(f'{BLUE}{"  " * (2 * i + 2)}{WHITE}{"  " * (14 - 2 * i)}{END}')
    else:
        print(f'{BLUE}{"  " * (12 - 2 * i)}{RED}{"  " * (4 + 2 * i)}{END}')'''


plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i ** 3

step = round(abs(result[0] - result[9]) / 9, 2)
print(step)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')

for i in range(10):
    #print(plot_list[i])
    pass

file = open('sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))
file.close()
print(list)