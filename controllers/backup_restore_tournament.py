#! /usr/bin/env python3
# coding: utf-8
"""
This module allows to serialise/deserialise tournaments,
to save and re-import data stored in the
the mini-database (using TinyDB and json file storage)

Functions
---------
serialized_tournament(tournament)
    For a tournament serialization
serialized_tournaments(list_tournaments)
    Generation table of tournaments from a list of tournaments
deserialized_tournaments(tournaments_table)
    Recuperation of list of tournaments from the tournaments table
"""
from tinydb import TinyDB
from models.tournament import Tournament


def serialized_tournament(tournament):
    """
    For a tournament serialization

    Parameters
    ---------
    tournament: Tournament()
        an instance of the Tounament Class

    Returns
    -------
    serialized_tournament_dict : dict
        a dictionnary with the information of the tournament
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
        'number_of_players': tournament.number_of_players,
        'number_of_round': tournament.number_of_round,
        'finished': tournament.finished
    }
    return serialized_tournament_dict


def serialized_tournaments(list_tournaments):
    """
    Generation table of tournaments from a list of tournaments

    Parameters
    ----------
    list_tournaments: list
        list of Player()
    Returns
    -------
    tournaments_table : tinydb.table.Table
        tournaments table
    """
    db = TinyDB('db.json')
    tournaments_table = db.table('tournaments')
    tournaments_table.truncate()

    for tournament in list_tournaments:
        tournaments_table.insert(serialized_tournament(tournament))

    return tournaments_table


def deserialized_tournaments(tournaments_table):
    """
    Recuperation of list of tournaments from the tournaments table

    Parameters
    ----------
    tournaments_table: tinydb.table.Table
        the tournaments_table from the db.json

    Returns
    -------
    list_tournaments : list
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
        number_of_players = entry['number_of_players']
        number_of_round = entry['number_of_round']
        finished = entry['finished']

        tournament = Tournament(name=name, place=place,
                                date_tournament=date_tournament,
                                control_time=control_time,
                                description=description,
                                id_tournament=id_tournament,
                                list_of_round=list_of_round,
                                list_of_players=list_of_players,
                                number_of_players=number_of_players,
                                number_of_round=number_of_round,
                                finished=finished)
        list_tournaments.append(tournament)
    return list_tournaments
