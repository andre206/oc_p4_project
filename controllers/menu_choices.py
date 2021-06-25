#! /usr/bin/env python3
# coding: utf-8
""" Main menu choices
contains all class for make choice in the appliance.
"""
from time import sleep

from views.decorators_menus import pre_menu, main_menu, players_menu, players_modify_menu, \
    tournament_menu, tournament_modify_menu
from views.menu_input import choice_option
from views.menu_input_players import new_user,  modify_player, delete_users_validation
from views.menu_input_tournament import new_tournament
from views.view_players import view_all_users
from views.view_tournaments import view_all_tournaments
from controllers.backup_restore_players import deserialized_players, serialized_players, delete_all_users
from controllers.backup_restore_tournament import deserialized_tournaments, serialized_tournaments
from models.player import Player
from models.tournament import Tournament


class SwitcherMainMenu:

    def __init__(self, players_table, tournaments_table, id_player=None, id_tournament=None):
        self.players_table = players_table
        self.tournaments_table = tournaments_table
        self.id_player = id_player
        self.id_tournament = id_tournament

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
        print(f"{'Tournament gestion':^120}\n")
        tournament_option = None
        SwitcherTournamentMenu(self.players_table, self.tournaments_table).option_selected(tournament_option)
        while tournament_option != 0:
            tournament_option = choice_option()
            SwitcherTournamentMenu(self.players_table, self.tournaments_table).option_selected(tournament_option)
        main_option = None
        SwitcherMainMenu(self.players_table, self.tournaments_table).option_selected(main_option)

    def main_option_2(self):
        """
        This option is the Players menu.
        It This will launch the players menu, with the option choices for the players menu.
        As soon as the user chooses option 0, it will automatically return to the main menu.
        """
        print(f"{'Players gestion':^120}\n")
        players_option = None
        SwitcherPlayersMenu(self.players_table, self.tournaments_table).option_selected(players_option)
        while players_option != 0:
            players_option = choice_option()
            SwitcherPlayersMenu(self.players_table, self.tournaments_table).option_selected(players_option)
        main_option = None
        SwitcherMainMenu(self.players_table, self.tournaments_table).option_selected(main_option)

    def main_option_3(self):
        print(f"{'Reports':^120}\n")

    def main_option_0(self):
        print(f"\n{'Have a nice day and see you soon':^120}")


class SwitcherTournamentMenu(SwitcherMainMenu):
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



class SwitcherPlayersMenu(SwitcherMainMenu):
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
        print(f"{'Add new player':^120}\n")
        list_players = deserialized_players(self.players_table)
        self.id_player = len(list_players) + 1
        element_player = new_user()
        new = Player(element_player[0], element_player[1], element_player[2], element_player[3],
                     self.id_player, element_player[4])
        list_players.append(new)

        self.players_table = serialized_players(list_players)

    def option_2(self):
        print(f"{'View all players':^120}\n")
        view_all_users(self.players_table)

    def option_3(self):
        print(f"{'Modify one player':^120}\n")
        modify_option = None
        SwitcherModifyPlayersMenu(self.players_table, self.tournaments_table).option_selected(modify_option)
        while modify_option != 0:
            modify_option = choice_option()
            SwitcherModifyPlayersMenu(self.players_table, self.tournaments_table).option_selected(modify_option)
        players_option = None
        SwitcherPlayersMenu(self.players_table, self.tournaments_table).option_selected(players_option)

    def option_4(self):
        print(f"{'Delete all players':^120}\n")
        delete_response = delete_users_validation()
        delete_all_users(delete_response, self.players_table)

    def option_0(self):
        print(f"\n{'Back to main menu':^120}\n")
        sleep(1)


class SwitcherModifyPlayersMenu(SwitcherMainMenu):
    @pre_menu
    @players_modify_menu
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
        view_all_users(self.players_table)
        modify_player(self.players_table)

    def option_0(self):
        print(f"\n{'Back to players menu':^120}")
        sleep(1)


class SwitcherModifyTournament(SwitcherMainMenu):
    @pre_menu
    @tournament_modify_menu
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
        view_all_tournaments(self.tournaments_table)
        pass

    def option_0(self):
        print(f"\n{'Back to tournament menu':^120}")
        sleep(1)