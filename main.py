#! /usr/bin/env python3
# coding: utf-8


""" Ici le code final de application. """
import time

from tinydb import TinyDB

from views.menu import PrincipalMenu, PlayersMenu
from controllers.control_backup_restore_players import BackupRestorePlayers as BRP
from models.player import Player

if __name__ == '__main__':

    # recuperation of users information in the database
    db = TinyDB('controllers/db.json')
    players_table = db.table('players')
    list_players = BRP().deserialized_players(players_table)

    principal_option = None

    while principal_option != 0:
        PrincipalMenu().main_menu()
        try:
            principal_option = int(input("Enter your option P: "))
        except ValueError:
            print("You must choose a number")
            principal_option = None
        if principal_option == 1:
            print(r"Option choisie : {} ".format(principal_option))
        elif principal_option == 2:
            # Menu gestion player affiché
            PlayersMenu().players_menu()
            player_option = None
            while player_option != 0:
                try:
                    player_option = int(input("Enter your option Play: "))
                except ValueError:
                    print("You must choose a number")
                    player_option = None

                if player_option == 1:  # correspond à l'ajout d'un nouveau player
                    id_player = len(list_players) + 1
                    player = PlayersMenu().new_user()
                    PlayersMenu().players_menu()
                    new_player = Player(id_player, player[0], player[1], player[2], player[3], player[4])
                    list_players.append(new_player)
                    players_table = BRP().serialized_players(list_players)
                    print(r"Add player OK, number of existing players : {}".format(len(list_players)))
                elif player_option == 2:  # view all players
                    PlayersMenu().players_menu()
                    PlayersMenu().view_all_users(players_table)
                elif player_option == 3:  # modify one player
                    pass
                elif player_option == 4:  # delete all players
                    validation_delete = PlayersMenu().delete_all_user()
                    BRP().delete_all_users(validation_delete, players_table)
                elif player_option == 0:
                    print('end of users gestion')
                    time.sleep(1)
                else:
                    print("You must choose an existing option")
                    player_option = None
            player_option = None
        elif principal_option == 0:
            print('end of chess tournament program')
            time.sleep(1)
        else:
            print("You must choose an existing option")
            principal_option = None
    print("\n{:^103s}".format("Have a nice day and see you soon."))
