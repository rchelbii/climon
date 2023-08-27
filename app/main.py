from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import (
        Label,
        Button,
        Header,
        Footer,
        Static
)

from pathlib import Path


class Climon(App):
    PARENTDIR = Path(__file__).resolve().parent.parent
    CSS_PATH = PARENTDIR / "static/grid.css" 

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
    ]

    def compose(self) -> ComposeResult:
        self.close_button = Button("close", id="close")
        yield Header(name="Climon", show_clock=True)
        yield Static("Uno", classes="box")
        yield Static("Uno", classes="box")
        yield Static("Uno", classes="box")
        yield Static("Uno", classes="box")
        yield Static("Uno", classes="box")
        yield Static("Uno", classes="box")
        yield Footer()

    def on_mount(self) -> None:
        self.screen.styles.background = "ansi_bright_blue"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


if __name__ == "__main__":
    app = Climon()
    app.run()
