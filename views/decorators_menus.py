#! /usr/bin/env python3
# coding: utf-8
"""
Module for views on the top of the console
decorators functions only

Functions
---------
clean()
    to clean the console
pre_menu(under)
    for the title of the appliance
main_menu(under)
    print the main menu
players_menu(under)
    print the player menu on the console
players_modify_menu(under)
    print the modify menu on the console
tournament_menu(under
    print the tournament menu on the console
tournament_modify_menu(under)
    print the modify tournament menu on the console
def tournament_modify_sub_menu(under)
    print the modify tournament sub menu on the console
reports_menu(under)
    Print the selection choices of reports
tournament_view_menu(under)
    print the choice for tournament view menu on the console
reports_tournament(under)
    Print the selection choices of reports
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


def pre_menu(under):
    """ for the title of the appliance"""

    def before_menu(*args, **kwargs):
        """
        Do this before an other function
        """
        clean()
        pre_menu_text = (f"\033[33m|{'-' * 118}|\n"
                         f"| \033[91m@ @@ @\033[33m {' ' * 102} "
                         f"\033[91m@ @@ @\033[33m |\n"
                         f"| \033[91m@@@@@@\033[33m {' ' * 102} "
                         f"\033[91m@@@@@@\033[33m |\n"
                         f"|   \033[91m@@\033[33m   {' ' * 39} {'#' * 22} "
                         f"{' ' * 39}   \033[91m@@\033[33m   |\n"
                         f"|  \033[91m@@@@\033[33m  {' ' * 39} ## Chess Tournament ## {' ' * 39}"
                         f"  \033[91m@@@@\033[33m  |\n"
                         f"| \033[91m@@@@@@\033[33m {' ' * 39} {'#' * 22}"
                         f" {' ' * 39} \033[91m@@@@@@\033[33m |\n"
                         f"|\033[91m@@@@@@@@\033[33m{' ' * 102}"
                         f"\033[91m@@@@@@@@\033[33m|\n"
                         f"|{'-' * 118}|\033[0m")
        print(pre_menu_text)
        under(*args, **kwargs)

    return before_menu


def main_menu(under):
    """
    print the main menu
    """

    def before_main_choice(*args, **kwargs):
        """
        Do this before an other function
        """
        main_menu_text = (f"\033[33m|{'Main Menu':^118}|\n"
                          f"|{'-' * 118}|\n|{'-' * 118}|\n"
                          f"|{' ':>45}\033[91m[1]\033[33m{' Tournaments management':<30s}"
                          f"{' ':>40}|\n"
                          f"|{' ':>45}\033[91m[2]\033[33m{' Players management':<30s}"
                          f"{' ':>40}|\n"
                          f"|{' ':>45}\033[91m[3]\033[33m{' Reports':<30s}"
                          f"{' ':>40}|\n"
                          f"|{' ':>45}\033[91m[0]\033[33m{' Exit Chess Tournament':<30s}"
                          f"{' ':>40}|\n"
                          f"|{'-' * 118}|\033[0m\n"
                          )
        print(main_menu_text)
        under(*args, **kwargs)

    return before_main_choice


def players_menu(under):
    """
    print the player menu on the console
    """

    def before_players_choice(*args, **kwargs):
        """
        Do this before an other function
        """
        players_menu_text = (f"\033[33m|{'Players management':^118}|\n"
                             f"|{'-' * 118}|\n|{'-' * 118}|\n"
                             f"|{' ':>45}\033[91m[1]\033[33m{' Add new player':<30s}"
                             f"{' ':>40}|\n"
                             f"|{' ':>45}\033[91m[2]\033[33m{' View all players':<30s}"
                             f"{' ':>40}|\n"
                             f"|{' ':>45}\033[91m[3]\033[33m{' Modify one player':<30s}"
                             f"{' ':>40}|\n"
                             f"|{' ':>45}\033[91m[0]\033[33m{' Return main menu':<30s}"
                             f"{' ':>40}|\n"
                             f"|{'-' * 118}|\033[0m\n"
                             )
        print(players_menu_text)
        under(*args, **kwargs)

    return before_players_choice


def players_modify_menu(under):
    """
    print the modify menu on the console
    """

    def before_modify_choice(*args, **kwargs):
        """
        Do this before an other function
        """
        players_modify_text = (f"\033[33m|{'Modify player':^118}|\n"
                               f"|{'-' * 118}|\n|{'-' * 118}|\n"
                               f"|{' ':>45}\033[91m[1]\033[33m"
                               f"{' Choose the ID player to modify':<30s}"
                               f"{' ':>39}|\n"
                               f"|{' ':>45}\033[91m[0]\033[33m{' Return Players management':<30s}"
                               f"{' ':>40}|\n"
                               f"|{'-' * 118}|\033[0m\n"
                               )
        print(players_modify_text)
        under(*args, **kwargs)

    return before_modify_choice


def tournament_menu(under):
    """
    print the tournament menu on the console
    """
    def before_tournament_choice(*args, **kwargs):
        """
        Do this before an other function
        """
        tournament_menu_text = (f"\033[33m|{'Tournaments management':^118}|\n"
                                f"|{'-' * 118}|\n|{'-' * 118}|\n"
                                f"|{' ':>45}\033[91m[1]\033[33m{' Add new tournament':<30s}"
                                f"{' ':>40}|\n"
                                f"|{' ':>45}\033[91m[2]\033[33m{' View all tournament':<30s}"
                                f"{' ':>40}|\n"
                                f"|{' ':>45}\033[91m[3]\033[33m{' Modify one tournament':<30s}"
                                f"{' ':>40}|\n"
                                f"|{' ':>45}\033[91m[0]\033[33m{' Return main menu':<30s}"
                                f"{' ':>40}|\n"
                                f"|{'-' * 118}|\033[0m\n"
                                )
        print(tournament_menu_text)
        under(*args, **kwargs)

    return before_tournament_choice


def tournament_modify_menu(under):
    """
    print the modify tournament menu on the console
    """

    def before_modify_choice(*args, **kwargs):
        """
        Do this before an other function
        """
        tournament_modify_text = (f"\033[33m|{'Modify Tournament':^118}|\n"
                                  f"|{'-' * 118}|\n|{'-' * 118}|\n"
                                  f"|{' ':>45}\033[91m[1]\033[33m"
                                  f"{' Choose the ID tournament to modify':<30s}"
                                  f"{' ':>35}|\n"
                                  f"|{' ':>45}\033[91m[0]\033[33m"
                                  f"{' Return Tournaments management':<30s}"
                                  f"{' ':>40}|\n"
                                  f"|{'-' * 118}|\033[0m\n"
                                  )
        print(tournament_modify_text)
        under(*args, **kwargs)

    return before_modify_choice


def tournament_modify_sub_menu(under):
    """
    print the modify tournament sub menu on the console
    """
    def before_modify_choice(*args, **kwargs):
        """
        Do this before an other function
        """
        tournament_sub_text = (f"\033[33m|{'Modify Tournament':^118}|\n"
                               f"|{'-' * 118}|\n|{'-' * 118}|\n"
                               f"|{' ':>45}\033[91m[1]\033[33m{' Add players':<30s}"
                               f"{' ':>40}|\n"
                               f"|{' ':>45}\033[91m[2]\033[33m{' Starting Round':<30s}"
                               f"{' ':>40}|\n"
                               f"|{' ':>45}\033[91m[3]\033[33m"
                               f"{' Ending Round and add results':<38s}"
                               f"{' ':>32}|\n"
                               f"|{' ':>45}\033[91m[4]\033[33m"
                               f"{' View results of tournament':<38s}"
                               f"{' ':>32}|\n"
                               f"|{' ':>45}\033[91m[0]\033[33m"
                               f"{' Return Tournament management':<30s}{' ':>40}|\n"
                               f"|{'-' * 118}|\033[0m\n"
                               )
        print(tournament_sub_text)
        under(*args, **kwargs)

    return before_modify_choice


def reports_menu(under):
    """
    Print the selection choices of reports
    """
    def before_select_report(*args, **kwargs):
        """
        Do this before an other function
        """
        reports_text = (f"\033[33m|{'Reports':^118}|\n"
                        f"|{'-' * 118}|\n|{'-' * 118}|\n"
                        f"|{' ':>45}\033[91m[1]\033[33m{' View All Players - by rank':<30s}"
                        f"{' ':>40}|\n"
                        f"|{' ':>45}\033[91m[2]\033[33m{' View All Players - by name':<30s}"
                        f"{' ':>40}|\n"
                        f"|{' ':>45}\033[91m[3]\033[33m"
                        f"{' View List of all Tournaments':<38s}"
                        f"{' ':>32}|\n"
                        f"|{' ':>45}\033[91m[4]\033[33m"
                        f"{' View informations of one specific tournament':<30s}"
                        f"{' ':>25}|\n"
                        f"|{' ':>45}\033[91m[0]\033[33m"
                        f"{' Return main menu':<30s}{' ':>40}|\n"
                        f"|{'-' * 118}|\033[0m\n"
                        )
        print(reports_text)
        under(*args, **kwargs)

    return before_select_report


def tournament_view_menu(under):
    """
    print the choice for tournament view menu on the console
    """
    def before_view_choice(*args, **kwargs):
        """
        Do this before an other function
        """
        tournament_view_text = (f"\033[33m|{'Modify Tournament':^118}|\n"
                                f"|{'-' * 118}|\n|{'-' * 118}|\n"
                                f"|{' ':>45}\033[91m[1]\033[33m"
                                f"{' Choose the ID tournament to view':<30s}"
                                f"{' ':>35}|\n"
                                f"|{' ':>45}\033[91m[0]\033[33m"
                                f"{' Return reports menu':<30s}"
                                f"{' ':>40}|\n"
                                f"|{'-' * 118}|\033[0m\n"
                                )
        print(tournament_view_text)
        under(*args, **kwargs)

    return before_view_choice


def reports_tournament(under):
    """
    Print the selection choices of reports
    """
    def before_select_report(*args, **kwargs):
        """
        Do this before an other function
        """
        reports_tournament_text = (f"\033[33m|{'Reports':^118}|\n"
                                   f"|{'-' * 118}|\n|{'-' * 118}|\n"
                                   f"|{' ':>45}\033[91m[1]\033[33m{' View Players - by score':<30s}"
                                   f"{' ':>40}|\n"
                                   f"|{' ':>45}\033[91m[2]\033[33m{' View Players - by name':<30s}"
                                   f"{' ':>40}|\n"
                                   f"|{' ':>45}\033[91m[3]\033[33m"
                                   f"{' View List of rounds and matches':<38s}"
                                   f"{' ':>32}|\n"
                                   f"|{' ':>45}\033[91m[4]\033[33m"
                                   f"{' View all other informations':<38s}"
                                   f"{' ':>32}|\n"
                                   f"|{' ':>45}\033[91m[0]\033[33m"
                                   f"{' Return reports menu':<30s}{' ':>40}|\n"
                                   f"|{'-' * 118}|\033[0m\n"
                                   )
        print(reports_tournament_text)
        under(*args, **kwargs)

    return before_select_report
