
# Customizable Console Progress Bar with Spinner

This repository contains a Python implementation of a **progress bar** with a **spinner**, complete with **color customization** and **dynamic status updates**. This is a highly customizable and reusable tool for displaying progress for long-running tasks directly in the terminal.

## Features

- **Customizable Progress Bar**: Display the progress in a visually appealing manner, with customizable length, characters, and color schemes.
- **Spinner Animation**: Adds a dynamic spinner animation to indicate that the process is still ongoing.
- **Task Completion**: Automatically completes the task once the progress reaches 100%.
- **Customizable Colors**: Choose from a range of colors for different parts of the progress bar, spinner, and status messages.
- **Clear Console Output**: The progress bar updates on the same line, keeping the console clean.
- **Graceful Handling of Large Tasks**: Efficient handling of long tasks by updating progress in increments and using customizable delays.

## Key Features

- **Progress Bar Display**: A clear visual representation of task progress with custom colors for the filled and empty sections.
- **Spinner Animation**: A spinner that updates every iteration, showing activity while the task is running.
- **Percentage Tracking**: Displays the percentage of completion in the status message.
- **Automatic Task Completion**: Once the task reaches 100%, the progress bar displays "Completed!" and stops further updates.
- **Color Support**: Each element of the progress bar, spinner, and status message can be customized using ANSI color codes.
- **Flexible Configuration**: The progress bar length, spinner characters, color scheme, and total steps can be configured to suit your needs.

## Installation

To use this progress bar in your project, you can either clone this repository or copy the code directly into your project.

1. Clone the repository:
   ```bash
   git clone https://github.com/lun4r0w1tv/console-progress-bar.git
   cd console-progress-bar
   ```

2. Or directly copy the code into your project.

## How to Use

The core of the implementation is the `ProgressBar` class, which you can instantiate with the total number of steps for your task. You can customize various aspects of the progress bar and spinner, including the color scheme and character set.

```python
from progress_bar import ProgressBar
import time

# Simulate a task with 10 million steps
progress_bar = ProgressBar(total=10_000_000, bar_length=50)

# Simulate progress
for i in range(0, 10_000_000, 4096):
    time.sleep(0.1)  # Simulate task duration
    progress_bar.update(4096)  # Update progress
    progress_bar.display()  # Display progress
```

## Customization

You can customize the following parameters when creating the `ProgressBar` instance:

- `total`: Total steps in the task.
- `bar_length`: The length of the progress bar.
- `full_char`: Character used to display the filled portion of the bar.
- `empty_char`: Character used to display the empty portion of the bar.
- `spinner_chars`: String of characters used for the spinner animation.
- `color_full`: Color for the filled portion of the progress bar.
- `color_empty`: Color for the empty portion of the progress bar.
- `color_spinner`: Color for the spinner.
- `color_status`: Color for the status text.
- `color_complete`: Color for the status text when the task is completed.
- `reset`: ANSI reset code to revert colors after the progress bar display.
- `output`: The output stream (e.g., `sys.stdout` or a custom stream).

## Example Usage

```python
from progress_bar import ProgressBar
import time

def simulate_task(total_steps: int, step_duration: float = 0.1, step_increment: int = 1):
    progress_bar = ProgressBar(total=total_steps, bar_length=50)
    
    for _ in range(0, total_steps, step_increment):
        time.sleep(step_duration)
        progress_bar.update(step_increment)
        progress_bar.display()

simulate_task(10_000_000, step_duration=0.1, step_increment=4096)
```

## Explanation

- **Progress Bar**: The progress bar is displayed dynamically, showing the filled and empty portions, updated with every iteration.
- **Spinner**: While the task is ongoing, the spinner is displayed alongside the progress bar to indicate that the task is running.
- **Status**: Once the progress reaches 100%, the status changes to "Completed!" and the task ends.
- **Custom Output**: You can change the output stream to direct the progress bar display to a file, another output, or the default console output.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
