#! /usr/bin/env python3
# coding: utf-8


""" Ici le code final de application. """
from tinydb import TinyDB


from views.menu import Menus, clean
from controllers.control_backup_restore_players import BackupRestorePlayers as BRP
from models.player import Player

if __name__ == '__main__':
    # recupération des infos joueurs déjà existantes
    db = TinyDB('controllers/db.json')
    players_table = db.table('players')
    list_players = BRP().deserialized_players(players_table)

    #Affichage menu principal
    Menus().main_menu()
    option_player = 999
    try:
        option_principal = int(input("Enter your option: "))
    except ValueError:
        print("You must choose a number")
        option_principal = 999

    while option_principal != 0:
        if option_principal == 1:
            print(r"Option choisie : {} ".format(option_principal))
        elif option_principal == 2:
            # Menu gestion player affiché
            Menus().players_menu()
            while option_player != 0:
                try:
                    option_player = int(input("Enter your option: "))
                except ValueError:
                    print("You must choose a number")
                    option_player = 999
                if option_player == 1:  # correspond à l'ajout d'un nouveau player
                    id_player = len(list_players)+1
                    player = Menus().new_user()
                    Menus().players_menu()
                    new_player = Player(id_player, player[0], player[1], player[2], player[3], player[4])
                    list_players.append(new_player)
                    players_table = BRP().serialized_players(list_players)
                    print(r"Add player OK, number of existing players : {}".format(len(list_players)))
                elif option_player == 2:  # view all users
                    Menus().view_all_users(players_table)
                    pass
                elif option_player == 3:  # modify one player
                    pass
                else:
                    print("You must choose an existing option")

        else:
            print("You must choose an existing option")

        Menus().main_menu()
        try:
            option_principal = int(input("Enter your option: "))
        except ValueError:
            print("Vous devez choisir un chiffre")
            option_principal = 999

    print("\nBonne fin de journée et à bientôt")
