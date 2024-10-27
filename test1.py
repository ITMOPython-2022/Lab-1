import time


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"


def draw_line(offset=0, length=1, color=222):
    line = " " * length
    print (f"{' ' * offset}{SET_COLOR}{color}m{line}{END}")

def draw_romb():
    size = 15
    center = size // 2
    offset = size // 2

    step = 1
    length = 1

    colors = [222, 157]

    while True:
        for color in colors:
            for line in range (size):
                draw_line(offset, length, color)

                if line < center:
                    offset -= step
                    length += step*2
                else :
                    offset += step
                    length -= step*2

            print(f"\x1b[{size+2}A")
            print(f"\x1b[{offset}D")

            length = 1
            offset = size // 2

            time.sleep (2)


    # print (size, center, offset)

draw_romb()

# if __name__ == "__main__":
#     # for i in range (20):
#     #        draw_line(length=20, color=47, offset=i)
#     #        print (f"{CLEAR}")
#     #        time.sleep(0.5)