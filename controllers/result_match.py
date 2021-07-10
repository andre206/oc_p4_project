#! /usr/bin/env python3
# coding: utf-8
""" Menus input fonctions and methode for tournament gestion"""

from controllers.backup_restore_players import (
    serialized_players,
    deserialized_players
)


def result_match(
        match,
        result_first_player,
        players_table
):
    list_of_player = deserialized_players(players_table)

    if result_first_player == '1':
        match[0][1] = 1
        match[1][1] = 0
    elif result_first_player == '0.5':
        match[0][1] = 0.5
        match[1][1] = 0.5
    elif result_first_player == '0':
        match[0][1] = 0
        match[1][1] = 1
    for player in list_of_player:
        if match[0][0] == player.id_player:
            player.score += match[0][1]
            print(f"\n {player.id_player} _ {player.name} \033[33m-->\033[91m {player.score}\033[0m")
        if match[1][0] == player.id_player:
            player.score += match[1][1]
            print(f" {player.id_player} _ {player.name} \033[33m-->\033[91m {player.score}\033[0m\n")
    serialized_players(list_of_player)
