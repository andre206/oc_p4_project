#! /usr/bin/env python3
# coding: utf-8
"""
Tournament menu choices
contains all class for make choice in the appliance about main.

Classes
-----
SwitcherMainMenu(SwitcherMenu)
    It's the main menu of the appliance. It's allow you to go to every menus
    of the appliance :
    - Tournaments gestion
    - Players gestion
    - Reports
"""

from controllers.menu_choices import SwitcherMenu
from controllers.menu_choices_players import SwitcherPlayersMenu
from controllers.menu_choice_tournament import SwitcherTournamentMenu
from controllers.menu_choices_reports import SwitcherReportsMenu
from controllers.menu_input import choice_option
from views.decorators_menus import pre_menu, main_menu


class SwitcherMainMenu(SwitcherMenu):
    """
    It's the main menu of the appliance. It's allow you to go to every menus
    of the appliance :
    - Tournaments gestion
    - Players gestion
    - Reports

    Methods
    -------
    option_selected(self, selected_option)
        method to retrieve the option chosen by the user
    option_1(self)
        For going to the 'tournaments gestion' menu
    option_2(self)
        For going to the 'players gestion' menu
    option_3(self)
        For going to view all reports of the appliance about
            - tournaments
            - players
            - players of one tournament...
    option_0
        Option for quit the appliance
    """
    @pre_menu
    @main_menu
    def option_selected(self, selected_option):
        """
        method inherited from the SwitcherMenu class
        retrieve the option chosen by the user

        Parameters
        ----------
        selected_option : str
            input by the user
        """
        super().option_selected(selected_option)

    def option_1(self):
        """
        This option redirect on the Tournaments menu
        It will launch the tournaments menu, with the option
         choices for the tournaments menu.
        As soon as the user chooses option 0, it will
        automatically return to the main menu.
        """
        tournament_option = str(None)
        SwitcherTournamentMenu(
            self.players_table, self.tournaments_table)\
            .option_selected(tournament_option)
        while tournament_option != 0:
            tournament_option = choice_option()
            SwitcherTournamentMenu(
                self.players_table, self.tournaments_table)\
                .option_selected(tournament_option)
        main_option = str(None)
        SwitcherMainMenu(self.players_table, self.tournaments_table)\
            .option_selected(main_option)

    def option_2(self):
        """
        This option redirect on the Players menu.
        It will launch the players menu, with the option
         choices for the players menu.
        As soon as the user chooses option 0, it will
        automatically return to the main menu.
        """
        players_option = str(None)
        SwitcherPlayersMenu(self.players_table, self.tournaments_table)\
            .option_selected(players_option)
        while players_option != 0:
            players_option = choice_option()
            SwitcherPlayersMenu(self.players_table,
                                self.tournaments_table)\
                .option_selected(players_option)
        SwitcherMainMenu(self.players_table, self.tournaments_table)\
            .option_selected(str(None))

    def option_3(self):
        """
        This option select the reports menu
        It will launch the reports menu, with the option
         choices for the reports menu.
        As soon as the user chooses option 0, it will
        automatically return to the main menu.
        """
        reports_option = str(None)
        SwitcherReportsMenu(
            self.players_table, self.tournaments_table) \
            .option_selected(reports_option)
        while reports_option != 0:
            reports_option = choice_option()
            SwitcherReportsMenu(
                self.players_table, self.tournaments_table) \
                .option_selected(reports_option)
        main_option = str(None)
        SwitcherMainMenu(self.players_table, self.tournaments_table) \
            .option_selected(main_option)

    def option_0(self):
        """
        Ending the appliance
        """
        print(f"\n\033[95m{'Have a nice day and see you soon':^120}\033[0m")
