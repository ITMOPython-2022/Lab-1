# флаг
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
SET_COLOR = "\x1b[48;5;"


print ('#1 Флаг Франции')

height = (6)
length = (30)


def draw_flag_line():
    for i in range (height):
            print(f'{BLUE}{"  " * (length // 3)}',f'{WHITE}{"  " * (length // 3)} ',f'{RED}{"  " * (length // 3)}{END}')


if __name__ == "__main__":
    draw_flag_line()


# # узор
# print('№2 Узор е')


# def draw_pattern(color1 = 232, color2 = 231):
#     print(f"{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*11}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*1}{END}")
#     print(f"{SET_COLOR}{color1}m{' '*2}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*7}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*3}{END}")
#     print(f"{SET_COLOR}{color1}m{' '*4}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*5}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*5}{END}")
#     print(f"{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*1}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*7}{END}")
#     print(f"{SET_COLOR}{color1}m{' '*7}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*8}{END}")
#     print(f"{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*1}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*7}{END}")
#     print(f"{SET_COLOR}{color1}m{' '*4}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*5}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*5}{END}")
#     print(f"{SET_COLOR}{color1}m{' '*2}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*7}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*3}{END}")
#     print(f"{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*11}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*1}{END}")


# if __name__ == "__main__":
#     for i in range(6):
#         draw_pattern()