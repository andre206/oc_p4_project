#! /usr/bin/env python3
# coding: utf-8
""" Menus input fonctions and methode for tournament gestion"""
from controllers.new_tournament import control_name_place_tournament, control_time_control, control_number_of_round
from controllers.user_entry import control_date


def new_tournament():
    """
    Function for input new tournament. Do not concerne the list of players or list of round,
    it's after for these entries.
    """
    name = input(f"Name of tournament : ")
    while control_name_place_tournament(name) == 0:
        name = input(f"Name of tournament : ")
    place = input(f"Place :").upper()
    while control_name_place_tournament(place) == 0:
        place = input(f"Place :").upper()

    date_debut = input(f"Date de début : ")
    while control_date(date_debut) == 0:
        date_debut = input(f"Date de début : ")
    date_fin = input(f"Date de fin [{date_debut}]: ")
    if date_fin == '':
        date_fin = date_debut
    else:
        while control_date(date_fin) == 0:
            date_fin = input(f"Date de fin : ")
    control_time = input(f"[1] bullet, [2] blitz, [3]quick hit : ")
    while control_time_control(control_time) == 0:
        control_time = input(f"[1] bullet, [2] blitz, [3]quick hit : ")
    control_time = control_time_control(control_time)
    print(control_time)
    description = input(f"Description : ")
    number_of_round = input(f"Number of round [4] : ")
    if number_of_round == 0:
        number_of_round = 4
    else:
        while control_number_of_round(number_of_round) == 0:
            number_of_round = input(f"Number of round : ")

    date_tournament = [date_debut, date_fin]
    tournament = [name, place, date_tournament, control_time, description, number_of_round]

    return tournament