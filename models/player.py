#! /usr/bin/env python3
# coding: utf-8
"""
Here the model class for a player.

Class
-----
Player
    a player
"""


class Player:
    """
    Model for one player

    Attributes
    ----------
    name: str
        the name of the player
    first_name: str
        the first name of the player
    date_of_birth: datetime
        date of the birth, in format 01/01/1900
    sex: str
        Male or Female (M or F)
    id_player: int
        the id of player, by default = 0
    ranking: int
        the ranking of the player, by default = 0
    score: float
        the score of a player,  by default = 0
    """
    def __init__(self, name, first_name,
                 date_of_birth, sex,
                 id_player=0, ranking=0,
                 score=0.0):

        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.id_player = id_player
        self.ranking = ranking
        self.score = score
