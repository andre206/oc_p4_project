#! /usr/bin/env python3
# coding: utf-8
"""
This module allows to serialise/deserialise rounds,
to save and re-import data stored in the
the mini-database (using TinyDB and json file storage)
"""
from models.round import Round


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
        'date_heure_debut': a_round.date_heure_debut,
        'date_heure_fin': a_round.date_heure_fin,
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
        date_heure_debut = round_dict['date_heure_debut']
        date_heure_fin = round_dict['date_heure_fin']
        match_list = round_dict['match_list']
        tournament_id = round_dict['tournament_id']
        tournament_name = round_dict['tournament_name']

        a_round = Round(
            name=name,
            date_heure_debut=date_heure_debut,
            date_heure_fin=date_heure_fin,
            match_list=match_list,
            tournament_id=tournament_id,
            tournament_name=tournament_name
        )
        list_of_round.append(a_round)

    return list_of_round
