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


def remove_playing_matches(
        list_of_possibilities,
        list_of_rounds,
):
    list_matches_played = []
    for match in list_of_possibilities:
        for rounds in list_of_rounds:
            for played_match in rounds:
                if match == played_match:
                    list_of_possibilities.remove(match)
                    list_matches_played.append(match)
    return list_of_possibilities, list_matches_played


class RoundGenerated:

    def __init__(self, list_of_players):
        self.list_of_players = list_of_players

    def list_of_possibilities(self):
        list_of_players_id = []
        for player in self.list_of_players:
            list_of_players_id.append((player.id_player, player.score))
        i = 2
        list_of_combinations = r_subset(list_of_players_id, i)
        return list_of_combinations

    def sorted_players_rank(self):
        sort_by_rank = []
        for player in self.list_of_players:
            sort_by_rank.append(
                (player.id_player,
                 player.name,
                 player.surname,
                 int(player.ranking),
                 float(player.score)),
            )

        sort_by_rank = sorted(sort_by_rank, key=lambda x: x[3], reverse=True)
        return sort_by_rank

    def sorted_players_scores(self):
        sort_by_scores = []
        for player in self.list_of_players:
            sort_by_scores.append(
                (player.id_player,
                 player.name,
                 player.surname,
                 int(player.ranking),
                 float(player.score)),
            )

        sort_by_scores = sorted(sort_by_scores, key=lambda x: x[4], reverse=True)
        return sort_by_scores

    def first_round(self, sort_by_rank):
        """
        for the fist round
        return a list of match for the first round
        """

        first_list = sort_by_rank[0:4]
        player_first = []
        for player in first_list:
            player_first.append((player[0], player[4]))
        second_list = sort_by_rank[4:8]
        player_second = []
        for player in second_list:
            player_second.append((player[0], player[4]))
        a_round = itertools.zip_longest(player_first, player_second)
        round_one = []
        for id_1, id_2 in a_round:
            if id_1 < id_2:
                match = (id_1, id_2)
                round_one.append(match)
            else:
                match = (id_2, id_1)
                round_one.append(match)

        return round_one

    def other_round(self, list_played_matches, sort_by_scores):
        """
        For generate another round (not the first round.
        Based on players sorted by scores.
        If a match was played yet, generate another match
        return a list of match for the round
        """
        list_matches_round = []
        list_of_players = []

        players_number = int(len(sort_by_scores))
        for player in sort_by_scores:
            list_of_players.append((player[0], player[4]))

        numbers_matches = int(players_number/2)

        for number in range(1, numbers_matches+1):
            player_one = list_of_players[0]
            player_two = list_of_players[1]
            match = (player_one, player_two)

            for i in range(2, players_number+1):
                if match in list_played_matches:
                    player_two = list_of_players[players_number - (players_number-i)]
                    match = (player_one, player_two)

            list_matches_round.append(match)
            if player_one in list_of_players:
                list_of_players.remove(player_one)
            if player_two in list_of_players:
                list_of_players.remove(player_two)

        return list_matches_round


if __name__ == '__main__':
    from backup_restore_players import (
        deserialized_players,
    )
    from tinydb import TinyDB

    db = TinyDB('C:\Git\oc_p4_project\db.json')
    players_table = db.table('players')
    tournaments_table = db.table('tournaments')
    list_of_players = deserialized_players((players_table))

    tri_rank = RoundGenerated(list_of_players).sorted_players_rank()

    print(tri_rank)

    tri_scores = RoundGenerated(list_of_players).sorted_players_scores()

    print(tri_scores)

    list_of_possible_match = RoundGenerated(
        list_of_players
    ).list_of_possibilities()

    print(list_of_possible_match)

    round_1 = RoundGenerated(
        list_of_players,
    ).first_round(sort_by_rank=tri_rank)

    print(round_1)

    list_of_rounds = []

    list_of_rounds.append(round_1)

    list_of_possible_match, list_matches_played = remove_playing_matches(
        list_of_possible_match,
        list_of_rounds
    )
    print(list_of_possible_match, list_matches_played)

    other_round = RoundGenerated(list_of_players).other_round(
        list_matches_played,
        tri_scores
    )

    print(other_round)