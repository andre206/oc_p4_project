#! /usr/bin/env python3
# coding: utf-8
"""
check the data entered by the user

Classes
-------
ControlGlobalEntry:
    class for test global input from user
ControlEntryTournament
    to control input user, specially for tournament options

"""
from datetime import datetime
import re

from controllers.maximum_round import max_rounds_without_duplicate


class ControlGlobalEntry:
    """
    class for test global input from user

    Attributes
    ----------
    input_user: str
        the input from the consol by user

    Methods
    ---------
    control_name_surname_player(self)
        control the entry name_surname, if it's matches the pattern
    control_date(self)
        control that the entry is a date in format dd/mm/yyyy
    control_sex(self)
        control that entry is F or M
    control_ranking(self)
        control that the entry is an integer, minimum 1000
    control_id(self)
        control  the the entry is an integer
    control_id_reuse(self, list_id, list_ids)
        control that the id is used just one time by the user, for exemple to add
        player in a tournament, you can't add twice the same person
    control_choice(self)
        for control an user choice, like change users in tournament before starting it
    control_result_match(self)
        control that the entry is 1 or 0.5 or 1.
    """
    def __init__(self, input_user):
        self.input_user = input_user

    def control_name_surname_player(self):
        """
        control the entry name_surname, if it's matches the pattern

        Returns
        -------
        0 : int
            if the name or surname doesn't match pattern
        1 : int
            if the name or surname matches pattern
        """
        name_surname_valid = re.search(r"[A-Za-zéùàèêëï\-]", self.input_user)
        if name_surname_valid is None:
            print("the entry is not valid.")
            return 0
        else:
            return 1

    def control_date(self):
        """
        control that the entry is a date in format dd/mm/yyyy

        Raises
        ------
        ValueError : datetime
            the date is not a datetime

        Returns
        -------
        0 : int
            if the entry is not valid
        1 : int
            if the entry is valid
        """
        try:
            datetime.strptime(self.input_user, "%d/%m/%Y")
            return 1

        except ValueError:
            print("Please, take a date with format 'dd/mm/yyyy'")
            return 0

    def control_sex(self):
        """
        control that entry is F or M

        Returns
        -------
        0 : int
            if the sex doesn't match pattern
        1 : int
            if the sex matches pattern

        """
        sex_valid = re.search(r"^[MF]$", self.input_user.upper())
        if sex_valid is None:
            print("Please, type 'M' or 'F'")
            return 0
        else:
            return 1

    def control_ranking(self):
        """
        control that the entry is an integer, minimum 1000

        Raises
        ------
        ValueError : int
            the ranking must changed in an integer.

        Returns
        -------
        0: int
            if the ranking is not valid
        1: int
            if the ranking is not valid
        """
        if self.input_user == '':
            self.input_user = 0

        try:
            int(self.input_user)
            if int(self.input_user) < 1000 and int(self.input_user) != 0:
                print('Minimum rank is 1000')
                return 0
            return 1
        except ValueError:
            return 0

    def control_id(self):
        """
        control  the the entry is an integer

        Raises
        ------
        ValueError: int
            the a_id must be changed in an integer

        Returns
        -------
        0: int
            if the a_id is not valid
        1: 1
            if the a_id is valid
        """
        try:
            int(self.input_user)
            return 1
        except ValueError:
            print("Please, take a number ID")
            return 0

    def control_id_reuse(self, list_id, list_ids):
        """
        control that the id is used just one time by the user, for exemple to add
        player in a tournament, you can't add twice the same person

        Parameters
        ----------
        list_id: list
            a list of used id
        list_ids: list
            a list of existing id

        Returns
        -------
        0: int
            if the id is already used
        1: int
            if the id is not used yet
        """
        for ids in list_id:
            if int(self.input_user) == ids:
                print("This ID already used. Please select another one.")
                return 0
        for ids in list_ids:
            if int(self.input_user) == ids:
                return 1
        print("Non-existent ID, please select an existent ID")
        return 0

    def control_choice(self):
        """
        for control an user choice, like change users in tournament before starting it

        Returns
        -------
        0: int
            if choice is not yes
        1: int
            if choice is yes
        """
        if self.input_user.upper() == 'YES':
            return 1
        else:
            return 0

    def control_result_match(self):
        """
        control that the entry is 1 or 0.5 or 1.

        Raises
        ------
        ValueError: str
            the result must be a number

        Returns
        -------
        0: int
            if invalid result
        1: int
            if valid result
        """
        try:
            if float(self.input_user) == 1 or float(self.input_user) == 0 or float(self.input_user) == 0.5:
                return 1
            else:
                print("[0] : lost --- [0.5] : equal --- [1] : win")
                return 0
        except ValueError:
            print("[0] : lost --- [0.5] : equal --- [1] : win")
            return 0


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
