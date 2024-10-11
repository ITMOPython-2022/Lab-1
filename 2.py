START_GAP = 10

gap = 10
flag = 0

spot = f'\x1b[48;5;{1}m{" "}\x1b[0m'

for i in range(11):
    space = (START_GAP - gap) * 2
    space *= ' '

    if gap == 0:
        flag = 1

    empty = ' ' * gap
    stroka = empty + spot + space + spot + empty

    print(stroka * 4)

    if flag != 1:
        gap -= 2
    else:
        gap += 2