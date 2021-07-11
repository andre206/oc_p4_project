#! /usr/bin/env python3
# coding: utf-8
"""
Here the model class of a tournament

Class
-----
Tournament
    a tournament instance
"""


class Tournament:
    """
    model for a tournament

    Attributes
    ----------
    name: str
        name of tournament
    place: str
        the place where playing tournament
    date_tournament: list
        a list contains start and stop tournament
        (allows you to manage tournaments over several days)
    control_time: str
        the type of control time (bullet, blitz or quick time)
    description: str
        the description of tournament
    id_tournament: int
        the id of tournament, by default = 0
    list_of_round: list
        list of round, [] by default
    list_of_players: list
        list of players id, [] by default
    number_of_players: int
        number of players, 8 by default
    number_of_round: int
        number of round, 4 by default
    finished: boolean
        status of tournament, False by default
    """

    def __init__(self, name, place, date_tournament,
                 control_time, description,
                 id_tournament=0,
                 list_of_round=None,
                 list_of_players=None,
                 number_of_players=8,
                 number_of_round=4,
                 finished=False):
        if list_of_players is None:
            list_of_players = []
        if list_of_round is None:
            list_of_round = []
        self.name = name
        self.place = place
        self.date_tournament = date_tournament
        self.control_time = control_time
        self.description = description
        self.id_tournament = id_tournament
        self.list_of_round = list_of_round
        self.list_of_players = list_of_players
        self.number_of_players = number_of_players
        self.number_of_round = number_of_round
        self.finished = finished
