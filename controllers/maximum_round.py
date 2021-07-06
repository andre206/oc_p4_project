#! /usr/bin/env python3
# coding: utf-8
"""
checks, depending of the players' number in a tournament,
the maximum rounds' number without duplicate matches.
"""

from itertools import combinations


def r_subset(arr, r):
    """
    return list of all subsets of length r to deal
    with duplicate subsets use set(list(combinations(arr, r)))
    """
    return list(combinations(arr, r))


def max_rounds_without_duplicate(number_of_players):
    list_of_players = []
    for i in range(1, number_of_players):
        list_of_players.append(i)
    pair = 2
    list_of_combinations = r_subset(list_of_players, pair)
    max_matches = len(list_of_combinations)
    # in one round, it will be number_of_players/2 matches :
    matches_by_round = number_of_players / 2
    max_rounds = max_matches // matches_by_round
    return int(max_rounds)

