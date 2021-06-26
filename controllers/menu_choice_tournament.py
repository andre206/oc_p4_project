#! /usr/bin/env python3
# coding: utf-8
""" Tournament menu choices
contains all class for make choice in the appliance about tournament.
"""
from time import sleep

from controllers.menu_choices import SwitcherMenu
from controllers.backup_restore_tournament import deserialized_tournaments, serialized_tournaments
from views.decorators_menus import pre_menu, tournament_menu, tournament_modify_menu, tournament_modify_sub_menu
from views.menu_input import choice_option
from views.menu_input_tournament import new_tournament
from views.view_tournaments import view_all_tournaments
from models.tournament import Tournament


class SwitcherTournamentMenu(SwitcherMenu):
    @pre_menu
    @tournament_menu
    def option_selected(self, selected_option):
        """
        method to launch the appropriate methods according to the user's choice.
        Depending on the choice, a return is sent to the display.
        About choice in the main menu.
        """
        option_name = f"option_{str(selected_option)}"
        option = getattr(self, option_name, lambda: "Invalid option")
        return option()

    def option_1(self):
        print(f"{'Add new tournament':^120}\n")
        list_tournament = deserialized_tournaments(self.tournaments_table)
        self.id_tournament = len(list_tournament) + 1
        element_tournament = new_tournament()
        new = Tournament(element_tournament[0], element_tournament[1], element_tournament[2], element_tournament[3],
                         element_tournament[4], self.id_tournament)
        list_tournament.append(new)

        self.tournaments_table = serialized_tournaments(list_tournament)

    def option_2(self):
        print(f"{'View all tournament':^120}\n")
        view_all_tournaments(self.tournaments_table)

    def option_3(self):
        print(f"{'Modify one tournament':^120}\n")
        modify_option = None
        SwitcherModifyTournament(self.players_table, self.tournaments_table).option_selected(modify_option)
        while modify_option != 0:
            modify_option = choice_option()
            SwitcherModifyTournament(self.players_table, self.tournaments_table).option_selected(modify_option)
        tournament_option = None
        SwitcherTournamentMenu(self.players_table, self.tournaments_table).option_selected(tournament_option)

    def option_0(self):
        print(f"\n{'Back to main menu':^120}\n")
        sleep(1)


class SwitcherModifyTournament(SwitcherMenu):
    @pre_menu
    @tournament_modify_menu
    def option_selected(self, selected_option):
        """
        method to launch the appropriate methods according to the user's choice.
        Depending on the choice, a return is sent to the display.
        About choice in the main menu.
        """
        option_name = f"option_{str(selected_option)}"
        option = getattr(self, option_name, lambda: "Invalid option")
        return option()

    def option_1(self):
        view_all_tournaments(self.tournaments_table)
        pass

    def option_0(self):
        print(f"\n{'Back to tournament menu':^120}")
        sleep(1)
