#! /usr/bin/env python3
# coding: utf-8
""" Menus input fonctions and methode"""

from controllers.user_entry import control_sex, control_ranking, control_id_player, control_name_surname_player
from controllers.user_entry import control_date_of_birth
from controllers.backup_restore_players import deserialized_players, serialized_players


def choice_option():
    try:
        option = int(input("Enter your choice : "))
    except ValueError:
        print("You must choose a number")
        option = None
    return option


def new_user():
    name = input("Name : ").upper()
    while control_name_surname_player(name) == 0:
        name = input("Name : ").upper()

    surname = input("Surname : ").capitalize()
    while control_name_surname_player(surname) == 0:
        surname = input("Surname : ").capitalize()

    date_of_birth = input("Date of birth (jj/mm/aaaa) : ")
    while control_date_of_birth(date_of_birth) == 0:
        date_of_birth = input("Date of birth (jj/mm/aaaa) : ")

    sex = input("sex (M or F) : ").upper()
    while control_sex(sex) == 0:
        sex = input("sex (M or F) : ").upper()

    ranking = input("Elo rank : (Leave blank if no classification yet) ")
    while control_ranking(ranking) == 0:
        ranking = input("Elo rank : (Leave blank if no classification yet) ")

    return name, surname, date_of_birth, sex, ranking


def view_all_users(player_table):
    print(f"|{'-' * 118}|\n"
          f"|{'ID Player':18}|{'Name':<19}|{'Surname':<19}"
          f"|{'Date of birth':19}|{'Sex':19}|{'Elo rank':19}|"
          f"|{'-' * 118}|"
          )

    for player in player_table:
        print(f"|{player['id_player']:^18}|{player['name'][0:19]:<19}"
              f"|{player['surname'][0:19]:<19}|{player['date_of_birth']:^19}"
              f"|{player['sex']:^19}|{player['ranking']:^19}|"
              f"|{'-' * 118}|"
              )


def delete_users_validation():
    validation_delete = input("Are your sure to delete all users ?"
                              "This action is irreversible"
                              "Type 'yes' to confirm : ")
    return validation_delete


def modify_player(player_table):
    id_player = input("enter the ID player to modify : ")
    while control_id_player(id_player) == 0:
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
                        name = input(f"name : ").upper()
                    player.name = name

                surname = input(f"surname [{player.surname}] : ").capitalize()
                if surname == '':
                    player.surname = player.surname
                else:
                    while control_name_surname_player(surname) == 0:
                        surname = input(f"surname : ").capitalize()
                    player.surname = surname

                date_of_birth = input(f"date of birth [{player.date_of_birth}] : ")
                if date_of_birth == '':
                    player.date_of_birth = player.date_of_birth
                else:
                    while control_date_of_birth(date_of_birth) == 0:
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


def new_tournament():
    name = input(f"Name of tournament : ")
    place = input(f"Place :")
    date = input(f"Date : ")
    control_time = input(f"[1] bullet, [2] blitz, [3]quick hit : ")
    description = input(f"Description : ")
    number_of_round = input(f"Number of round [4] : ")
    tournament = [name, place, date, control_time, description, number_of_round]

    return tournament


"""
player_data = db.get(doc_id=1)  # c'est un dictionnaire

player_data["name"]  # manipulation directe du dictionnaire - pas pratique car pas d'autocomplétion et plus verbeux

player = Player(**player_data)  # transmition des clés/valeurs du dictionnaire à l'initialisation d'un objet Player
player.name  # utilisation de la POO pour accéder aux valeurs
player.save()  # on peut aussi utiliser des méthodes, chose impossible en manipulant directement le dictionnaire"""
