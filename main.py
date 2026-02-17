# Libraries
from textual import on
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Label, OptionList
from textual.widgets.option_list import Option

# Screens
from screens.home import Home
from screens.hotkeys import Hotkeys


# Main
class Main(App):
    CSS_PATH = "style.tcss"

    BINDINGS = [
        ("escape", "go_home", "Back to Home"),
        ("1", "go_hotkeys", "Hotkeys"),
    ]
    
    
    # Mount
    async def on_mount(self) -> None:
        await self.push_screen(Home())


    # Compose
    def compose(self) -> ComposeResult:
        yield Header("Home")

        OptionList()

        yield OptionList(
            Option("Hotkeys", id="option-hotkeys"),
            Option("Option-2", id="option-2"),
            Option("Option-3", id="option-3"),
            name="Menus",
            id="option-list"
        )

        self.option = Label("Option: ")
        yield self.option

        yield Footer()

    @on(OptionList.OptionSelected, "#option-list")
    def handle_option_selection(self, event: OptionList.OptionSelected):
        selected_id = event.option.id

        # hotkeys
        if selected_id == "option-hotkeys":
            self.switch_screen(Hotkeys())

        self.option.update(f"Option: {selected_id}")


    # Actions
    def action_go_home(self) -> None:
        self.switch_screen(Home())

    def action_go_hotkeys(self) -> None:
        self.switch_screen(Hotkeys())


if __name__ == "__main__":
    Main().run()
