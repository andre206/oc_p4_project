#! /usr/bin/env python3
# coding: utf-8
"""
Module for views on the top of the console
"""

import platform
import os


def clean():
    """For clean the console display"""
    p = platform.system()
    commands = {"Windows": "cls", "Linux": "clear", "Darwin": "clear"}
    try:
        os.system(commands[p])
    except ValueError:  # empty string or Java os name
        print(chr(27) + "[2J")


def pre_menu(on_top):
    """ for the title of the appliance"""

    def before_menu(*args, **kwargs):
        clean()
        print(f"|{'-' * 118}|\n"
              f"| @ @@ @ {' ' * 102} @ @@ @ |\n"
              f"| @@@@@@ {' ' * 102} @@@@@@ |\n"
              f"|   @@   {' ' * 39} {'#' * 22} {' ' * 39}   @@   |\n"
              f"|  @@@@  {' ' * 39} ## Chess Tournament ## {' ' * 39}"
              f"  @@@@  |\n"
              f"| @@@@@@ {' ' * 39} {'#' * 22} {' ' * 39} @@@@@@ |\n"
              f"|@@@@@@@@{' ' * 102}@@@@@@@@|\n"
              f"|{'-' * 118}|"
              )
        on_top(*args, **kwargs)

    return before_menu


def main_menu(on_top):
    """
    print the main menu
    """

    def before_main_choice(*args, **kwargs):
        print(f"|{'Principal Menu':^118}|\n"
              f"|{'-' * 118}|\n|{'-' * 118}|\n"
              f"|{' ':>45}{'[1] Tournament gestion':<30s}{' ':>43}|\n"
              f"|{' ':>45}{'[2] Players gestion':<30s}{' ':>43}|\n"
              f"|{' ':>45}{'[3] Reports':<30s}{' ':>43}|\n"
              f"|{' ':>45}{'[0] Exit Chess Tournament':<30s}{' ':>43}|\n"
              f"|{'-' * 118}|"
              )
        on_top(*args, **kwargs)

    return before_main_choice


def players_menu(on_top):
    """ print the player menu on the console
    """

    def before_players_choice(*args, **kwargs):
        print(f"|{'Player gestion':^118}|\n"
              f"|{'-' * 118}|\n|{'-' * 118}|\n"
              f"|{' ':>45}{'[1] Add new player':<30s}{' ':>43}|\n"
              f"|{' ':>45}{'[2] View all players':<30s}{' ':>43}|\n"
              f"|{' ':>45}{'[3] Modify one player':<30s}{' ':>43}|\n"
              f"|{' ':>45}{'[4] Delete all players':<30s}{' ':>43}|\n"
              f"|{' ':>45}{'[0] Return principal menu':<30s}{' ':>43}|\n"
              f"|{'-' * 118}|"
              )
        on_top(*args, **kwargs)

    return before_players_choice


def players_modify_menu(on_top):
    """ print the modify menu on the console
    """

    def before_modify_choice(*args, **kwargs):
        print(f"|{'Modify player':^118}|\n"
              f"|{'-' * 118}|\n|{'-' * 118}|\n"
              f"|{' ':>45}{'[1] Choose the ID player to modify':<30s}"
              f"{' ':>39}|\n"
              f"|{' ':>45}{'[0] Return Player gestion':<30s}{' ':>43}|\n"
              f"|{'-' * 118}|"
              )
        on_top(*args, **kwargs)

    return before_modify_choice


def tournament_menu(on_top):
    """ print the modify menu on the console
    """

    def before_tournament_choice(*args, **kwargs):
        print(f"|{'Tournament gestion':^118}|\n"
              f"|{'-' * 118}|\n|{'-' * 118}|\n"
              f"|{' ':>45}{'[1] Add new tournament':<30s}{' ':>43}|\n"
              f"|{' ':>45}{'[2] View all tournament':<30s}{' ':>43}|\n"
              f"|{' ':>45}{'[3] Modify one tournament':<30s}{' ':>43}|\n"
              f"|{' ':>45}{'[0] Return principal menu':<30s}{' ':>43}|\n"
              f"|{'-' * 118}|"
              )
        on_top(*args, **kwargs)

    return before_tournament_choice


def tournament_modify_menu(on_top):
    """ print the modify menu on the console
    """

    def before_modify_choice(*args, **kwargs):
        print(f"|{'Modify Tournament':^118}|\n"
              f"|{'-' * 118}|\n|{'-' * 118}|\n"
              f"|{' ':>45}{'[1] Choose the ID tournament to modify':<30s}"
              f"{' ':>35}|\n"
              f"|{' ':>45}{'[0] Return Tournament gestion':<30s}{' ':>43}|\n"
              f"|{'-' * 118}|"
              )
        on_top(*args, **kwargs)

    return before_modify_choice


def tournament_modify_sub_menu(on_top):
    """ print the modify menu on the console
    """

    def before_modify_choice(*args, **kwargs):
        print(f"|{'Modify Tournament':^118}|\n"
              f"|{'-' * 118}|\n|{'-' * 118}|\n"
              f"|{' ':>45}{'[1] Add players':<30s}{' ':>35}|\n"
              f"|{' ':>45}{'[2] Start tournament':<30s}{' ':>35}|\n"
              f"|{' ':>45}{'[3] Ending round and add resluts':<30s}"
              f"{' ':>35}|\n"
              f"|{' ':>45}{'[0] Return Tournament gestion':<30s}{' ':>43}|\n"
              f"|{'-' * 118}|"
              )
        on_top(*args, **kwargs)

    return before_modify_choice
