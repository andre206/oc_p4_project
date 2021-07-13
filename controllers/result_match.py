#! /usr/bin/env python3
# coding: utf-8
"""
Menus input for control the result of matches

Functions
---------
result_match(match, result_first_player, players_table)
    Calculate and return results for matches
"""

from controllers.backup_restore_players import (
    serialized_players,
    deserialized_players
)


def result_match(match, result_first_player, players_table):
    """
    Calculate and return results for matches

    Parameters
    ----------
    match : list
        a list of couple [[id_player,scores][id_player,scores]]
    result_first_player : str
        input by user. Must be 1, 0.5 or 0.
    players_table : tinydb.table.Table
        table of players
    """
    list_of_player = deserialized_players(players_table)

    if float(result_first_player) == 1.0:
        match[0][1] = 1
        match[1][1] = 0
    elif float(result_first_player) == 0.5:
        match[0][1] = 0.5
        match[1][1] = 0.5
    elif float(result_first_player) == 0.0:
        match[0][1] = 0
        match[1][1] = 1
    print('\n')
    for player in list_of_player:
        if match[0][0] == player.id_player:
            player.score += match[0][1]
            print(f" {player.id_player} - {player.name} \033[33m-->\033[91m {player.score}\033[0m")
        if match[1][0] == player.id_player:
            player.score += match[1][1]
            print(f" {player.id_player} - {player.name} \033[33m-->\033[91m {player.score}\033[0m")
    print('\n')
    serialized_players(list_of_player)
