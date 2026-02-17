# Libraries
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Label


# Menu
class Hotkeys(Screen):
    def compose(self) -> ComposeResult:
        yield Header("Hotkeys")

        yield Label("Create custom Hotkeys with AutoHotkey easily")

        yield Footer()