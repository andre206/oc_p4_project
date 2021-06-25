#! /usr/bin/env python3
# coding: utf-8
""" Menus input fonctions and methode for tournament gestion"""

def new_tournament():
    name = input(f"Name of tournament : ")
    place = input(f"Place :")
    date = input(f"Date : ")
    control_time = input(f"[1] bullet, [2] blitz, [3]quick hit : ")
    description = input(f"Description : ")
    number_of_round = input(f"Number of round [4] : ")
    tournament = [name, place, date, control_time, description, number_of_round]

    return tournament