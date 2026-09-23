import os
import time
from pathlib import Path


RESET = "\033[0m"
BLUE = "\033[44m"
RED = "\033[41m"
WHITE = "\033[47m"
BLACK = "\033[40m"
GREEN = "\033[42m"
YELLOW = "\033[43m"


SEQUENCE_PATH = Path(__file__).with_name("sequence.txt")


def block(color, width):
    return f"{color}{' ' * width}{RESET}"


def pause(seconds=0.8):
    time.sleep(seconds)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[H", end="")


def draw_flag():
    """Draws the Swiss flag for variant 10."""
    height = 13
    width = 26

    print("1. Flag")
    for row in range(height):
        line = ""
        for column in range(width):
            in_vertical_cross = 10 <= column <= 15 and 3 <= row <= 9
            in_horizontal_cross = 6 <= column <= 19 and 5 <= row <= 7
            color = WHITE if in_vertical_cross or in_horizontal_cross else RED
            line += block(color, 2)
        print(line)
    print()


def draw_pattern(repeats=4):
    """Draws pattern j: two repeating hollow circles."""
    pattern = [
        "  ####    ####  ",
        " ##  ##  ##  ## ",
        "##    ####    ##",
        " ##  ##  ##  ## ",
        "  ####    ####  ",
    ]

    print("2. Repeating pattern")
    for line in pattern:
        print((BLACK + line + RESET + "  ") * repeats)
    print()


def animation(delay=0.5):
    """Animates the Swiss flag cross in four frames."""
    frames = [
        (11, 14, 4, 8, 8, 17, 5, 7),
        (10, 15, 3, 9, 7, 18, 5, 7),
        (9, 16, 3, 9, 6, 19, 5, 7),
        (10, 15, 3, 9, 7, 18, 5, 7),
    ]

    for frame_number, frame in enumerate(frames, start=1):
        vertical_left, vertical_right, vertical_top, vertical_bottom = frame[:4]
        horizontal_left, horizontal_right, horizontal_top, horizontal_bottom = frame[4:]

        clear_screen()
        print(f"3. Animation. Swiss flag. Frame {frame_number}/4\n")
        for row in range(13):
            line = ""
            for column in range(26):
                in_vertical_cross = (
                    vertical_left <= column <= vertical_right
                    and vertical_top <= row <= vertical_bottom
                )
                in_horizontal_cross = (
                    horizontal_left <= column <= horizontal_right
                    and horizontal_top <= row <= horizontal_bottom
                )
                color = WHITE if in_vertical_cross or in_horizontal_cross else RED
                line += block(color, 2)
            print(line)
        pause(delay)

    clear_screen()


def read_sequence():
    with SEQUENCE_PATH.open(encoding="utf-8") as file:
        return [float(line) for line in file if line.strip()]


def draw_sequence_chart(numbers):
    """Compares numbers from -3 to 3 with all other numbers."""
    inside_count = sum(1 for number in numbers if -3 <= number <= 3)
    outside_count = len(numbers) - inside_count
    total = len(numbers)

    groups = [
        ("from -3 to 3", inside_count, RED),
        ("other numbers", outside_count, BLUE),
    ]

    print("4. Sequence chart")
    for title, count, color in groups:
        percent = count / total * 100 if total else 0
        bar_width = round(percent / 2)
        print(f"{title:14} {block(color, bar_width)} {percent:5.1f}% ({count})")
    print()


def build_function_plot(size=10):
    """Generates the first quarter of y = x / 3 as one console string."""
    max_x = size - 1
    max_y = max_x / 3
    values = [x / 3 for x in range(size)]
    scaled_values = [round(value / max_y * (size - 1)) for value in values]

    plot = ["5. Function y = x / 3"]
    for y in range(size - 1, -1, -1):
        line = ""
        for x in range(size):
            if scaled_values[x] == y:
                line += f"{YELLOW}  {RESET}"
            elif x == 0 or y == 0:
                line += f"{WHITE}  {RESET}"
            else:
                line += "  "
        plot.append(line)
    return "\n".join(plot)


def draw_function_plot(size=10):
    print(build_function_plot(size))
    print()


def main():
    draw_flag()
    draw_pattern()
    animation()
    numbers = read_sequence()
    draw_sequence_chart(numbers)
    draw_function_plot()


if __name__ == "__main__":
    main()
