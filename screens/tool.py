# Libraries
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Label


# Menu
class Tool(Screen):
    def compose(self) -> ComposeResult:
        yield Header("Tool")

        yield Label("This is a tool")

        yield Footer()