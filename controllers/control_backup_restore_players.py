"""
Permet de sérialiser/désérialiser les joueurs, pour sauvegarder et réimporter les données stockées dans
la mini base de donnée (utilisation de TinyDB et stockage file json)
"""
from tinydb import TinyDB
from models.player import Player


def serialized_player(player):
    serialized_player = {
        'name': player.name,
        'age': player.age,
    }
    return serialized_player


def serialized_players(list_players):
    db = TinyDB('db.json')
    players_table = db.table('players')
    players_table.truncate()

    for player in list_players:
        players_table.insert(serialized_player(player))

    return players_table

def deserialized_players(players_table):
    list_players = []
    for entry in players_table.all():
        name = entry['name']
        age = entry['age']
        player = Player(name=name, age=age)
        list_players.append(player)
    return list_players

if __name__ == '__main__':
    player1 = Player(name='Toto', age='25')
    player2 = Player(name='Tata', age='30')
    list_players = [player1, player2]
    print(list_players)
    player_table = serialized_players(list_players)
    #print(serialized_players(list_players))
    serialized_players = serialized_players(list_players).all()
    #print(serialized_players)

    deserialized_players(player_table)
    print(deserialized_players(player_table))