#! /usr/bin/env python3
# coding: utf-8
"""
checks, depending of the players' number in a tournament,
the maximum rounds' number without duplicate matches.

Functions
---------
max_rounds_without_duplicate(number_of_players)
    calculate the maximum rounds without duplicate matches possibilities
"""
from controllers.appairing_players import r_subset


def max_rounds_without_duplicate(number_of_players):
    """
    calculate the maximum rounds without duplicate matches possibilities

    Parameters
    __________
    number_of_players : int

    Returns
    -------
    max_rounds : int
    """
    list_of_players = []
    for i in range(1, number_of_players):
        list_of_players.append(i)
    pair = 2
    list_of_combinations = r_subset(list_of_players, pair)
    max_matches = len(list_of_combinations)

    # in one round, it will be number_of_players/2 matches :
    matches_by_round = number_of_players / 2
    max_rounds = max_matches // matches_by_round
    max_rounds = int(max_rounds)
    return max_rounds
