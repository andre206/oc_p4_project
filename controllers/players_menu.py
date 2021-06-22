#! /usr/bin/env python3
# coding: utf-8
""" Players menu choices """

from views.decorators_menus import pre_menu
from views.decorators_menus import players_menu
from views.menu import PlayersMenu as PM
from controllers.main_menu import SwitcherMainMenu as SMM
from controllers.backup_restore_players import BackupRestorePlayers as BRP
from models.player import Player


class SwitcherPlayersMenu(SMM):
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

        print("Add new player")
        list_players = BRP().deserialized_players(self.players_table)
        id_player = len(list_players)+1

        element_player = PM().new_user()
        new_user = Player(element_player[0], element_player[1], element_player[3], id_player, element_player[4])
        list_players.append(new_user)
        self.players_table = BRP().serialized_players(list_players)


    def option_2(self):
        print("View all players")
        PM().view_all_users(self.players_table)

    def option_3(self):
        print("Modify one player")


    def option_4(self):
        print("Delete all players")
        PM().delete_all_user()

    def option_0(self):
        print("Return principal menu")


if __name__ == '__main__':
    pass
