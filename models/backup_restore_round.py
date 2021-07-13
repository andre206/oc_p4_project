#! /usr/bin/env python3
# coding: utf-8
"""
This module allows to serialise/deserialise rounds,
to save and re-import data stored in the
the mini-database (using TinyDB and json file storage)

Functions
---------
serialized_round(a_round)
    for a round serialization
deserialized_round(list_of_round_dict)
     Recuperation of round from the tournaments table
"""
from models.rounds import Round


def serialized_round(a_round):
    """
    for a round serialization

    Parameters
    ----------
    a_round: Round
        an instance of the Round Class

    Returns
    -------
    serialized_round_dict : dict
        a dictionnary with the information of a round
    """
    serialized_round_dict = {
        'name': a_round.name,
        'date_hour_start': a_round.date_hour_start,
        'date_hour_stop': a_round.date_hour_stop,
        'match_list': a_round.match_list,
        'tournament_id': a_round.tournament_id,
        'tournament_name': a_round.tournament_name,
    }
    return serialized_round_dict


def deserialized_round(list_of_round_dict):
    """
     Recuperation of round from the tournaments table

     Parameters
     ----------
     list_of_round_dict: dict
        a list of round_dict from the db.json

    Returns
    -------
    list_of_round : list
        a list of Round()
    """

    list_of_round = []
    for round_dict in list_of_round_dict:
        name = round_dict['name']
        date_hour_start = round_dict['date_hour_start']
        date_hour_stop = round_dict['date_hour_stop']
        match_list = round_dict['match_list']
        tournament_id = round_dict['tournament_id']
        tournament_name = round_dict['tournament_name']

        a_round = Round(
            name=name,
            date_hour_start=date_hour_start,
            date_hour_stop=date_hour_stop,
            match_list=match_list,
            tournament_id=tournament_id,
            tournament_name=tournament_name
        )
        list_of_round.append(a_round)

    return list_of_round
