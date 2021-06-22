#! /usr/bin/env python3
# coding: utf-8
""" Main menu choices"""

from views.decorators_menus import pre_menu
from views.decorators_menus import main_menu
from views.decorators_menus import players_menu
from views.menu import choice_option
from views.menu import PlayersMenu as PM
from controllers.backup_restore_players import BackupRestorePlayers as BRP
from models.player import Player



class SwitcherMainMenu:

    def __init__(self, players_table):
        self.players_table = players_table

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
        print("It's the first option, take it easy !")

    def main_option_2(self):
        """
        This option is the Players menu.
        It This will launch the players menu, with the option choices for the players menu.
        As soon as the user chooses option 0, it will automatically return to the main menu.
        """
        print("It's the second option, take it easy !")
        players_option = None
        SwitcherPlayersMenu(self.players_table).option_selected(players_option)
        while players_option != 0:
            players_option = choice_option()
            SwitcherPlayersMenu(self.players_table).option_selected(players_option)
        main_option = None
        SwitcherMainMenu(self.players_table).option_selected(main_option)

    def main_option_3(self):
        print("Its the third option, oh yeah !")

    def main_option_0(self):
        print("It's over... Bye !")


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
        list_players = BRP().deserialized_players(self.players_table)
        id_player = len(list_players) + 1
        element_player = PM().new_user()
        new_user = Player(element_player[0], element_player[1], element_player[2], element_player[3],
                          id_player, element_player[4])
        list_players.append(new_user)

        self.players_table = BRP().serialized_players(list_players)

    def option_2(self):
        print(f"{'View all players':^120}\n")
        PM().view_all_users(self.players_table)

    def option_3(self):
        print(f"{'Modify one player':^120}\n")

    def option_4(self):
        print(f"{'Delete all players':^120}\n")
        delete_response = PM().delete_all_user()
        BRP().delete_all_users(delete_response, self.players_table)

    def option_0(self):
        print("Return principal menu")


if __name__ == '__main__':
    pass
