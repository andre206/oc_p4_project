#! /usr/bin/env python3
# coding: utf-8
""" Main menu choices"""

from views.decorators_menus import pre_menu
from views.decorators_menus import main_menu
from views.menu import choice_option
from controllers.players_menu import SwitcherPlayersMenu as SPM


class SwitcherMainMenu:
    @pre_menu
    @main_menu
    def option_selected(self, selected_option):
        """
        method to launch the appropriate methods according to the user's choice.
        Depending on the choice, a return is sent to the display.
        About choice in the main menu.
        """
        option_name = f"main_option_{str(selected_option)}"
        option = getattr(self, option_name, lambda: "Invalid option")
        return option()

    def main_option_1(self):
        print("It's the first option, take it easy !")

    def main_option_2(self):
        """
        This option is the Players menu.
        It This will launch the players menu, with the option choices for the players menu.
        As soon as the user chooses option 0, it will automatically return to the main menu.
        """
        print("It's the second option, take it easy !")
        players_option = None
        SPM().option_selected(players_option)
        while players_option != 0:
            players_option = choice_option()
            SPM().option_selected(players_option)
        main_option = None
        SwitcherMainMenu().option_selected(main_option)

    def main_option_3(self):
        print("Its the third option, oh yeah !")

    def main_option_0(self):
        print("It's over... Bye !")


if __name__ == '__main__':
    main_option = None
    SwitcherMainMenu().option_selected(main_option)

    while main_option != 0:
        main_option = choice_option()
        SwitcherMainMenu().option_selected(main_option)
