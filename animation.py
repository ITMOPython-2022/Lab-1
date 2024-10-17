import time
import os

SET_COLOR = "\x1b[38;5;"
END = "\x1b[0m"


def clear_screen():
    os.system('cls')


colors = [35, 37, 39, 42, 56, 68]


def generate_frames(text, width):
    frames = []
    for i in range(width):
        frames.append(i)
    return frames


text = "Добро пожаловать!"
width = 30


frames = generate_frames(text, width)


while True:
    for i, frame in enumerate(frames):
        clear_screen()
        color = colors[i % len(colors)]
        print(f"{' ' * frame}{SET_COLOR}{color}m{text}{END}")
        time.sleep(0.5)








# SET_COLOR = "\x1b[48;5;"
# END = "\x1b[0m"

# # ANSI escape codes for text colors
# SET_COLOR = "\033["
# END = "\033[0m"

# ANSI escape codes for text colors
# ANSI escape codes for text colors
# ANSI escape codes for text colors
# SET_COLOR = "\033["
# END = "\033[0m"

# def draw_pattern(color1=232, color2=231):
#     """Draws a single pattern."""
#     return [
#         f"{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*11}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*1}{END}",
#         f"{SET_COLOR}{color1}m{' '*2}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*7}{SET_COLOR}{color2}m{' '*3}{SET_COLOR}{color1}m{' '*3}{END}",
#         f"{SET_COLOR}{color1}m{' '*4}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*5}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*5}{END}",
#         f"{SET_COLOR}{color1}m{' '*6}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*1}{SET_COLOR}{color2}m{' '*2}{SET_COLOR}{color1}m{' '*7}{END}",
#         f"{SET_COLOR}{color1}m{' '*8}{SET_COLOR}{color2}m{' '*1}{SET_COLOR}{color1}m{' '*9}{END}",
#     ]

# def draw_grid(rows=10, cols=10, color1=232, color2=231):
#     """Draws a grid of patterns."""
#     pattern_lines = draw_pattern(color1, color2)
    
#     for r in range(rows):  # Loop through rows
#         for line in pattern_lines:  # Loop through each line of the pattern
#             print(line * cols)  # Repeat the line for the number of columns
#         print()  # New line after each pattern block

# if __name__ == "__main__":
#     draw_grid()


















