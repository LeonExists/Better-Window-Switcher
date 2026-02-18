from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static


class MyTUIApp(App):
    """A Textual TUI application."""

    CSS = """
    Screen {
        background: $surface;
    }

    Container {
        height: 100%;
        align: center middle;
    }

    Static {
        width: 60;
        height: auto;
        padding: 2 4;
        background: $panel;
        border: solid $primary;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Container(
            Static("Welcome to My TUI App!\n\nPress 'q' to quit.")
        )
        yield Footer()


if __name__ == "__main__":
    app = MyTUIApp()
    app.run()
