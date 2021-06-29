#! /usr/bin/env python3
# coding: utf-8
""" Menus input fonctions and methode for players gestion """

from controllers.user_entry import control_sex, \
    control_ranking, control_id, control_name_surname_player
from controllers.user_entry import control_date
from controllers.backup_restore_players import \
    deserialized_players, serialized_players


def new_user():
    name = input("Name : ").upper()
    while control_name_surname_player(name) == 0:
        name = input("Name : ").upper()

    surname = input("Surname : ").capitalize()
    while control_name_surname_player(surname) == 0:
        surname = input("Surname : ").capitalize()

    date_of_birth = input("Date of birth (jj/mm/aaaa) : ")
    while control_date(date_of_birth) == 0:
        date_of_birth = input("Date of birth (jj/mm/aaaa) : ")

    sex = input("sex (M or F) : ").upper()
    while control_sex(sex) == 0:
        sex = input("sex (M or F) : ").upper()

    ranking = input("Elo rank : (Leave blank if no classification yet) ")
    while control_ranking(ranking) == 0:
        ranking = input("Elo rank : (Leave blank if no classification yet) ")

    return name, surname, date_of_birth, sex, ranking


def delete_users_validation():
    validation_delete = input("Are your sure to delete all users ?"
                              "This action is irreversible"
                              "Type 'yes' to confirm : ")
    return validation_delete


def modify_player(player_table):
    id_player = input("enter the ID player to modify : ")
    while control_id(id_player) == 0:
        id_player = input("enter the ID player to modify : ")
    result = 0
    for player in player_table:
        if player['id_player'] == int(id_player):
            result = 1

    if result == 0:
        print('Player ID not found. No changes registered')
    elif result == 1:
        list_players = deserialized_players(player_table)
        for player in list_players:
            if player.id_player == int(id_player):
                name = input(f"name [{player.name}] : ").upper()
                if name == '':
                    player.name = player.name
                else:
                    while control_name_surname_player(name) == 0:
                        name = input("name : ").upper()
                    player.name = name

                surname = input(f"surname [{player.surname}] : ").capitalize()
                if surname == '':
                    player.surname = player.surname
                else:
                    while control_name_surname_player(surname) == 0:
                        surname = input("surname : ").capitalize()
                    player.surname = surname

                date_of_birth = input(f"date of birth "
                                      f"[{player.date_of_birth}] : ")
                if date_of_birth == '':
                    player.date_of_birth = player.date_of_birth
                else:
                    while control_date(date_of_birth) == 0:
                        date_of_birth = input("Date of birth (jj/mm/aaaa) : ")
                    player.date_of_birth = date_of_birth

                sex = input(f"sex [{player.sex}] : ").upper()
                if sex == '':
                    player.sex = player.sex
                else:
                    while control_sex(sex) == 0:
                        sex = input("sex (M or F) : ").upper()
                    player.sex = sex

                ranking = input(f"Elo rank [{player.ranking}] : ")
                if ranking == '':
                    player.ranking = player.ranking
                else:
                    while control_ranking(ranking) == 0:
                        ranking = input("Elo rank : ")
                    player.ranking = ranking
        serialized_players(list_players)
