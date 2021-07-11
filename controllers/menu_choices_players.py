#! /usr/bin/env python3
# coding: utf-8
"""
Players menu choices
contains all class for make choice in the appliance about players.

Classes
-------
SwitcherPlayersMenu(SwitcherMenu)
    View menu for players gestion. Can choose an option for manage players
SwitcherModifyPlayersMenu(SwitcherMenu)
    Especially for modify one player information.
"""

from time import sleep

from controllers.backup_restore_players import (
    deserialized_players,
    serialized_players,
)
from controllers.menu_choices import SwitcherMenu
from views.decorators_menus import (
    pre_menu,
    players_menu,
    players_modify_menu,
)
from views.menu_input_players import (
    new_user,
    modify_player,
)
from views.players import view_all_players
from controllers.menu_input import choice_option
from models.player import Player


class SwitcherPlayersMenu(SwitcherMenu):
    """
    View menu for players gestion. Can choose an option for manage players

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
        Add new player
    option_2(self)
        View all players in the base
    option_3(self)
        Modify one player - open the SwitcherModifyPlayersMenu
    option_0(self)
        back to the menu to the main menu
    """
    @pre_menu
    @players_menu
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
        Add a new player on the base, according the user input.
        """
        print(f"\033[33m{'Add new player':^120}\033[0m\n")
        list_players = deserialized_players(self.players_table)
        self.id_player = len(list_players) + 1
        element_player = new_user()
        new = Player(element_player[0], element_player[1],
                     element_player[2], element_player[3],
                     self.id_player, element_player[4])
        list_players.append(new)

        self.players_table = serialized_players(list_players)

    def option_2(self):
        """
        view all player in the base
        """
        print(f"\033[33m{'View all players':^120}\033[0m\n")
        view_all_players(self.players_table)

    def option_3(self):
        """
        Modify one player - open the SwitcherModifyPlayersMenu
        """
        print(f"\033[33m{'Modify one player':^120}\033[0m\n")
        modify_option = str(None)
        SwitcherModifyPlayersMenu(
            self.players_table, self.tournaments_table)\
            .option_selected(modify_option)
        while modify_option != 0:
            modify_option = choice_option()
            SwitcherModifyPlayersMenu(
                self.players_table, self.tournaments_table)\
                .option_selected(modify_option)
        players_option = str(None)
        SwitcherPlayersMenu(
            self.players_table, self.tournaments_table)\
            .option_selected(players_option)

    def option_0(self):
        """
        Back to main menu
        """
        print(f"\033[95m\n{'Back to main menu':^120}\n\033[0m")
        sleep(0.5)


class SwitcherModifyPlayersMenu(SwitcherMenu):
    """
    View menu for players gestion. Can choose an option for manage players

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
        Select the id player to modify and make some modifications
    option_0(self)
        back to the Players gestion menu
    """
    @pre_menu
    @players_modify_menu
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
        Select the id player to modify and make some modifications
        """
        view_all_players(self.players_table)
        modify_player(self.players_table)
        SwitcherModifyPlayersMenu(
            self.players_table,
            self.tournaments_table
        ).option_selected(str('None'))

    def option_0(self):
        """
        back to the Players gestion menu
        """
        sleep(0.5)
