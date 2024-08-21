def print_d_like_pattern(height):
    # Ensure the height is at least 5 to get a recognizable pattern
    if height < 5:
        print("Height must be at least 5")
        return
    
    width = height  # Width of the pattern

    for i in range(height):
        if i == 0 or i == height - 1:
            # Print the top and bottom horizontal lines
            print('*' * width)
        elif i < height // 2:
            # Print the upper vertical line and upper curve
            print('*' + ' ' * (width - 2) + '*')
        else:
            # Print the vertical line and lower curve
            print('*' + ' ' * (width - 2) + '*' * (height // 2 - i + height // 2))

# Set the height of the pattern
height = 7
print_d_like_pattern(height)
