#! /usr/bin/env python3
# coding: utf-8
"""
check the data entered by the user

Functions
---------
control_name_surname_player(name_surname)
    control the entry name_surname, if it's matches the pattern
control_date(date_to_control)
    control that the entry is a date in format dd/mm/yyyy
control_sex(sex)
    control that entry is F or M
control_ranking(ranking)
    control that the entry is an integer, minimum 1000
control_id(a_id)
    control  the the entry is an integer
control_id_reuse(a_id, list_id, list_ids)
    control that the id is used just one time by the user, for exemple to add
    player in a tournament, you can't add twice the same person
control_choice(choice)
    for control an user choice, like change users in tournament before starting it
control_result_match(result)
    control that the entry is 1 or 0.5 or 1.
"""
from datetime import datetime
import re


def control_name_surname_player(name_surname):
    """
    control the entry name_surname, if it's matches the pattern

    Parameters
    ----------
    name_surname : str
        the entry by user

    Returns
    -------
    0 : int
        if the name or surname doesn't match pattern
    1 : int
        if the name or surname matches pattern
    """
    name_surname_valid = re.search(r"[A-Za-zéùàèêëï\-]", name_surname)
    if name_surname_valid is None:
        print("the entry is not valid.")
        return 0
    else:
        return 1


def control_date(date_to_control):
    """
    control that the entry is a date in format dd/mm/yyyy

    Parameters
    ----------
    date_to_control : int
        the date enter by user

    Raises
    ------
    ValueError : datetime
        the date is not a datetime

    Returns
    -------
    0 : int
        if the entry is not valid
    1 : int
        if the entry is valid
    """
    try:
        datetime.strptime(date_to_control, "%d/%m/%Y")
        return 1

    except ValueError:
        print("Please, take a date with format 'dd/mm/yyyy'")
        return 0


def control_sex(sex):
    """
    control that entry is F or M

    Parameters
    ----------
    sex = int
        The sex of the player enter by user
        must be F or M - don't take care the case

    Returns
    -------
    0 : int
        if the sex doesn't match pattern
    1 : int
        if the sex matches pattern

    """
    sex_valid = re.search(r"^[MF]$", sex.upper())
    if sex_valid is None:
        print("Please, type 'M' or 'F'")
        return 0
    else:
        return 1


def control_ranking(ranking):
    """
    control that the entry is an integer, minimum 1000

    Parameters
    ----------
    ranking: str
        the ranking enter by the user

    Raises
    ------
    ValueError : int
        the ranking must changed in an integer.

    Returns
    -------
    0: int
        if the ranking is not valid
    1: int
        if the ranking is not valid
    """
    if ranking == '':
        ranking = 0

    try:
        int(ranking)
        if int(ranking) < 1000 and int(ranking) != 0:
            print('Minimum rank is 1000')
            return 0
        return 1
    except ValueError:
        return 0


def control_id(a_id):
    """
    control  the the entry is an integer

    Parameters
    ----------
    a_id: str
        input id by user

    Raises
    ------
    ValueError: int
        the a_id must be changed in an integer

    Returns
    -------
    0: int
        if the a_id is not valid
    1: 1
        if the a_id is valid
    """
    try:
        int(a_id)
        return 1
    except ValueError:
        print("Please, take a number ID")
        return 0


def control_id_reuse(a_id, list_id, list_ids):
    """
    control that the id is used just one time by the user, for exemple to add
    player in a tournament, you can't add twice the same person

    Parameters
    ----------
    a_id: str
        input by user
    list_id: list
        a list of used id
    list_ids: list
        a list of existing id

    Returns
    -------
    0: int
        if the id is already used
    1: int
        if the id is not used yet
    """
    for ids in list_id:
        if int(a_id) == ids:
            print("This ID already used. Please select another one.")
            return 0
    for ids in list_ids:
        if int(a_id) == ids:
            return 1
    print("Non-existent ID, please select an existent ID")
    return 0


def control_choice(choice):
    """
    for control an user choice, like change users in tournament before starting it

    Parameters
    ----------
    choice: str
        input by user

    Returns
    -------
    0: int
        if choice is not yes
    1: int
        if choice is yes
    """
    if choice.upper() == 'YES':
        return 1
    else:
        return 0


def control_result_match(result):
    """
    control that the entry is 1 or 0.5 or 1.

    Parameters
    ----------
    result: str
        input by the user

    Raises
    ------
    ValueError: str
        the result must be a number

    Returns
    -------
    0: int
        if invalid result
    1: int
        if valid result
    """
    try:
        if float(result) == 1 or float(result) == 0 or float(result) == 0.5:
            return 1
        else:
            print("[0] : lost --- [0.5] : equal --- [1] : win")
            return 0
    except ValueError:
        print("[0] : lost --- [0.5] : equal --- [1] : win")
        return 0
