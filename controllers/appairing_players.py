#! /usr/bin/env python3
# coding: utf-8
"""
gestion of the appairing players in  matches and rounds

This module contains fonctions and class to help for generate rounds in a
tournament.

Classes
-------
RoundGenerated
    This class is made for generate rounds.
Functions
---------
r_subset(arr, r)
    list of all subsets of length r to deal
    with duplicate subsets use set(list(combinations(arr, r)))
remove_playing_matches
    This fonction permit to add played matches in a list,
    and remove from the possible matches the
    played matches.
"""
import itertools
from itertools import combinations

import controllers.for_tournament
import models.backup_restore_players


def r_subset(arr, r):
    """
    Returns
    -------
    list : list of all subsets of length r to deal
    with duplicate subsets use set(list(combinations(arr, r)))
    """
    return list(combinations(arr, r))


def remove_playing_matches(list_of_possibilities, list_of_matches_rounds):
    """
    This fonction permit to add played matches in a list,
    and remove from the possible matches the
    played matches.

    Parameters
    ----------
    list_of_possibilities : list
        list of all matches possibilities
    list_of_matches_rounds : list
        a list of matches played yet

    Returns:
    --------
    list_of_possibilities : list
        list of possible matches
    list_matches_played : list
        list of matches played yet
    """
    list_matches_played = []
    for match in list_of_matches_rounds:
        if match in list_of_possibilities:
            list_of_possibilities.remove(match)
            list_matches_played.append(match)
    return list_of_possibilities, list_matches_played


class RoundGenerated:
    """
    This class is made for generate rounds.

    Attributes
    ----------
    list_of_players : list
        a list of players

    Methods
    -------
    list of possibilities(self)
        calculate the number of different matches could be play in the tournament
    sorted_players_rank(self)
        sort the list of players by rank
    sorted_players_scores(self)
        sort the list of players by score
    first_round(self, sort_by_rank)
        for the fist round
    other_round(self, list_played_matches, sort_by_scores)
        for generate another round (not the first round.
    """

    def __init__(self, list_of_players):
        """
        Parameters
        ----------
        list_of_players : list
            a list of Players
        """
        self.list_of_players = list_of_players

    def list_of_possibilities(self):
        """
        based on the number of players, this fonction calculate
        the number of different matches could be play in the
        tournament, at first.

        Returns
        -------
        list_of_combinations : list
            a list of all possibilities matches
        """
        list_of_players_id = []
        for player in self.list_of_players:
            list_of_players_id.append(player.id_player)
        list_of_players_id = sorted(list_of_players_id)
        i = 2
        list_of_combinations = r_subset(list_of_players_id, i)
        return list_of_combinations

    def sorted_players_rank(self):
        """
        sort the list of players by rank

        Returns
        -------
        sort_by_rank : list
            a list of players
        """
        sort_by_rank = []
        for player in self.list_of_players:
            sort_by_rank.append(
                (player.id_player,
                 player.name,
                 player.first_name,
                 int(player.ranking),
                 float(player.score)),
            )

        sort_by_rank = sorted(sort_by_rank, key=lambda x: x[3], reverse=True)
        return sort_by_rank

    def sorted_players_scores(self):
        """
        sort the list of players by score

        Returns
        -------
        sort_by_scores : list
            a list of players
        """
        sort_by_scores = []
        for player in self.list_of_players:
            sort_by_scores.append(
                (player.id_player,
                 player.name,
                 player.first_name,
                 int(player.ranking),
                 float(player.score)),
            )

        sort_by_scores = sorted(sort_by_scores, key=lambda x: x[4], reverse=True)
        return sort_by_scores

    @staticmethod
    def first_round(sort_by_rank):
        """
        for the fist round

        Parameters
        ----------
        sort_by_rank : list
            a list of Players, sorted by rank

        Returns
        -------
        round_one : list
            a list of match for the first round
        """
        half_players = int(len(sort_by_rank) / 2)
        all_players = int(len(sort_by_rank))
        first_list = sort_by_rank[0:half_players]
        player_first = []
        for player in first_list:
            player_first.append((player[0], player[4]))
        second_list = sort_by_rank[half_players:all_players]
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

    @staticmethod
    def other_round(list_played_matches, sort_by_scores):
        """
        For generate another round (not the first round.
        Based on players sorted by scores.
        If a match was played yet, generate another match

        Parameters
        ----------
        list_played_matches : list
            a list of played matches
        sort_by_scores : list
            a list of players sorted by scores

        Returns
        -------
        list_matches_round : list
            a list of match for the round
        """

        try:
            list_matches_round = []
            list_of_players = []
            list_of_id_players = []

            players_number = int(len(sort_by_scores))

            for player in sort_by_scores:
                list_of_players.append((player[0], player[4]))
                list_of_id_players.append(player[0])

            numbers_matches = int(players_number / 2)

            for number in range(1, numbers_matches + 1):
                id_player_one = int(list_of_id_players[0])
                id_player_two = int(list_of_id_players[1])
                pair_player = [id_player_one, id_player_two]
                pair_player_two = [id_player_two, id_player_one]
                player_one = player_two = None

                i = number + 1
                if i >= numbers_matches:
                    i = 1
                while pair_player in list_played_matches or pair_player_two in list_played_matches:
                    id_player_two = list_of_id_players[i]
                    pair_player = [id_player_one, id_player_two]
                    pair_player_two = [id_player_two, id_player_one]
                    i += 1

                for player in list_of_players:
                    if player[0] == id_player_one:
                        player_one = player
                        list_of_id_players.remove(id_player_one)
                    if player[0] == id_player_two:
                        player_two = player
                        list_of_id_players.remove(id_player_two)
                list_matches_round.append((player_one, player_two))

                if player_one in list_of_players:
                    list_of_players.remove(player_one)
                if player_two in list_of_players:
                    list_of_players.remove(player_two)
            return list_matches_round
        except IndexError:
            print('Shuffle...')

        try:
            list_matches_round = []
            list_of_players = []
            list_of_id_players = []

            players_number = int(len(sort_by_scores))
            for player in sort_by_scores:
                list_of_players.append((player[0], player[4]))
                list_of_id_players.append(player[0])

            numbers_matches = int(players_number / 2)
            for number in range(1, numbers_matches + 1):
                j = len(list_of_id_players)
                id_player_one = int(list_of_id_players[j - 1])
                id_player_two = int(list_of_id_players[j - 2])
                pair_player = [id_player_one, id_player_two]
                pair_player_two = [id_player_two, id_player_one]
                player_one = player_two = None

                i = numbers_matches - number
                if i <= -1:
                    i = numbers_matches
                while pair_player in list_played_matches or pair_player_two in list_played_matches:
                    id_player_two = list_of_id_players[i]
                    pair_player = [id_player_one, id_player_two]
                    pair_player_two = [id_player_two, id_player_one]
                    i -= 1

                for player in list_of_players:
                    if player[0] == id_player_one:
                        player_one = player
                        list_of_id_players.remove(id_player_one)
                    if player[0] == id_player_two:
                        player_two = player
                        list_of_id_players.remove(id_player_two)
                list_matches_round.append((player_one, player_two))

                if player_one in list_of_players:
                    list_of_players.remove(player_one)
                if player_two in list_of_players:
                    list_of_players.remove(player_two)
            return list_matches_round

        except IndexError:
            print('Shuffle...')
        except ValueError:
            print('Shuffle...')

        try:

            list_matches_round = []
            list_of_players = []
            list_of_id_players = []

            players_number = int(len(sort_by_scores))
            for player in sort_by_scores:
                list_of_players.append((player[0], player[4]))
                list_of_id_players.append(player[0])

            numbers_matches = int(players_number / 2)
            for number in range(1, numbers_matches + 1):
                j = len(list_of_id_players)
                id_player_one = int(list_of_id_players[0])
                id_player_two = int(list_of_id_players[j - 1])
                pair_player = [id_player_one, id_player_two]
                pair_player_two = [id_player_two, id_player_one]
                player_one = player_two = None

                i = number + 1
                if i >= numbers_matches:
                    i = 1
                print(i)
                print(list_of_players, list_of_id_players)
                while pair_player in list_played_matches or pair_player_two in list_played_matches:
                    id_player_two = list_of_id_players[i]
                    pair_player = [id_player_one, id_player_two]
                    pair_player_two = [id_player_two, id_player_one]
                    i += 1
                    print(i, id_player_one, id_player_two)

                for player in list_of_players:
                    if player[0] == id_player_one:
                        player_one = player
                        list_of_id_players.remove(id_player_one)
                    if player[0] == id_player_two:
                        player_two = player
                        list_of_id_players.remove(id_player_two)
                list_matches_round.append((player_one, player_two))

                if player_one in list_of_players:
                    list_of_players.remove(player_one)
                if player_two in list_of_players:
                    list_of_players.remove(player_two)
            return list_matches_round

        except IndexError:
            print('Shuffle...')
        except ValueError:
            print('Shuffle...')
