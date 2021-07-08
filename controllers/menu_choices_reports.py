#! /usr/bin/env python3
# coding: utf-8
""" Reports menu choices
contains all class for make choice in the appliance about reports.
"""
from time import sleep

from controllers.menu_choices import SwitcherMenu
from controllers.new_tournament import tournament_in_progress
from controllers.menu_input import (
    choice_option,
    selected_tournament,
)
from controllers.backup_restore_tournament import (
    deserialized_tournaments
)
from views.decorators_menus import (
    pre_menu,
    reports_menu,
    reports_tournament,
    tournament_modify_menu
)
from views.view_players import (
    view_all_players,
)
from views.view_tournaments import (
    view_all_tournaments,
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
        Export informations in a PDF file
        Not implemented yet
        """
        pass

    def option_5(self):
        """
        Display the menu to select a tournament id or return to the report menu
        """
        print(f"\033[33m{'Modify one tournament':^120}\033[0m\n")
        choose_option = None
        SwitcherChooseTournament(
            self.players_table, self.tournaments_table) \
            .option_selected(choose_option)
        while choose_option != 0:
            choose_option = choice_option()
            SwitcherChooseTournament(
                self.players_table, self.tournaments_table) \
                .option_selected(choose_option)
        report_option = None
        SwitcherReportsMenu(
            self.players_table, self.tournaments_table) \
            .option_selected(report_option)

        pass

    def option_0(self):
        print(f"\033[95m\n{'Back to main menu':^120}\n\033[0m")
        sleep(0.5)


class SwitcherChooseTournament(SwitcherMenu):

    @pre_menu
    @tournament_modify_menu
    def option_selected(self, selected_option):
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
            ).option_selected(0)
        else:
            view_tournament_option = None
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
            .option_selected(0)

    def option_0(self):
        sleep(0.5)


class SwitchedViewTournament(SwitcherMenu):
    @pre_menu
    @reports_tournament
    def option_selected(self, selected_option):
        super().option_selected(selected_option)

    def option_1(self):
        """
        view players of this tournament, by rank (scores)
        """
        tournaments_table = deserialized_tournaments(self.tournaments_table)
        tournament = tournament_in_progress(tournaments_table, int(self.id_tournament))
        tournament_str = f"Tournament : {tournament.name}"
        print(f"\033[33m{' View Players - by rank':^120}\n"
              f"{'-'*10:^120}\n"
              f"\033[91m{tournament_str:^120}\n"
              f"\033[33m{'-'*10:^120}\033[0n\n")
"""
f"\033[33m|{'Reports':^118}|\n"
              f"|{'-' * 118}|\n|{'-' * 118}|\n"
              f"|{' ':>45}\033[91m[1]\033[33m{' View Players - by rank':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[2]\033[33m{' View Players - by name':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[3]\033[33m"
              f"{' View List of rounds ans matches':<38s}"
              f"{' ':>32}|\n"
              f"|{' ':>45}\033[91m[4]\033[33m"
              f"{' Export informations in a PDF file':<38s}"
              f"{' ':>32}|\n"
              f"|{' ':>45}\033[91m[0]\033[33m"
              f"{' Return Tournament gestion':<30s}{' ':>40}|\n"
              f"|{'-' * 118}|\033[0m\n"
"""
