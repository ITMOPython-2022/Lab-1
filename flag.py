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
