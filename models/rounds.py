#! /usr/bin/env python3
# coding: utf-8
"""
Here the model class of a round

Class
-----
Round
    a round instance
"""


class Round:
    """
    Model of a round

    Attributes
    ----------
    name: str
        the round's name
    date_hour_start: date
        date and hour of starting round, None by default
    date_hour_stop: date
        date and hour of ending round, None by default
    match_list: list
        list of matches in a round, None by default
    tournament_id: int
        id of the tournament, None by default
    tournament_name: str
        name of the tournament including the round, None by default
    """
    def __init__(self,
                 name,
                 date_hour_start=None,
                 date_hour_stop=None,
                 match_list=None,
                 tournament_id=None,
                 tournament_name=None,
                 ):
        if match_list is None:
            match_list = []
        self.name = name
        self.date_hour_start = date_hour_start
        self.date_hour_stop = date_hour_stop
        self.match_list = match_list
        self.tournament_id = tournament_id
        self.tournament_name = tournament_name
