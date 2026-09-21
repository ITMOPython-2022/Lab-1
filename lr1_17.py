import time
import sys


BLUE = '\u001b[44m'
RED = '\u001b[41m'
WHITE = '\u001b[47m'
RESET = '\u001b[0m'
ERASE = '\x1B[2K'
BEGIN = '\x1B[1G'


def flag():
    pixel = '    '
    lenght = 10
    height = lenght

    for i in range(height):
        if i < height // 2:
            print(BLUE + pixel * (i + 1) + WHITE + pixel * (lenght - i) + RESET)
        else:
            print(BLUE + pixel * (lenght - i) + RED + pixel * (i + 1) + RESET)


def loading():
    for i in range(100):
        print(f'\u001b[20DLoading... {i+1}%', end='', flush=True)
        time.sleep(0.1)
    print(" Done!")


def multiple_progressbar(num_tasks):
    bar_width = 25
    for task in range(1, num_tasks+1):
        for progress in range(1, bar_width+1):
            bar = '#' * progress + '_' * (bar_width - progress)
            print(f'{BEGIN}Task {task}/{num_tasks} [{bar}] {progress * 4}%', end='', flush=True)
            time.sleep(0.1)
    print(" Done")


def diamond():
    height = 15
    center = height // 2
    offset = height // 2
    step = 1
    lenght = 1
    colors = [87, 196, 226]

    while True:
        for color in colors:
            for line in range(height):
                print(f'{' ' * offset}\u001b[48;5;{color}m{' ' * lenght}{RESET}')
                if line < center:
                    offset -= step
                    lenght += step * 2
                else:
                    offset += step
                    lenght -= step * 2
            print(f'\u001b[{height + 2}A')
            print(f'\u001b[{offset+1}D')
            lenght = 1
            offset = height // 2
            time.sleep(2)


def sequence():
    file = open('sequence.txt', 'r')
    odds = []
    evens = []
    for line in file:
        if int(float(line) * 100) % 2 == 0:
            odds.append(float(line))
        else:
            evens.append(float(line))
    file.close()
    # print(len(odds), len(evens))
    print(f'{BLUE}{' ' * int(len(odds) / 5)}{RESET} {len(odds)/(len(odds) + len(evens)) * 100}%')
    print(f'{RED}{' ' * int(len(evens) / 5)}{RESET} {len(evens)/(len(odds) + len(evens)) * 100}%')


#flag()
#loading()
#m = int(sys.argv[1]) if len(sys.argv) > 1 else 3
#multiple_progressbar(m)
# diamond()
sequence()