import sys
import time


class ProgressBar:
    """
    A class to display a customizable progress bar with a spinner, color support, 
    and dynamic updates to show task progress.
    """
    def __init__(
        self, 
        total: int, 
        bar_length: int = 30, 
        full_char: str = '▰', 
        empty_char: str = '▱', 
        spinner_chars: str = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏',
        color_full: str = '\033[1;38;2;224;0;90m',  
        color_empty: str = '\033[1;38;2;54;65;82m',  
        color_spinner: str = '\033[1;38;2;255;215;0m',  
        color_status: str = '\033[1;38;2;104;118;244m',  
        color_complete: str = '\033[1;38;2;12;159;109m',  
        reset: str = '\033[0m',  
        clear_line: str = '\033[K',  
        output=sys.stdout  
    ):
        """
        Initializes the progress bar with customizable parameters.
        
        :param total: The total number of steps in the task (must be > 0).
        :param bar_length: The length of the progress bar (default 30).
        :param full_char: The character used to represent the filled portion of the bar (default '▰').
        :param empty_char: The character used to represent the empty portion of the bar (default '▱').
        :param spinner_chars: A string of characters used for the spinner animation (default '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏').
        :param color_full: Color for the filled portion of the bar (default is red).
        :param color_empty: Color for the empty portion of the bar (default is blue).
        :param color_spinner: Color for the spinner animation (default is yellow).
        :param color_status: Color for the percentage/status text (default is blue).
        :param color_complete: Color for the status text when the task is complete (default is green).
        :param reset: ANSI reset code to revert colors (default is '\033[0m').
        :param clear_line: ANSI code to clear the current line on the terminal (default is '\033[K').
        :param output: The stream where output should be printed (default is sys.stdout).
        """
        self.total = total
        self.bar_length = bar_length
        self.full_char = full_char
        self.empty_char = empty_char
        self.spinner_chars = spinner_chars
        self.color_full = color_full
        self.color_empty = color_empty
        self.color_spinner = color_spinner
        self.color_status = color_status
        self.color_complete = color_complete
        self.reset = reset
        self.clear_line = clear_line  
        self.output = output

        self.current_value = 0
        self.spinner_index = 0
        self._validate_total()

    def _validate_total(self):
        """
        Validates that the total number of steps is specified and greater than 0.
        
        Raises:
            ValueError: If the total number of steps is None or less than or equal to 0.
        """
        if self.total is None or self.total <= 0:
            raise ValueError('Total steps must be specified and greater than 0.')

    @property
    def percentage(self) -> float:
        """
        Calculates the current progress percentage based on the current value and total steps.
        
        :return: The current progress as a percentage (0 to 100).
        """
        return (self.current_value / self.total) * 100

    def _generate_bar(self) -> str:
        """
        Generates the string representation of the progress bar, combining filled and empty portions.
        
        :return: A string representing the progress bar with colors applied.
        """
        filled_length = int(self.percentage / 100 * self.bar_length)
        return (
            f'{self.color_full}{self.full_char * filled_length}{self.reset}'
            f'{self.color_empty}{self.empty_char * (self.bar_length - filled_length)}{self.reset}'
        )

    def _get_spinner(self) -> str:
        """
        Retrieves the next spinner character in the sequence and cycles through them.
        
        :return: A string containing the next spinner character.
        """
        char = self.spinner_chars[self.spinner_index]
        self.spinner_index = (self.spinner_index + 1) % len(self.spinner_chars)
        return f'{self.color_spinner}{char}{self.reset}'

    def display(self) -> None:
        """
        Displays the current progress bar, spinner, and status message in the terminal. 
        This method updates the display each time it is called.
        If the progress reaches 100%, the task is marked as complete.
        """
        status_color = self.color_complete if self.percentage >= 100 else self.color_status
        status_text = 'Completed!' if self.percentage >= 100 else f'{self.percentage:.2f}%'

        self.output.write(f'\r{self.clear_line}{self._get_spinner()} {self._generate_bar()} {status_color}{status_text}{self.reset}')
        self.output.flush()

    def update(self, value: int = 1) -> None:
        """
        Updates the current progress by the specified value and ensures the value does not exceed the total.
        
        :param value: The number of steps to increment the progress by (default is 1).
        """
        self.current_value = min(self.current_value + value, self.total)


def simulate_task(total_steps: int, step_duration: float = 0.1, step_increment: int = 1) -> None:
    """
    Simulates a task by incrementally updating the progress bar and displaying it with a delay.
    
    :param total_steps: The total number of steps in the task.
    :param step_duration: The duration (in seconds) to wait between each step update (default is 0.1).
    :param step_increment: The number of steps to increment at each update (default is 1).
    """
    progress_bar = ProgressBar(total=total_steps, bar_length=50)

    for _ in range(0, total_steps, step_increment):
        time.sleep(step_duration)
        progress_bar.update(step_increment)
        progress_bar.display()


def main() -> None:
    """
    The main function that starts the task simulation with a specified number of total steps, 
    step duration, and increment.
    """
    simulate_task(total_steps=10_000_000, step_duration=0.1, step_increment=4096)


if __name__ == '__main__':
    main()
