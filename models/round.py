"""
round1 = [match1, match2, match3, match4]
Round contient : nom (round1...), date et heure de début,
date et heure de fin (création automatique à la création
d'un tour par l'utilisateur et à son marquage comme terminé)
"""


class Round:
    def __init__(self, name, date_heure_debut=None,
                 date_heure_fin=None, match_list=None):
        if match_list is None:
            match_list = []
        self.name = name
        self.date_heure_debut = date_heure_debut
        self.date_heure_fin = date_heure_fin
        self.match_list = match_list


if __name__ == '__main__':
    name_round = 'Round1'
    round1 = Round(name_round)
    print(round1.name, round1.date_heure_debut,
          round1.date_heure_fin, round1.match_list)
