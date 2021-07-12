#! /usr/bin/env python3
# coding: utf-8
"""
Menus input fonctions for tournament gestion

Functions
---------
new_tournament()
    create a new tournament
add_players(list_ids, number_of_players)
    add user id in a tournament
modify_tournament_players(list_ids)
    modify list of players in a tournament
add_result_round(match_list, players_table)
    add result of a round in a tournament at the end of a round
add_result_tournoi(tournament, players_list)
    add the new ELO ranking after the end of tournament
"""

from controllers.for_tournament import (
    participants_tournament
)
from controllers.user_entry import (
    ControlEntryTournament as Cet,
    ControlGlobalEntry as Cge
)
from controllers.result_match import result_match


def new_tournament():
    """
    Function for input new tournament.
    Do not concerne the list of players or list of round,
    it's after for these entries.

    Returns
    -------
    tournament: list
        a list contains the informations for create a new tournament
        [name, place, date_tournament, control_time, description, number_of_round, number_of_players]
    """
    name = input("Name of tournament : ")
    while Cet(name).control_name_place_tournament() == 0:
        name = input("Name of tournament : ")

    place = input("Place :").upper()
    while Cet(place).control_name_place_tournament() == 0:
        place = input("Place :").upper()

    date_debut = input("Date de début : ")
    while Cge(date_debut).control_date() == 0:
        date_debut = input("Date de début : ")

    date_fin = input(f"Date de fin [{date_debut}]: ")
    if date_fin == '':
        date_fin = date_debut
    else:
        while Cge(date_fin).control_date() == 0:
            date_fin = input("Date de fin : ")

    control_time = input("[1] bullet, [2] blitz, [3]quick hit : ")
    while Cet(control_time).control_time_control() == 0:
        control_time = input("[1] bullet, [2] blitz, [3]quick hit : ")
    control_time = Cet(control_time).control_time_control()

    description = input("Description : ")

    number_of_players = input("Number_of_players [8] : ")
    if number_of_players == '':
        number_of_players = 8
    else:
        while Cet(number_of_players).control_number_of_players() == 0:
            number_of_players = input("Number_of_players : ")

    number_of_round = input("Number of round [4] : ")
    if number_of_round == '':
        number_of_round = 4
    else:
        while Cet(number_of_round).control_number_of_round(number_of_players) == 0:
            number_of_round = input("Number of round : ")

    date_tournament = [date_debut, date_fin]
    tournament = [name, place, date_tournament, control_time,
                  description, number_of_round, number_of_players]

    return tournament


def add_players(list_ids, number_of_players):
    """
    Add id players to a tournament

    Parameters
    ----------
    list_ids: list
        a list of ID
    number_of_players: int
        the number of players in the tournament

    Returns
    -------
    list_players: list
        a list contains the id players
    """
    list_players = []
    for i in range(1, number_of_players+1):

        player_id = input(f"ID player {i} : ")
        while Cge(player_id).control_id() == 0:
            player_id = input(f"ID player {i} : ")
        while Cge(player_id).control_id_reuse(list_players, list_ids) == 0:
            player_id = input(f"ID player {i} : ")

        list_players.append(int(player_id))

    list_players.sort()

    return list_players


def modify_tournament_players(list_ids, number_of_players):
    """
    Modify all players in a tournament. Can be used only if the tournament is not start yet

    Parameters
    ----------
    list_ids: list
        a list of id players
    number_of_players: int
        the number of players in the tournament

    Returns
    -------
    list_players: list
        the list of new id players for tournament in progress
    """
    choice = input("\033[33mWould you change players entries ? (yes/no) : \033[0m")
    if Cge(choice).control_choice() == 1:
        list_players = add_players(list_ids, number_of_players)
        return list_players


def add_result_round(match_list, players_table):
    """
    add result after a round

    Parameters
    ----------
    match_list: list
        a list of matches for the round
    players_table: tinydb.table.Table
        players table
    """
    for match in match_list:
        result_first_player = input(f" \033[33mPlayer ID {match[0][0]} :\033[0m ")
        while Cge(result_first_player).control_result_match() == 0:
            result_first_player = input(f" \033[33mPlayer ID {match[0][0]} :\033[0m ")
        result_match(match, result_first_player, players_table)


def add_result_tournoi(tournament, players_list):
    """
    Add result ranking ELO after the ending of tournament

    Parameters
    ----------
    tournament: Tournament
        an instance of tournament class
    players_list: list
        a list of players
    """
    applicants = participants_tournament(tournament, players_list)
    for player in applicants:
        ranking = input(f"ELO rank for {player[0]} {player[1]} {player[2]} "
                        f"global score : {player[3]} [{player[4]}]: "
                        )
        if ranking == '':
            ranking = player[4]
        while Cge(ranking).control_ranking() == 0:
            ranking = input(f"ELO rank for {player[0]} {player[1]} {player[2]} "
                            f"global score : {player[3]} [{player[4]}]: "
                            )
        player[4] = ranking

    return applicants
