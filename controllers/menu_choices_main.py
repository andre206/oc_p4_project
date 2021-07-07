#! /usr/bin/env python3
# coding: utf-8
""" Tournament menu choices
contains all class for make choice in the appliance about main.
"""

from controllers.menu_choices import SwitcherMenu
from controllers.menu_choices_players import SwitcherPlayersMenu
from controllers.menu_choice_tournament import SwitcherTournamentMenu
from controllers.menu_choices_reports import SwitcherReportsMenu
from controllers.menu_input import choice_option
from views.decorators_menus import pre_menu, main_menu


class SwitcherMainMenu(SwitcherMenu):

    @pre_menu
    @main_menu
    def option_selected(self, selected_option):
        super().option_selected(selected_option)

    def option_1(self):
        print(f"{'Tournament gestion':^120}\n")
        tournament_option = None
        SwitcherTournamentMenu(
            self.players_table, self.tournaments_table)\
            .option_selected(tournament_option)
        while tournament_option != 0:
            tournament_option = choice_option()
            SwitcherTournamentMenu(
                self.players_table, self.tournaments_table)\
                .option_selected(tournament_option)
        main_option = None
        SwitcherMainMenu(self.players_table, self.tournaments_table)\
            .option_selected(main_option)

    def option_2(self):
        """
        This option is the Players menu.
        It This will launch the players menu, with the option
         choices for the players menu.
        As soon as the user chooses option 0, it will
        automatically return to the main menu.
        """
        print(f"{'Players gestion':^120}\n")
        players_option = None
        SwitcherPlayersMenu(self.players_table, self.tournaments_table)\
            .option_selected(players_option)
        while players_option != 0:
            players_option = choice_option()
            SwitcherPlayersMenu(self.players_table,
                                self.tournaments_table)\
                .option_selected(players_option)
        SwitcherMainMenu(self.players_table, self.tournaments_table)\
            .option_selected(None)

    def option_3(self):
        """
        This option select the reports menu
        It This will launch the reports menu, with the option
         choices for the reports menu.
        As soon as the user chooses option 0, it will
        automatically return to the main menu.
        """
        reports_option = None
        SwitcherReportsMenu(
            self.players_table, self.tournaments_table) \
            .option_selected(reports_option)
        while reports_option != 0:
            reports_option = choice_option()
            SwitcherReportsMenu(
                self.players_table, self.tournaments_table) \
                .option_selected(reports_option)
        main_option = None
        SwitcherMainMenu(self.players_table, self.tournaments_table) \
            .option_selected(main_option)

    def option_0(self):
        print(f"\n{'Have a nice day and see you soon':^120}")
