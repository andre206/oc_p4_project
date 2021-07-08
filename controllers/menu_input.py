#! /usr/bin/env python3
# coding: utf-8
""" Menus input fonction - """
from time import sleep

from controllers.user_entry import control_id

def choice_option():
    try:
        option = int(input(f"\033[95mEnter your choice : \033[0m"))
    except ValueError:
        print("\033[91mYou must choose a number\033[91m")
        sleep(0.5)
        option = None
    return option


def selected_tournament(tournament_table):
    id_tournament = input("Enter the ID Tournament to modify : ")
    while control_id(id_tournament) == 0:
        id_tournament = input("Enter the ID Tournament to modify : ")
    result = 0
    for tournament in tournament_table:
        if tournament['id_tournament'] == int(id_tournament):
            result = id_tournament

    if result == 0:
        print('Tournament ID not found. No changes registered')
        sleep(1)

    return result