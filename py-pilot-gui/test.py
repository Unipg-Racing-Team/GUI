from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, ProgressBar
from textual.timer import Timer


class UtilityContainersExample(App):
    CSS_PATH = "utility_containers.css"

    def __init__(self) -> None:
        super().__init__()
        self.progress_timer: Timer
        self.progress_bar: ProgressBar

    def on_mount(self) -> None:
        """Inizia la progressione della progress bar."""
        self.progress_timer = self.set_interval(1 / 10, self.make_progress, pause=True)

    def make_progress(self) -> None:
        """Avanza la progress bar."""
        self.progress_bar.advance(1)

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal():
                yield Static("One", classes="column")
                yield Static("Two", classes="column")
            with Vertical(classes="column"):
                yield Static("Four")
                self.progress_bar = ProgressBar(
                    total=100,
                    classes="progress-bar",
                )
                yield self.progress_bar


if __name__ == "__main__":
    app = UtilityContainersExample()
    app.run()