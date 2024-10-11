WIDTH = 60
HEIGHT = 15
CIRCLE_UP = 2
CIRCLE_BOTTOM = 12
CIRCLE_WIDTH = 18
CIRCLE_CENTER = HEIGHT // 2

len_red = 8

for row in range(HEIGHT):
    if CIRCLE_UP < row < CIRCLE_BOTTOM:
        len_white = (WIDTH - len_red) // 2
        white = f'\x1b[48;5;{7}m{" " * len_white}\x1b[0m'
        red = f'\x1b[48;5;{1}m{" " * len_red}\x1b[0m'
        print(white + red + white)
        
        if row < CIRCLE_CENTER and len_red < CIRCLE_WIDTH:
            len_red += 4
        elif row > CIRCLE_CENTER:
             len_red -= 4
    else:
        print(f'\x1b[48;5;{7}m{" " * WIDTH}\x1b[0m')