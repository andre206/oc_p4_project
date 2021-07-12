#! /usr/bin/env python3
# coding: utf-8
"""
Control specific for tournament participants/applicants

Functions
---------
participants_tournament(tournament, list_of_players, sort_by='score')
    calculate the current score of the participants of a tournament
    and to return the list of participants with the updated scores.
"""
from controllers.backup_restore_round import deserialized_round


def participants_tournament(tournament, list_of_players, sort_by='score'):
    """
    calculate the current score of the participants of a tournament
    and to return the list of participants with the updated scores.

    Parameters
    ----------
    tournament : Tournament
        an instance of tournament class
    list_of_players : list
        a list of players
    sort_by : str
        for select the method to sort players. By score by default. Possibly by name.

    Returns
    -------
    applicants : list
        a list of participants tournament, sorted, with update scores.
    """
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
