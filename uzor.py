SET_COLOR = "\x1b[48;5;"
END = '\u001b[0m'
repeats = 5


def draw_pattern(color1 = 232, color2 = 231):
    print(f"{SET_COLOR}{color2}m{' '*6}{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*6}{END}")
    print(f"{SET_COLOR}{color2}m{' '*6}{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*6}{END}")
    print(f"{SET_COLOR}{color2}m{' '*6}{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*6}{END}")
    print(f"{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*6}{SET_COLOR}{color1}m{' '*6}{END}")
    print(f"{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*6}{SET_COLOR}{color1}m{' '*6}{END}")
    print(f"{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*6}{SET_COLOR}{color1}m{' '*6}{END}")
    print(f"{SET_COLOR}{color2}m{' '*6}{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*6}{END}")
    print(f"{SET_COLOR}{color2}m{' '*6}{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*6}{END}")
    print(f"{SET_COLOR}{color2}m{' '*6}{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*6}{END}")


if __name__ == "__main__":
    for i in range(repeats):
        draw_pattern()