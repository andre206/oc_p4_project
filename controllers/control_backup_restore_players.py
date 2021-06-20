#! /usr/bin/env python3
# coding: utf-8
"""
Permet de sérialiser/désérialiser les joueurs, pour sauvegarder et réimporter les données stockées dans
la mini base de donnée (utilisation de TinyDB et stockage file json)
"""
from tinydb import TinyDB
from models.player import Player


class BackupRestorePlayers:
    """
    gestion of the serliaized data for the players
    """
    def __init__(self):
        pass

    def serialized_player(self,player):
        """
        pour sérialiser un joueur
        :param player: an instance of the Player Class
        :return: a dictionnary with the information of the player
        """
        serialized_player = {
            'id_player': player.id_player,
            'name': player.name,
            'surname': player.surname,
            'date_of_birth': player.date_of_birth,
            'sex': player.sex,
            'ranking': player.ranking,
        }
        return serialized_player

    def serialized_players(self,list_players):
        """
        generation table of players from a list of players
        :param list_players: list of Player()
        :return: players table
        """
        db = TinyDB('controllers/db.json')
        players_table = db.table('players')
        players_table.truncate()

        for player in list_players:
            players_table.insert(BackupRestorePlayers().serialized_player(player))

        return players_table

    def deserialized_players(self,players_table):
        """
        recuparation of list of players from the players table
        :param players_table: the players_table from the db.json
        :return: a list of Player()
        """
        list_players = []
        for entry in players_table.all():
            id_player = entry['id_player']
            name = entry['name']
            surname = entry['surname']
            date_of_birth = entry['date_of_birth']
            sex = entry['sex']
            ranking = entry['ranking']
            player = Player(id_player=id_player,name=name, surname=surname, date_of_birth=date_of_birth, sex=sex,
                            ranking=ranking)
            list_players.append(player)
        return list_players

    def delete_all_users(self, delete_validation, players_table):

        if delete_validation == 'yes':
            players_table.truncate()
            print('Users are deleted')
        else:
            print('Users are not deleted')



if __name__ == '__main__':
    player1 = Player(name='TOTO', surname='toto', date_of_birth='12/06/1984', sex='F')
    player2 = Player(name='TITI', surname='titi', date_of_birth='22/09/1986', sex='M')

    list_players = [player1, player2]

    player_table = BackupRestorePlayers().serialized_players(list_players)

    BackupRestorePlayers().deserialized_players(player_table)
