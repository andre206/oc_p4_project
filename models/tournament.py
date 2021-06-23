""" Module concernant le tournoi
Chaque tournoi doit contenir :
- un nom
- un lieu
- une date de tournoi ou une plage de date
- un nombre de tour (par défaut 4, mais soit être modifiable par l'utilisateur)
- tournée : la liste des instances de round
- joueurs : la liste des indices correspondant aux instances du joueur stockées en mémoire
- contrôle du temps (bullet, blitz ou coup rapide)
- description (remarques générales du directeur du tournoi)
tournoi = |round1, round2, round3...]
"""


class Tournament:

    def __init__(self, name, place, date, control_time, description, id_tournament=0, list_of_round=None,
                 list_of_players=None, number_of_round=4):
        self.name = name
        self.place = place
        self.date = date
        self.control_time = control_time
        self.description = description
        self.id_tournament = id_tournament
        self.list_of_round = list_of_round
        self.list_of_players = list_of_players
        self.number_of_round = number_of_round
