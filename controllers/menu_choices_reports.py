#! /usr/bin/env python3
# coding: utf-8
""" Reports menu choices
contains all class for make choice in the appliance about reports.
"""
from controllers.menu_choices import SwitcherMenu
from views.decorators_menus import (
    pre_menu,
    reports_menu,
    reports_tournament,
)
from views.view_players import (
    view_all_players,
)


class SwitcherReportsMenu(SwitcherMenu):

    @pre_menu
    @reports_menu
    def option_selected(self, selected_option):
        super().option_selected(selected_option)

    def option_1(self):
        """
        Displays all players in the database in ranking order
        """
        print(f"{'View All Players - by rank':^120}\n")
        view_all_players(self.players_table, 'rank')


    def option_2(self):
        """
        Displays all players in the database in family name order
        """
        print(f"{'View All Players - by family name':^120}\n")
        view_all_players(self.players_table, 'name')

    def option_3(self):
        print(f"{'Reports':^120}\n")

    def option_0(self):
        print(f"\n{'Have a nice day and see you soon':^120}")