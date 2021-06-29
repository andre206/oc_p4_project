#! /usr/bin/env python3
# coding: utf-8
""" Menus input fonctions and methode for tournament gestion"""
from time import sleep
from controllers.new_tournament import control_name_place_tournament
from controllers.new_tournament import control_time_control
from controllers.new_tournament import control_number_of_round
from controllers.user_entry import control_date, control_id


def new_tournament():
    """
    Function for input new tournament.
    Do not concerne the list of players or list of round,
    it's after for these entries.
    """
    name = input("Name of tournament : ")
    while control_name_place_tournament(name) == 0:
        name = input("Name of tournament : ")
    place = input("Place :").upper()
    while control_name_place_tournament(place) == 0:
        place = input("Place :").upper()

    date_debut = input("Date de début : ")
    while control_date(date_debut) == 0:
        date_debut = input("Date de début : ")
    date_fin = input(f"Date de fin [{date_debut}]: ")
    if date_fin == '':
        date_fin = date_debut
    else:
        while control_date(date_fin) == 0:
            date_fin = input("Date de fin : ")
    control_time = input("[1] bullet, [2] blitz, [3]quick hit : ")
    while control_time_control(control_time) == 0:
        control_time = input("[1] bullet, [2] blitz, [3]quick hit : ")
    control_time = control_time_control(control_time)
    print(control_time)
    description = input("Description : ")
    number_of_round = input("Number of round [4] : ")
    if number_of_round == 0:
        number_of_round = 4
    else:
        while control_number_of_round(number_of_round) == 0:
            number_of_round = input("Number of round : ")

    date_tournament = [date_debut, date_fin]
    tournament = [name, place, date_tournament, control_time,
                  description, number_of_round]

    return tournament


def modify_tournament(tournament_table):
    id_tournament = input("enter the ID Tournament to modify : ")
    while control_id(id_tournament) == 0:
        id_tournament = input("enter the ID Tournament to modify : ")
    result = 0
    for tournament in tournament_table:
        if tournament['id_tournament'] == int(id_tournament):
            result = id_tournament

    if result == 0:
        print('Tournament ID not found. No changes registered')
        sleep(1)

    return result
