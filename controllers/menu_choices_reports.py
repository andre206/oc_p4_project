#! /usr/bin/env python3
# coding: utf-8
"""
Reports menu choices
contains all class for make choice in the appliance about reports.

Classes
-------
SwitcherReportsMenu(SwitcherMenu)
    View menu for reports of all informations form the base
SwitcherChooseTournament(SwitcherMenu)
    permit to select one id tournament to view informations about the selected tournament
SwitchedViewTournament(SwitcherMenu)
    permit to view all information about one specific tournament
"""
from time import sleep

from controllers.menu_choices import SwitcherMenu
from controllers.user_entry import ControlEntryTournament as Cet
from controllers.menu_input import (
    choice_option,
    selected_tournament,
)
from controllers.backup_restore_tournament import deserialized_tournaments
from controllers.backup_restore_players import deserialized_players
from views.decorators_menus import (
    pre_menu,
    reports_menu,
    reports_tournament,
    tournament_modify_menu
)
from views.players import (
    view_all_players,
)
from views.ranking import view_players_tournament
from views.tournaments import (
    view_all_tournaments,
    report_all_informations_one_tournament,
)
from views.list_rounds_matches import view_rounds_matches


class SwitcherReportsMenu(SwitcherMenu):
    """
    View menu for reports of all informations form the base

    Attributes (inherited by the SwitcherMenu)
    ------
    players_table : tinydb.table.Table
    tournaments_table : tinydb.table.Table
    id_player : None (str/int)
    id_tournament : None (str/int)

    Methods
    -------
    option_selected(self, selected_option)
        method to retrieve the option chosen by the user
    option_1(self)
        Displays all players in the database in ranking order
    option_2(self)
        Displays all players in the database in family name order
    option_3(self)
        Display a list of all Tournament
    option_4(self)
        Display the menu to select a tournament id or return to the report menu
    option_0()
        back to the menu to the main menu
    """
    @pre_menu
    @reports_menu
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
        Displays all players in the database in ranking order
        """
        print(f"\033[33m{'View All Players - by rank':^120}\n\033[0m")
        view_all_players(self.players_table, 'rank')

    def option_2(self):
        """
        Displays all players in the database in family name order
        """
        print(f"\033[33m{'View All Players - by family name':^120}\n\033[0m")
        view_all_players(self.players_table, 'name')

    def option_3(self):
        """
        Display a list of all Tournament
        - ID
        - Name
        - Date
        - Number of rounds played
        - Number of players
        - State (finished / not finished)
        """
        print(f"\033[33m{'View List of all Tournaments':^120}\033[0m\n")
        view_all_tournaments(self.tournaments_table)

    def option_4(self):
        """
        Display the menu to select a tournament id or return to the report menu
        """
        print(f"\033[33m{'Modify one tournament':^120}\033[0m\n")
        choose_option = str(None)
        SwitcherChooseTournament(
            self.players_table, self.tournaments_table) \
            .option_selected(choose_option)
        while choose_option != 0:
            choose_option = choice_option()
            SwitcherChooseTournament(
                self.players_table, self.tournaments_table) \
                .option_selected(choose_option)
        report_option = str(None)
        SwitcherReportsMenu(
            self.players_table, self.tournaments_table) \
            .option_selected(report_option)

    @staticmethod
    def option_0():
        print(f"\033[95m\n{'Back to main menu':^120}\n\033[0m")
        sleep(0.5)


class SwitcherChooseTournament(SwitcherMenu):
    """
    Permit to select one id tournament to view informations about the selected tournament

    Attributes (inherited by the SwitcherMenu)
    ------
    players_table : tinydb.table.Table
    tournaments_table : tinydb.table.Table
    id_player : None (str/int)
    id_tournament : None (str/int)

    Methods
    -------
    option_selected(self, selected_option)
       method to retrieve the option chosen by the user
    option_1(self)
       Select the id tournament to modify
    option_0()
       Back to reports menu
    """
    @pre_menu
    @tournament_modify_menu
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
        select the tournament to modify
        """
        view_all_tournaments(self.tournaments_table)
        select_tournament = selected_tournament(self.tournaments_table)
        if select_tournament == 0:
            SwitcherChooseTournament(
                self.players_table,
                self.tournaments_table
            ).option_selected(str(None))
        else:
            view_tournament_option = str(None)
            SwitchedViewTournament(
                self.players_table,
                self.tournaments_table,
                select_tournament
            ).option_selected(view_tournament_option)

            while view_tournament_option != 0:
                view_tournament_option = choice_option()
                SwitchedViewTournament(
                    self.players_table,
                    self.tournaments_table,
                    self.id_tournament,
                    select_tournament
                ).option_selected(view_tournament_option)

        SwitcherChooseTournament(self.players_table, self.tournaments_table) \
            .option_selected(str(None))

    @staticmethod
    def option_0():
        """
        Back to reports menu
        """
        sleep(0.5)


class SwitchedViewTournament(SwitcherMenu):
    """
    permit to view all information about one specific tournament

    Attributes (inherited by the SwitcherMenu)
    ------
    players_table : tinydb.table.Table
    tournaments_table : tinydb.table.Table
    id_player : None (str/int)
    id_tournament : None (str/int)

    Methods
    -------
    option_selected(self, selected_option)
        method to retrieve the option chosen by the user
    option_1(self)
        view players of this tournament, by rank (scores)
    option_2(self)
        view players of this tournament, by name
    option_3(self)
        view results - round and matches
    option_4(self)
        view other informations about tournament (place, description, time control....)
    option_0()
        back to the choice id tournament id
    """
    @pre_menu
    @reports_tournament
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
        view players of this tournament, by rank (scores)
        """
        tournaments_table = deserialized_tournaments(self.tournaments_table)
        list_of_players = deserialized_players(
            self.players_table
        )
        tournament = Cet(self.id_tournament).tournament_in_progress(tournaments_table)
        tournament_str = f"Tournament : {tournament.name}"
        print(f"\033[33m{' View Players - by rank':^120}\n"
              f"{'-'*10:^120}\n"
              f"\033[91m{tournament_str:^120}\n"
              f"\033[33m{'-'*10:^120}\033[0n\n")
        view_players_tournament(tournament, list_of_players, sort_by='score')

    def option_2(self):
        """
        view players of this tournament, by name
        """
        tournaments_table = deserialized_tournaments(self.tournaments_table)
        list_of_players = deserialized_players(
            self.players_table
        )
        tournament = Cet(self.id_tournament).tournament_in_progress(tournaments_table)
        tournament_str = f"Tournament : {tournament.name}"
        print(f"\033[33m{' View Players - by family name':^120}\n"
              f"{'-' * 10:^120}\n"
              f"\033[91m{tournament_str:^120}\n"
              f"\033[33m{'-' * 10:^120}\033[0n\n")
        view_players_tournament(tournament, list_of_players, sort_by='name')

    def option_3(self):
        """
        view results - round and matches
        """
        tournaments_table = deserialized_tournaments(self.tournaments_table)
        list_of_players = deserialized_players(
            self.players_table
        )
        tournament = Cet(self.id_tournament).tournament_in_progress(tournaments_table)
        tournament_str = f"Tournament : {tournament.name}"
        print(f"\033[33m{' View List of rounds and matches':^120}\n"
              f"{'-' * 10:^120}\n"
              f"\033[91m{tournament_str:^120}\n"
              f"\033[33m{'-' * 10:^120}\033[0m\n")
        view_rounds_matches(tournament, list_of_players)

    def option_4(self):
        """
        view other informations about tournament
        """
        tournaments_table = deserialized_tournaments(self.tournaments_table)
        tournament = Cet(self.id_tournament).tournament_in_progress(tournaments_table)
        tournament_str = f"Tournament : {tournament.name}"
        print(f"\033[33m{' View other informations':^120}\n"
              f"{'-' * 10:^120}\n"
              f"\033[91m{tournament_str:^120}\n"
              f"\033[33m{'-' * 10:^120}\033[0m\n")
        report_all_informations_one_tournament(tournament)

    @staticmethod
    def option_0():
        sleep(0.5)
