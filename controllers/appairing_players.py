#! /usr/bin/env python3
# coding: utf-8
""" gestion of the appairing matches and rounds"""
import itertools
from itertools import combinations
from models.player import Player


def r_subset(arr, r):
    """
    return list of all subsets of length r to deal
    with duplicate subsets use set(list(combinations(arr, r)))
    """
    return list(combinations(arr, r))


def remove_playing_matches(list_of_possibilities, round):
    for element in list_of_possibilities:
        for elt in round:
            if element == elt:
                list_of_possibilities.remove(elt)
    return list_of_possibilities


def first_round(tri_par_rang):
    first_list = tri_par_rang[0:4]
    id_player_first = []
    for player in first_list:
        id_player_first.append(player[0])
    second_list = tri_par_rang[4:8]
    id_player_second = []
    for player in second_list:
        id_player_second.append(player[0])
    round = itertools.zip_longest(id_player_first, id_player_second)
    round_1 = []
    for id_1, id_2 in round:
        if id_1 < id_2:
            match = (id_1, id_2)
            round_1.append(match)
        else:
            match = (id_2, id_1)
            round_1.append(match)

    return round_1


class RoundGenerated:

    def __init__(self, list_of_players):
        self.list_of_players = list_of_players

    def list_of_possibilities(self):
        list_of_players_id = []
        for player in self.list_of_players:
            list_of_players_id.append(player.id_player)
        i = 2
        list_of_combinations = r_subset(list_of_players_id, i)
        return list_of_combinations

    def sorted_players_rank(self):
        tri_par_rang = []
        for player in self.list_of_players:
            tri_par_rang.append((player.id_player, player.name, player.surname, player.ranking))

        tri_par_rang = sorted(tri_par_rang, key=lambda x: x[3], reverse=True)
        return tri_par_rang


if __name__ == '__main__':
    list_of_players = []
    player_name = 'player_'
    for i in range(1, 9):
        player = Player(name=f'player_{i}',
                        surname=f'surname_{i}',
                        date_of_birth=f'0{i}/01/1980',
                        sex='F',
                        id_player=i,
                        ranking=1000 - i)
        list_of_players.append(player)

    tri_rank = RoundGenerated(list_of_players).sorted_players_rank()

    print(tri_rank)

    list_of_possible_match = RoundGenerated(list_of_players).list_of_possibilities()

    print(list_of_possible_match)

    round_1 = first_round(tri_rank)

    print(round_1)

    list_of_possible_match = remove_playing_matches(list_of_possible_match, round_1)
    print(list_of_possible_match)
