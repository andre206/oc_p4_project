""" vérifier les donner entrée par l'utilisateur
- si un joueur existe dans la bdd, on le reprend,
sinon, on le crée, (on peut modifier le joueur si déjà existant)
- si un classement existe, on le reprend, sinon, on le crée
(et on peut réinit si besoin)"""
from datetime import datetime
import re


def control_name_surname_player(name_surname):
    name_surname_valid = re.search(r"[A-Za-zéùàèêëï\-]", name_surname)
    if name_surname_valid is None:
        print("the entry is not valid.")
        return 0
    else:
        return 1


def control_date(date_to_control):
    try:
        datetime.strptime(date_to_control, "%d/%m/%Y")
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


def control_id(id):
    try:
        int(id)
        return 1
    except ValueError:
        print("Please, take a number ID")
        return 0


def control_id_reuse(id, list_id, list_ids):
    for ids in list_id:
        if int(id) == ids:
            print("This ID already used. Please select another one.")
            return 0
    for ids in list_ids:
        if int(id) == ids:
            return 1
    print("Non-existent ID, please select an existent ID")
    return 0


def control_choice(choice):
    if choice.upper() == 'YES':
        return 1
    else:
        return 0
