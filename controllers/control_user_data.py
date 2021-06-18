""" vérifier les donner entrée par l'utilisateur
- si un joueur existe dans la bdd, on le reprend, sinon, on le crée, (on peut modifier le joueur si déjà existant)
- si un classement existe, on le reprend, sinon, on le crée (et on peut réinit si besoin)"""
from datetime import datetime
from models.player import Player


class ControlUserData:

    def add_player(self):
        name = input("Name : ")
        surname = input("Surname : ")
        date_of_birth = input("Date of birth (jj/mm/aaaa) : ")
        sex = input("sex (M or F) : ")
        new_player = Player(name, surname, date_of_birth,sex)
        return new_player


if __name__ == '__main__':
    player = ControlUserData().add_player()
    print(player.date_of_birth)