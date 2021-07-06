#! /usr/bin/env python3
# coding: utf-8
"""
Control specific for new tournament creation
"""
import re
from controllers.maximum_round import max_rounds_without_duplicate


def control_name_place_tournament(name_place):
    name_place_valid = re.search(r"[A-Za-zéùàèêëï\- ]", name_place)
    if name_place_valid is None:
        print("the entry is not valid.")
        return 0
    else:
        return 1


def control_time_control(control_time):
    control_time_valid = re.search(r'^[123]$', control_time)
    choice_control = 0
    if control_time_valid is None:
        print("You must choose between the option 1, 2 or 3")
    else:
        if control_time == '1':
            choice_control = 'bullet'
        elif control_time == '2':
            choice_control = 'blitz'
        elif control_time == '3':
            choice_control = 'quick hit'
    return choice_control


def control_number_of_round(number_of_round, number_of_players):
    number_valid = re.search(r'^[\d]{1,3}$', number_of_round)

    if number_valid is None:
        return 0
    max_rounds = max_rounds_without_duplicate(int(number_of_players))
    if max_rounds < int(number_of_round):
        print(f"Maximum rounds for {number_of_players} players is"
              f" {max_rounds} ")
        return 0
    else:
        return 1


def control_number_of_players(number_of_players):
    number_valid = re.search(r'^[\d]{1,3}$', number_of_players)
    if number_valid is None:
        return 0
    elif int(number_of_players) % 2 != 0:  # Must be a multiple of 2 for making matches
        print("The number of players must be even to play the matches")
        return 0
    else:
        return 1


def tournament_in_progress(tournament_table, id_tournament):
    for tournament in tournament_table:
        if tournament.id_tournament == int(id_tournament):
            return tournament
    print("Problem with tournament ID")
    return False


def participants_tournament(tournament, list_of_players):
    applicants = []
    for player in list_of_players:
        if player.id_player in tournament.list_of_players:
            applicants.append(
                [
                    player.id_player,
                    player.name,
                    player.surname,
                    player.score,
                    player.ranking
                ]
            )

    applicants = sorted(applicants, key=lambda x: x[3], reverse=True)

    return applicants
