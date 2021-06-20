""" vérifier les donner entrée par l'utilisateur
- si un joueur existe dans la bdd, on le reprend, sinon, on le crée, (on peut modifier le joueur si déjà existant)
- si un classement existe, on le reprend, sinon, on le crée (et on peut réinit si besoin)"""
from datetime import datetime
import re

from models.player import Player
from controllers.control_backup_restore_players import BackupRestorePlayers as BRP

class ControlPlayerEntry:
    def __init__(self):

        pass
    def control_nameplayer(self,name):

        name_valid = re.search(r'[A-Za-zéùàèêëï\-]+', name)
        if name_valid is None:
            print("Le nom n'est pas valide")
            return 0
        else:
            print('OK')
            return 1

        #new_player = Player(name, surname, date_of_birth, sex)
        #return new_player




if __name__ == '__main__':
    #player = ControlUserData().add_player()
    #print(player.date_of_birth)
    ControlUserData().control_nameplayer('')
