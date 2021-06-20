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


class Player:
    """
    Model for one player
    """

    def __init__(self, id_player=0, name="", surname="", date_of_birth="", sex="", ranking=0):
        """
        :param name: the name of the player
        :param surname: the surname of the player
        :param date_of_birth: date of the birth, in format 01/01/1900
        :param sex: Male or Female (M or F)
        """
        self.id_player = id_player
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.ranking = ranking

    def scoring(self):
        pass









