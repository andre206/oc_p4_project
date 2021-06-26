#! /usr/bin/env python3
# coding: utf-8
"""
Permet de sérialiser/désérialiser les joueurs,
pour sauvegarder et réimporter les données stockées dans
la mini base de donnée (utilisation de TinyDB et stockage file json)
"""
from tinydb import TinyDB
from models.player import Player


def serialized_player(player):
    """
    pour sérialiser un joueur
    :param player: an instance of the Player Class
    :return: a dictionnary with the information of the player
    """
    serialized_player_dict = {
        'name': player.name,
        'surname': player.surname,
        'date_of_birth': player.date_of_birth,
        'sex': player.sex,
        'id_player': player.id_player,
        'ranking': player.ranking,
    }
    return serialized_player_dict


def serialized_players(list_players):
    """
    generation table of players from a list of players
    :param list_players: list of Player()
    :return: players table
    """
    db = TinyDB('db.json')
    players_table = db.table('players')
    players_table.truncate()

    for player in list_players:
        players_table.insert(serialized_player(player))

    return players_table


def deserialized_players(players_table):
    """
    recuparation of list of players from the players table
    :param players_table: the players_table from the db.json
    :return: a list of Player()
    """
    list_players = []
    for entry in players_table.all():
        name = entry['name']
        surname = entry['surname']
        date_of_birth = entry['date_of_birth']
        sex = entry['sex']
        id_player = entry['id_player']
        ranking = entry['ranking']
        player = Player(name=name, surname=surname,
                        date_of_birth=date_of_birth,
                        sex=sex, id_player=id_player,
                        ranking=ranking)
        list_players.append(player)
    return list_players


def delete_all_users(delete_validation, players_table):
    if delete_validation == 'yes':
        players_table.truncate()
        print('Users are deleted')
    else:
        print('Users are not deleted')
