#! /usr/bin/env python3
# coding: utf-8
"""
Control specific for new tournament creation
"""
import re
from controllers.maximum_round import max_rounds_without_duplicate
from controllers.backup_restore_round import deserialized_round


def control_name_place_tournament(name_place):
    name_place_valid = re.search(r"[A-Za-zéùàèêëï\- ]", name_place)
    if name_place_valid is None:
        print("\033[91mInvalid entry\033[0m\n")
        return 0
    else:
        return 1


def control_time_control(control_time):
    control_time_valid = re.search(r'^[123]$', control_time)
    choice_control = 0
    if control_time_valid is None:
        print("\033[91mYou must choose between the option 1, 2 or 3\033[0m\n")
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
        print(f"\033[33mMaximum rounds for {number_of_players} players is"
              f" \033[91m{max_rounds} \033[0m")
        return 0
    else:
        return 1


def control_number_of_players(number_of_players):
    number_valid = re.search(r'^[\d]{1,3}$', number_of_players)
    if number_valid is None:
        return 0
    elif int(number_of_players) % 2 != 0:  # Must be a multiple of 2 for making matches
        print("\033[91mThe number of players must be even to play the matches\033[0m\n")
        return 0
    else:
        return 1


def tournament_in_progress(tournament_table, id_tournament):
    for tournament in tournament_table:
        if tournament.id_tournament == int(id_tournament):
            return tournament
    print("\033[91mProblem with tournament ID\33[0m\n")
    return False


def participants_tournament(tournament, list_of_players, sort_by='score'):
    applicants = []
    list_round = deserialized_round(tournament.list_of_round)

    for a_round in list_round:
        number_matches = len(a_round.match_list)
        for i in range(0, number_matches):
            id_player_one = int(a_round.match_list[i][0][0])
            id_player_two = int(a_round.match_list[i][1][0])
            for player in list_of_players:
                if id_player_one == int(player.id_player):
                    player.score += float(a_round.match_list[i][0][1])
                elif id_player_two == int(player.id_player):
                    player.score += float(a_round.match_list[i][1][1])

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
    if sort_by == 'score':
        applicants = sorted(applicants, key=lambda x: x[3], reverse=True)
    elif sort_by == 'name':
        applicants = sorted(applicants, key=lambda x: x[2])

    return applicants
