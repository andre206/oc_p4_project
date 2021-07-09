#! /usr/bin/env python3
# coding: utf-8
"""
This module allows to serialise/deserialise players,
to save and re-import data stored in the
the mini-database (using TinyDB and json file storage)
"""
from tinydb import TinyDB
from models.player import Player


def serialized_player(player):
    """
    for a player serialisation

    Parameters
    ---------
    player: Player
        an instance of the Player Class

    Returns
    ------
    serialized_player_dict : dict
        a dictionary with the information of the player
    """
    serialized_player_dict = {
        'name': player.name,
        'surname': player.surname,
        'date_of_birth': player.date_of_birth,
        'sex': player.sex,
        'id_player': player.id_player,
        'ranking': player.ranking,
        'score': player.score,
    }
    return serialized_player_dict


def serialized_players(list_players):
    """
    generation table of players from a list of players

    Parameters
    ----------
    list_players: list
        list of Player()

    Returns
    -------
    players_table : tinydb.table.Table
        players table
    """
    db = TinyDB('db.json')
    players_table = db.table('players')
    players_table.truncate()

    for player in list_players:
        players_table.insert(serialized_player(player))
    print(type(players_table))
    return players_table


def deserialized_players(players_table):
    """
    recuperation of list of players from the players table

    Parameters
    ----------
    players_table: tinydb.table.Table
        the players_table from the db.json

    Returns
    -------
    list_players : list
        a list of Player()
    """
    list_players = []
    for entry in players_table.all():
        name = entry['name']
        surname = entry['surname']
        date_of_birth = entry['date_of_birth']
        sex = entry['sex']
        id_player = entry['id_player']
        ranking = entry['ranking']
        score = entry['score']
        player = Player(
            name=name,
            surname=surname,
            date_of_birth=date_of_birth,
            sex=sex,
            id_player=id_player,
            ranking=ranking,
            score=score
        )
        list_players.append(player)
    return list_players
