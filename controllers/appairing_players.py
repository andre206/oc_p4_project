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


def sorted_players_id(list_players):
    sorted(list_players, key='ranking')
    print(list_players)


class Round_generated:

    def init(self, list_of_players_id, list_of_combinations=None, r=2):
        self.list_of_players = list_of_players_id
        self.list_of_combination = list_of_combinations
        self.r = r

    def apparing_first_round(self):
        pass


if __name__ == '__main__':
    list_of_players_id = [1, 2, 3, 4, 5, 6, 7, 8]
    list_of_players = []
    i = 2
    list_of_match_possibilities = r_subset(list_of_players_id, i)
    print(list_of_match_possibilities)
    round_1 = [(1, 5), (2, 6), (3, 7), (4, 8)]

    for element in list_of_match_possibilities:
        for elt in round_1:
            if element == elt:
                print(elt)
                list_of_match_possibilities.remove(elt)
    print(list_of_match_possibilities)
    player_name = 'player_'
    for i in range(1, 9):
        player = Player(name=f'player_{i}',
                        surname=f'surname_{i}',
                        date_of_birth=f'0{i}/01/1980',
                        sex='F',
                        id_player=i,
                        ranking=1000 - i)
        list_of_players.append(player)
    tri_par_rang = []
    for player in list_of_players:
        tri_par_rang.append((player.id_player, player.ranking))
    tri_par_rang = sorted(tri_par_rang, key=lambda x: x[1], reverse=True)
    print(tri_par_rang)

    first_list = tri_par_rang[0:4]
    id_player_first = []
    for player in first_list:
        id_player_first.append(player[0])
    second_list = tri_par_rang[4:8]
    id_player_second = []
    for player in second_list:
        id_player_second.append(player[0])
    print(id_player_first, id_player_second)

    round_1 = itertools.zip_longest(id_player_first, id_player_second)
    i = 1
    list_of_match = []
    for id_1, id_2 in round_1:
        if id_1 < id_2 :
            match = (id_1, id_2)
            list_of_match.append(match)
        else:
            match = (id_2, id_1)
            list_of_match.append(match)
    print(list_of_match)
