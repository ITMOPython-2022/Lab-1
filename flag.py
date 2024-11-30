def print_flag_finland():
# ANSI escape sequences for colors
    white = "\033[48;5;15m "  # White background    
    blue = "\033[48;5;4m "    # Blue background
    reset = "\033[0m"         # Reset to default
    # Define the flag dimensions    
    height = 9
    width = 35    
    cross_width = 7
    cross_height = 3
    for row in range(height):       
        line = ""
        for col in range(width):       
            if (cross_height <= row < cross_height + 3) or (cross_width <= col < cross_width + 7):
                line += blue  # Add blue for the cross           
            else:
                line += white  # Add white for the background       
        line += reset  # Reset colors at the end of each line
        print(line)
# Call the function to print the flag
print_flag_finland()
