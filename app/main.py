from textual.app import App, ComposeResult
from textual.widgets import Label, Button

from pathlib import Path


class Climon(App):
    PARENTDIR = Path(__file__).resolve().parent.parent
    CSS_PATH = PARENTDIR / "static/theme.css" 
    def compose(self) -> ComposeResult:
        self.close_button = Button("close", id="close")
        yield Label("Hello, World!", id="main-label")
        yield self.close_button

    def on_mount(self) -> None:
        self.screen.styles.background = "gray"
        self.close_button.styles.background = "darkblue"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


if __name__ == "__main__":
    app = Climon()
    app.run()
