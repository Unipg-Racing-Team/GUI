import time

def update_horizontal_bar(value, max_value, bar_length):
    # Calculate the length of the filled and empty segments of the bar
    filled_length = int(bar_length * value / max_value)
    empty_length = bar_length - filled_length

    # Create the visual representation of the bar
    bar = '\033[95m█' * filled_length + '\033[0m░' * empty_length

    return f'|{bar}|'

def run_horizontal_bar(max_value, bar_length, initial_speed, speed_increment):
    value = 0
    speed = initial_speed

    while value <= max_value:
        horizontal_bar = update_horizontal_bar(value, max_value, bar_length)
        # Print the horizontal bar, current progress, and speed
        print(f'{horizontal_bar} {value}/{max_value} - Speed: {speed}')
        value += speed_increment
        speed += speed_increment
        time.sleep(0.5)  # Pause for 0.5 seconds between each iteration

    print("Maximum speed reached!")

# Example usage of the function
max_value = 100
bar_length = 100
initial_speed = 0  # Initial speed of the progress bar increment
speed_increment = 5  # Increment of the speed for each iteration

run_horizontal_bar(max_value, bar_length, initial_speed, speed_increment)