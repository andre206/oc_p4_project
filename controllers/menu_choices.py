#! /usr/bin/env python3
# coding: utf-8
""" Main menu choices
contains the master class of the menu.
"""


class SwitcherMenu:
    def __init__(self, players_table,
                 tournaments_table,
                 id_player=None,
                 id_tournament=None):
        self.players_table = players_table
        self.tournaments_table = tournaments_table
        self.id_player = id_player
        self.id_tournament = id_tournament

    def option_selected(self, selected_option):
        """
        method to launch the appropriate methods
        according to the user's choice.
        Depending on the choice, a return is sent
        to the display. About choice in the main menu.
        """
        option_name = f"option_{str(selected_option)}"
        option = getattr(self, option_name, lambda: "Invalid option")
        return option()
