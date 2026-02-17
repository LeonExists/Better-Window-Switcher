# Libraries
from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Label, OptionList
from textual.widgets.option_list import Option


# Menu
class Home(Screen):    
    def compose(self) -> ComposeResult:
        yield Header("Menu")

        yield OptionList(
            Option("Option-1", id="option-1"),
            Option("Option-2", id="option-2"),
            Option("Option-3", id="option-3"),
            id="option-list"
        )

        self.option = Label("Option: ")
        yield self.option

        yield Footer()

    @on(OptionList.OptionSelected, "#option-list")
    def handle_option_selection(self, event: OptionList.OptionSelected):
        selected_id = event.option.id

        self.option.update(f"Option: {selected_id}")