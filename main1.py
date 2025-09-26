import time, sys


RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
ERASE = '\x1B[2K' # erase the line
BEGIN = '\x1B[1G' # return to column 1


def flag():
    line = ' ' * 4
    lenght = 15
    height = lenght

    for i in range(height):
        if i < height // 2:
            print(f'{BLUE}{line * (i + 1)}{WHITE}{line * (lenght - i)}{END}') 
        else:
            print(f'{BLUE}{line * (lenght - i)}{RED}{line * (i + 1)}{END}')


def loading():
    for i in range(100):
        time.sleep(0.1)
        print(f'\u001b[100DLoading... {i+1}%', end='', flush=True)
    print(' Done!')


def loading_multiple(num_tasks):
    bar_width = 25
    for k in range(1, num_tasks+1):
        for p in range(1, bar_width+1):
            #filled = p
            bar = "#" * p + "-" * (bar_width - p)
            #print(f'{BEGIN}{ERASE}Task {k}/{num_tasks} [{bar}] {p * 4}%',
                  #end='', flush=True)
            print(BEGIN + ERASE+"Task "+str(k)+"/"+str(num_tasks)+
                  " ["+bar+"] "+str(p * 4)+"%", end='', flush=True)
            time.sleep(0.1)
    print("Done!")


def draw_line(offset=0, lenght=1, color=88):
    line = ' ' * lenght
    print(f'{" " * offset}\x1b[48;5;{color}m{line}\x1b[0m')


def draw_diamond():
    height = 15
    center = height // 2
    offset = height // 2
    step = 1
    lenght = 1
    colors = [88, 157, 105]

    while True:
        for color in colors:
            for line in range(height):
                draw_line(offset, lenght, color)
                if line < center:
                    offset -= step
                    lenght += step * 2
                else:
                    offset += step
                    lenght -= step * 2
            print(f'\x1b[{height + 2}A')
            print(f'\x1b[{offset}D')
            lenght = 1
            offset = height // 2
            time.sleep(2)




#loading_multiple(3)
#flag()
#draw_diamond()

file = open('sequence.txt', 'r')
list = []
for line in file:
    list.append(float(line))
print(list[3:10])