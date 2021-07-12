#! /usr/bin/env python3
# coding: utf-8
"""
Control specific for tournament creation and/or modification

Class
-----
ControlEntryTournament
    to control input user, specially for tournament options

Functions
---------
tournament_in_progress(tournament_table, id_tournament)
    control that th id of the tournament progress is known
participants_tournament(tournament, list_of_players, sort_by='score')
    calculate the current score of the participants of a tournament
    and to return the list of participants with the updated scores.
"""
import re
from controllers.maximum_round import max_rounds_without_duplicate
from controllers.backup_restore_round import deserialized_round





def participants_tournament(tournament, list_of_players, sort_by='score'):
    """
    calculate the current score of the participants of a tournament
    and to return the list of participants with the updated scores.

    Parameters
    ----------
    tournament : Tournament
        an instance of tournament class
    list_of_players : list
        a list of players
    sort_by : str
        for select the method to sort players. By score by default. Possibly by name.

    Returns
    -------
    applicants : list
        a list of participants tournament, sorted, with update scores.
    """
    applicants = []
    list_round = deserialized_round(tournament.list_of_round)

    for a_round in list_round:
        number_matches = len(a_round.match_list)
        for i in range(0, number_matches):
            id_player_one = int(a_round.match_list[i][0][0])
            id_player_two = int(a_round.match_list[i][1][0])
            for player in list_of_players:
                if id_player_one == int(player.id_player):
                    player.score += float(a_round.match_list[i][0][1])
                elif id_player_two == int(player.id_player):
                    player.score += float(a_round.match_list[i][1][1])

    for player in list_of_players:
        if player.id_player in tournament.list_of_players:
            applicants.append(
                [
                    player.id_player,
                    player.name,
                    player.surname,
                    player.score,
                    player.ranking
                ]
            )
    if sort_by == 'score':
        applicants = sorted(applicants, key=lambda x: x[3], reverse=True)
    elif sort_by == 'name':
        applicants = sorted(applicants, key=lambda x: x[2])

    return applicants


class ControlEntryTournament:
    """

    Attributes
    ----------
    input_user = str
        the name place input by the user

    Methods
    -------
    control_mane_place_tournament(name_place)
        check that the name of the tournament place is correctly define
    control_time_control(control_time)
        check that the control time is correctly define
    control_number_of_players(number_of_players)
        check that the number of player is correct (even players)
    control_number_of_round(number_of_round, number_of_players)
        check that the number of round selected by the user is correct
    """
    def __init__(self, input_user):
        self.input_user = input_user

    def control_name_place_tournament(self):
        """
        Check that the name place contains some letters.

        Returns
        -------
        0 : int
            if the name place doesn't match the pattern
        1 : int
            if the name place matches pattern
        """
        name_place_valid = re.search(r"[A-Za-zéùàèêëï\- ]", self.input_user)
        if name_place_valid is None:
            print("\033[91mInvalid entry\033[0m\n")
            return 0
        else:
            return 1

    def control_time_control(self):
        """
        Check that the control time is correctly define
        the entry must be 1, 2 or 3.

        Returns
        -------
        choice_control : int
            if the control time dosen't match pattern
        choice_control : str
            if the control time matches patern. Return 'bullet', 'blitz' or
            'quick hit'
        """
        control_time_valid = re.search(r'^[123]$', self.input_user)
        choice_control = 0
        if control_time_valid is None:
            print("\033[91mYou must choose between the option 1, 2 or 3\033[0m\n")
        else:
            if self.input_user == '1':
                choice_control = 'bullet'
            elif self.input_user == '2':
                choice_control = 'blitz'
            elif self.input_user == '3':
                choice_control = 'quick hit'
        return choice_control

    def control_number_of_players(self):
        """
        Check that the number of players charged by the user is correct and even

        Parameters
        ----------
        number_of_players : str
            input by the user

        Returns
        -------
        0 : int
            if number of players is not valid
        1 : int
            if number of players is valid
        """
        number_valid = re.search(r'^[\d]{1,3}$', self.input_user)
        if number_valid is None:
            return 0
        elif int(self.input_user) % 2 != 0:  # Must be a multiple of 2 for making matches
            print("\033[91mThe number of players must be even to play the matches\033[0m\n")
            return 0
        else:
            return 1

    def control_number_of_round(self, number_of_players):
        """
        Check that the number of rounds charged by the user is correct,
        and that it does not exceed the maximum number of rounds possible
        depending on the number of players in the tournament.

        Parameters
        __________
        number_of_players : str
            number input by the user

        Returns
        -------
        0 : int
            if number of rounds is not valid
        1 : int
            if number of rounds is valid

        """
        number_valid = re.search(r'^[\d]{1,3}$', self.input_user)

        if number_valid is None:
            return 0
        max_rounds = max_rounds_without_duplicate(int(number_of_players))
        if max_rounds < int(self.input_user):
            print(f"\033[33mMaximum rounds for {number_of_players} players is"
                  f" \033[91m{max_rounds} \033[0m")
            return 0
        else:
            return 1

    def tournament_in_progress(self, tournament_table):
        """
        control that th id of the tournament progress is known

        Parameters
        ----------
        tournament_table : list
            list of tournament registered in the base
        id_tournament : str
            input by the user

        Returns
        -------
        tournament : Tournament()
            an instance of the Tournament class. Corresponding to the id tournament input by the user
            if known in the base
        False : binary
            if the ID doesn't correspond with a known id tournament
        """
        for tournament in tournament_table:
            if tournament.id_tournament == int(self.input_user):
                return tournament
        print("\033[91mProblem with tournament ID\33[0m\n")
        return False
