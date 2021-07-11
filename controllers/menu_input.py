#! /usr/bin/env python3
# coding: utf-8
"""
Menus input functions -

Functions
---------
choice_option()
    for input the user option
selected_tournament(tournament_table)
    for selected a specific tournament

"""
from time import sleep

from controllers.user_entry import control_id


def choice_option():
    """
    test the option input by user

    Raises
    ------
    ValueError
        the input must be an integer

    Returns
    option : int
        the option chosen by user
    """
    try:
        option = int(input("\033[95mEnter your choice : \033[0m"))
    except ValueError:
        print("\033[91mYou must choose a number\033[91m")
        sleep(0.5)
        option = None
    return option


def selected_tournament(tournament_table):
    """
    for selected a specific tournament

    Parameters
    ----------
    tournament_table : tinydb.table.Table
        tournament table

    Returns
    -------
    result : str(int)
        the id tournament selected by user
        0 if id not found
    """
    id_tournament = input("Enter the ID Tournament to modify : ")
    while control_id(id_tournament) == 0:
        id_tournament = input("Enter the ID Tournament to modify : ")
    result = 0
    for tournament in tournament_table:
        if tournament['id_tournament'] == int(id_tournament):
            result = id_tournament

    if result == 0:
        print('\033[91mTournament ID not found. \033[33mNo changes registered\033[0m')
        sleep(0.5)

    return result
