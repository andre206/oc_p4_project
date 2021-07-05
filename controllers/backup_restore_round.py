#! /usr/bin/env python3
# coding: utf-8
"""
Permet de sérialiser un round pour l'intégrer dans un tournoi,
pour sauvegarder et réimporter les données stockées dans
la mini base de donnée (utilisation de TinyDB et stockage file json)
"""
from models.round import Round


def serialized_round(a_round):
    """
    pour sérialiser un round
    :param a_round: an instance of the Round Class
    :return: a dictionnary with the information of the tournament
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
     recuparation of round from the tournaments table
    :param round_dict: the round_dict from the db.json
    :return: a Round()
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
