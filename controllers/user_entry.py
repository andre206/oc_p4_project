""" vérifier les donner entrée par l'utilisateur
- si un joueur existe dans la bdd, on le reprend, sinon, on le crée, (on peut modifier le joueur si déjà existant)
- si un classement existe, on le reprend, sinon, on le crée (et on peut réinit si besoin)"""
from datetime import datetime
import re


def control_name_surname_player(name_surname):
    name_surname_valid = re.search(r"[A-Za-zéùàèêëï\-]", name_surname)
    if name_surname_valid is None:
        print("the entry is not valid.")
        return 0
    else:
        return 1


def control_date_of_birth(date_of_birth):
    try:
        datetime.strptime(date_of_birth, "%d/%m/%Y")
        return 1

    except ValueError:
        print("Please, take a date with format 'dd/mm/yyyy'")
        return 0


def control_sex(sex):
    sex_valid = re.search(r"^[MF]$", sex.upper())
    if sex_valid is None:
        print("Please, type 'M' or 'F'")
        return 0
    else:
        return 1


def control_ranking(ranking):
    if ranking == '':
        ranking = 0
    try:
        int(ranking)
        return 1
    except ValueError:
        return 0


def control_id_player(id_player):
    try:
        int(id_player)
        return 1
    except ValueError:
        print("Please, take a number ID player")
        return 0