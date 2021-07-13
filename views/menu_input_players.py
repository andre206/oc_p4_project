#! /usr/bin/env python3
# coding: utf-8
"""
Menus input functions for players gestion

Functions
---------
new_user()
    to add a new user
modify_player(player_table)
    to modify an existent player
"""

from time import sleep

from controllers.user_entry import ControlGlobalEntry as Cge
from models.backup_restore_players import (
    deserialized_players,
    serialized_players,
)


def new_user():
    """
    To add a new player

    Returns
    -------
    name: str
        name input after control
    first_name: str
        first_name input after control
    date_of_birth: str
        date of birth input after control, must be as a datetime
    sex: str
        sex input after control
    ranking: str
        ranking input after control, if no entry ==> 1000
    """
    name = input("Name : ").upper()
    while Cge(name).control_name_player() == 0:
        name = input("Name : ").upper()

    first_name = input("First name : ").capitalize()
    while Cge(first_name).control_name_player() == 0:
        first_name = input("First name : ").capitalize()

    date_of_birth = input("Date of birth (jj/mm/aaaa) : ")
    while Cge(date_of_birth).control_date() == 0:
        date_of_birth = input("Date of birth (jj/mm/aaaa) : ")

    sex = input("sex (M or F) : ").upper()
    while Cge(sex).control_sex() == 0:
        sex = input("sex (M or F) : ").upper()

    ranking = input("Elo rank : (Leave blank if no classification yet) ")
    if ranking == '' or int(ranking) == 0:
        ranking = 1000
    while Cge(ranking).control_ranking() == 0:
        ranking = input("Elo rank : (Leave blank if no classification yet) ")
        if ranking == '' or int(ranking) == 0:
            ranking = 1000
    return name, first_name, date_of_birth, sex, ranking


def modify_player(player_table):
    """
    To modify a player

    no return, the modification will be directly registered in the database
    """
    id_player = input("enter the ID player to modify : ")
    while Cge(id_player).control_id() == 0:
        id_player = input("enter the ID player to modify : ")
    result = 0
    for player in player_table:
        if player['id_player'] == int(id_player):
            result = 1

    if result == 0:
        print('Player ID not found. No changes registered')
        sleep(1)
    elif result == 1:
        list_players = deserialized_players(player_table)
        for player in list_players:
            if player.id_player == int(id_player):
                name = input(f"name [{player.name}] : ").upper()
                if name == '':
                    player.name = player.name
                else:
                    while Cge(name).control_name_player() == 0:
                        name = input("name : ").upper()
                    player.name = name

                first_name = input(f"First name [{player.first_name}] : ").capitalize()
                if first_name == '':
                    player.first_name = player.first_name
                else:
                    while Cge(first_name).control_name_player() == 0:
                        first_name = input("First name : ").capitalize()
                    player.first_name = first_name

                date_of_birth = input(f"date of birth "
                                      f"[{player.date_of_birth}] : ")
                if date_of_birth == '':
                    player.date_of_birth = player.date_of_birth
                else:
                    while Cge(date_of_birth).control_date() == 0:
                        date_of_birth = input("Date of birth (jj/mm/aaaa) : ")
                    player.date_of_birth = date_of_birth

                sex = input(f"sex [{player.sex}] : ").upper()
                if sex == '':
                    player.sex = player.sex
                else:
                    while Cge(sex).control_sex() == 0:
                        sex = input("sex (M or F) : ").upper()
                    player.sex = sex

                ranking = input(f"Elo rank [{player.ranking}] : ")
                if ranking == '':
                    player.ranking = player.ranking
                else:
                    while Cge(ranking).control_ranking() == 0:
                        ranking = input("Elo rank : ")
                    player.ranking = ranking
        serialized_players(list_players)
