#! /usr/bin/env python3
# coding: utf-8
""" Tournament menu choices
contains all class for make choice in the appliance about tournament.
"""
from time import sleep

from controllers.menu_choices import SwitcherMenu
from controllers.backup_restore_tournament import (
    deserialized_tournaments,
    serialized_tournaments,
)
from views.decorators_menus import (
    pre_menu,
    tournament_menu,
    tournament_modify_menu,
    tournament_modify_sub_menu,
)
from controllers.menu_input import choice_option
from views.menu_input_tournament import (
    new_tournament,
    modify_tournament,
)
from views.view_tournaments import view_all_tournaments
from models.tournament import Tournament


class SwitcherTournamentMenu(SwitcherMenu):
    @pre_menu
    @tournament_menu
    def option_selected(self, selected_option):
        super().option_selected(selected_option)

    def option_1(self):
        print(f"{'Add new tournament':^120}\n")
        list_tournament = deserialized_tournaments(self.tournaments_table)
        self.id_tournament = len(list_tournament) + 1
        element_tournament = new_tournament()
        new = Tournament(element_tournament[0], element_tournament[1],
                         element_tournament[2], element_tournament[3],
                         element_tournament[4], self.id_tournament)
        list_tournament.append(new)

        self.tournaments_table = serialized_tournaments(list_tournament)

    def option_2(self):
        print(f"{'View all tournament':^120}\n")
        view_all_tournaments(self.tournaments_table)

    def option_3(self):
        print(f"{'Modify one tournament':^120}\n")
        modify_option = None
        SwitcherModifyTournament(
            self.players_table, self.tournaments_table) \
            .option_selected(modify_option)
        while modify_option != 0:
            modify_option = choice_option()
            SwitcherModifyTournament(
                self.players_table, self.tournaments_table) \
                .option_selected(modify_option)
        tournament_option = None
        SwitcherTournamentMenu(
            self.players_table, self.tournaments_table) \
            .option_selected(tournament_option)

    def option_0(self):
        print(f"\n{'Back to main menu':^120}\n")
        sleep(1)


class SwitcherModifyTournament(SwitcherMenu):


    @pre_menu
    @tournament_modify_menu
    def option_selected(self, selected_option):
        super().option_selected(selected_option)

    def option_1(self):
        """
        select the tournament to modify
        """
        view_all_tournaments(self.tournaments_table)
        select_tournament = modify_tournament(self.tournaments_table)
        if select_tournament == 0:
            SwitcherModifyTournament(self.players_table, self.tournaments_table).option_selected(0)
        else:
            print(select_tournament)
            sleep(3)
            sub_modify_tournament_option = None
            SwitcherModifyTournamentSub(
                self.players_table,
                self.tournaments_table,
                select_tournament
            ).option_selected(sub_modify_tournament_option)

            while sub_modify_tournament_option != 0:
                sub_modify_tournament_option = choice_option()
                SwitcherModifyTournamentSub(
                    self.players_table,
                    self.tournaments_table,
                    select_tournament
                    ).option_selected(sub_modify_tournament_option)

        SwitcherModifyTournament(self.players_table, self.tournaments_table) \
            .option_selected(0)

    def option_0(self):
        sleep(0.5)


class SwitcherModifyTournamentSub(SwitcherMenu):
    @pre_menu
    @tournament_modify_sub_menu
    def option_selected(self, selected_option):
        super().option_selected(selected_option)

    def option_1(self):
        """
        Add players on tournament
        - search in the players database the registred players.
        - if it si not 8 players, redirection to the add players
        in the player gestion
        """
        print(f" Add players on tournament {self.id_tournament}\n")
        pass

    def option_2(self):
        """
        Starting Round
        - search the existing rounds for the tournament,
        - initialize the next one by looking at the maximum
        number of rounds defined at the creation of the tournament
        - add a start date and hour
        - generate the matches for the round
        - Save the round in the tournament round list
        """
        print(f"{'Starting Round':^120}\n")
        pass

    def option_3(self):
        """
        Ending Round and add results
        -select the round that does not yet have an end date
        -enter the scores of the matches
        -add the end date and time
        -save the round in the tournament rounds list
        """
        print(f"{'Ending Round and add results':^120}\n")
        pass

    def option_0(self):
        sleep(0.5)
