#! /usr/bin/env python3
# coding: utf-8
""" Players menu choices """

from views.decorators_menus import pre_menu
from views.decorators_menus import players_menu
from views.menu import choice_option


class SwitcherPlayersMenu:
    @pre_menu
    @players_menu
    def option_selected(self, selected_option):
        """
        method to launch the appropriate methods according to the user's choice.
        Depending on the choice, a return is sent to the display.
        About choice in the player menu
        """
        option_name = f"option_{str(selected_option)}"
        option = getattr(self, option_name, lambda: "Invalid option")
        return option()

    def option_1(self):
        print("Add new player")

    def option_2(self):
        print("View all players")

    def option_3(self):
        print("Modify one player")

    def option_4(self):
        print("Delete all players")

    def option_0(self):
        print("Return principal menu")


if __name__ == '__main__':
    option = None
    SwitcherPlayersMenu().option_selected(option)

    while option != 0:
        option = choice_option()
        SwitcherPlayersMenu().option_selected(option)
