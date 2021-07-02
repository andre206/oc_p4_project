#! /usr/bin/env python3
# coding: utf-8
"""
Permet de sérialiser/désérialiser les tournois,
pour sauvegarder et réimporter les données stockées dans
la mini base de donnée (utilisation de TinyDB et stockage file json)
"""
from tinydb import TinyDB
from models.tournament import Tournament



def serialized_tournament(tournament):
    """
    pour sérialiser un tournoi
    :param tournament: an instance of the Tounament Class
    :return: a dictionnary with the information of the tournament
    """
    serialized_tournament_dict = {
        'name': tournament.name,
        'place': tournament.place,
        'date_tournament': tournament.date_tournament,
        'control_time': tournament.control_time,
        'description': tournament.description,
        'id_tournament': tournament.id_tournament,
        'list_of_round': tournament.list_of_round,
        'list_of_players': tournament.list_of_players,
        'number_of_round': tournament.number_of_round,
    }
    return serialized_tournament_dict


def serialized_tournaments(list_tournaments):
    """
    generation table of tournaments from a list of tournaments
    :param list_tournaments: list of Player()
    :return: tournaments table
    """
    db = TinyDB('db.json')
    tournaments_table = db.table('tournaments')
    tournaments_table.truncate()

    for tournament in list_tournaments:
        tournaments_table.insert(serialized_tournament(tournament))

    return tournaments_table


def deserialized_tournaments(tournaments_table):
    """
    recuparation of list of tournaments from the tournaments table
    :param tournaments_table: the tournaments_table from the db.json
    :return: a list of Tournament()
    """
    list_tournaments = []
    for entry in tournaments_table.all():
        name = entry['name']
        place = entry['place']
        date_tournament = entry['date_tournament']
        control_time = entry['control_time']
        description = entry['description']
        id_tournament = entry['id_tournament']
        list_of_round = entry['list_of_round']
        list_of_players = entry['list_of_players']
        number_of_round = entry['number_of_round']

        tournament = Tournament(name=name, place=place,
                                date_tournament=date_tournament,
                                control_time=control_time,
                                description=description,
                                id_tournament=id_tournament,
                                list_of_round=list_of_round,
                                list_of_players=list_of_players,
                                number_of_round=number_of_round)
        list_tournaments.append(tournament)
    return list_tournaments
