from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Label
from textual.reactive import Reactive
import threading
import time

class UtilityContainersExample(App):
    CSS_PATH = "utility_containers.css"

    progress: Reactive[int] = Reactive(0)

    def __init__(self) -> None:
        super().__init__()
        self.battery_status = {
            "low": "🔌", 
            "middle": "🪫",
            "full": "🔋"
        }
    
    def check_battery(self, level): 
        if level < 20: 
            return self.battery_status["low"]
        elif level < 50: 
            return self.battery_status["middle"]
        else:
            return self.battery_status["full"]

    def on_mount(self) -> None:
        """Start the progress of the progress bar."""
        self.start_progress_thread()

    def start_progress_thread(self) -> None:
        """Start the thread for the progress bar."""
        progress_thread = threading.Thread(target=self.run_progress)
        progress_thread.start()

    def run_progress(self) -> None:
        """Run the progress bar in a separate thread."""
        total = 100
        for i in range(total + 1):
            self.progress = i
            time.sleep(0.1)  # Wait for 0.1 seconds

    def get_progress_bar_text(self) -> str:
        bar_length = 40
        filled_length = int(bar_length * self.progress / 100)
        bar = '#' * filled_length + '-' * (bar_length - filled_length)
        return f'Progress: |{bar}| {self.progress}% complete'

    def on_model_update(self, changed: set[str]) -> None:
        """Handle updates to reactive attributes."""
        if "progress" in changed:
            self.invalidate()  # Force a re-render of the interface

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal():
                yield Static(self.check_battery(level=40), classes="column")  # Display battery emoji in the first column
                yield Static("Two", classes="column")  # Display "Two" in a column
            with Vertical(classes="column"):
                yield Static("Four")  # Display "Four"
                yield Label(self.get_progress_bar_text(), classes="progress-bar")


if __name__ == "__main__":
    app = UtilityContainersExample()
    app.run()
