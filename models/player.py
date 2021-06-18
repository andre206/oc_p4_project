""" Ici les informations pour la création des joueurs.
Doit contenir :
- nom de famille
- prénom
- Date de naissance
- sexe
- classement (un chiffre positif)
- score (0 au début de chaque tournoi)
- un numéro d'instance de joueur (indice)
-faire une vérification si un joueur existe, sinon le créer- pas de gestion de suppression des joueurs pour le moment"""

from tinydb import TinyDB

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def serialized_players(player):
    serialized_player = {
        'name': player.name,
        'age': player.age,
    }
    return serialized_player


player1 = Player(name= 'Toto', age= '25')
player2 = Player(name='Tata', age='30')
list = [player1,player2]
db = TinyDB('db.json')
players_table = db.table('players')
players_table.truncate()

for player in list:
    players_table.insert(serialized_players(player))

print(players_table)
serialized_players = players_table.all()
print(serialized_players)




