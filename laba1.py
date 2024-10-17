SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"


print('№1 Флаг Литвы')


length = 30
height = 3
color = [3, 35, 160]


def draw_flag_line(color):
    for i in range(height):
        print(f"{SET_COLOR}{color}m{' ' * length}{END}")


if __name__ == "__main__":
    draw_flag_line(color[0])
    draw_flag_line(color[1])
    draw_flag_line(color[2])


print()
print('№2 Узор е')


def draw_pattern(color1 = 232, color2 = 231):
    print(f"{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*11}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*1}{END}")
    print(f"{SET_COLOR}{color1}m{' '*2}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*7}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*3}{END}")
    print(f"{SET_COLOR}{color1}m{' '*4}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*5}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*5}{END}")
    print(f"{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*1}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*7}{END}")
    print(f"{SET_COLOR}{color1}m{' '*8}{SET_COLOR}{color2}m{' '*1}{SET_COLOR}{color1}m{' '*9}{END}")


if __name__ == "__main__":
    for i in range(6):
        draw_pattern()


print()
print('№3 График функции y = |x| (1 четверть, где х>0, y>0)')


def draw_graphic(color3 = 200):
        for i in range(9):
            print(9-i, f'{'  '*(9-i-1)}{SET_COLOR}{color3}m{"  "}{END}')


if __name__ == "__main__":
     draw_graphic()
     print('0 1 2 3 4 5 6 7 8 9')


print()
print('№4 Процентная диаграмма')


def draw_percentage_diagram(filename, color4 = 129, color5 = 51):


    with open(filename, 'r') as file:
        numbers = [float(line.strip()) for line in file.readlines()]


    chet = [abs(numbers[i]) for i in range(len(numbers)) if i % 2 == 0]
    nechet = [abs(numbers[i]) for i in range(len(numbers)) if i % 2 != 0]


    spm_chet = sum(chet) / len(chet) if chet else 0
    spm_nechet = sum(nechet) / len(nechet) if nechet else 0


    total = spm_chet + spm_nechet
    if total == 0:
        chet_percent = nechet_percent = 0
    else:
        chet_percent = (spm_chet / total) * 100
        nechet_percent = (spm_nechet / total) * 100


    chetnye = int(chet_percent // 2) * ' '
    nechetnye = int(nechet_percent // 2) * ' '    


    print(f"Числа на чётных позициях: {chet_percent:.2f}% | {SET_COLOR}{color4}m{chetnye}{END}")
    print(f"Числа на нечётных позициях: {nechet_percent:.2f}%|{SET_COLOR}{color5}m{nechetnye}{END}")


if __name__=='__main__':
    draw_percentage_diagram('sequence.txt')  
