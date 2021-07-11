#! /usr/bin/env python3
# coding: utf-8
"""
Tournament menu choices
contains all class for make choice in the appliance about tournament.

Classes
-----
SwitcherTournamentMenu(SwitcherMenu)
    interact with the tournaments management menu
SwitcherModifyTournament(SwitcherMenu)
    menu for selected one specific tournament
SwitcherModifyTournamentSub(SwitcherMenu)
    interact with menu of one specific tournament
"""
from time import sleep
from datetime import datetime

from controllers.menu_choices import SwitcherMenu
from controllers.backup_restore_tournament import (
    deserialized_tournaments,
    serialized_tournaments,
)
from controllers.for_tournament import (
    tournament_in_progress,
)
from controllers.backup_restore_round import (
    serialized_round,
    deserialized_round,
)
from controllers.backup_restore_players import (
    deserialized_players,
    serialized_players,
)
from controllers.menu_input import (
    choice_option,
    selected_tournament,
)
from controllers.appairing_players import (
    RoundGenerated,
    remove_playing_matches,
)
from views.decorators_menus import (
    pre_menu,
    tournament_menu,
    tournament_modify_menu,
    tournament_modify_sub_menu,
)
from views.menu_input_tournament import (
    new_tournament,
    add_result_tournoi,
    add_players,
    modify_tournament_players,
    add_result_round
)
from views.tournaments import (
    view_all_tournaments,
    view_one_tournament,
)
from views.players import view_all_players
from views.list_rounds_matches import view_matches_a_round
from models.tournament import Tournament
from models.round import Round


class SwitcherTournamentMenu(SwitcherMenu):
    """
    interact with the tournaments management menu
    daughter class of the SwitcherMenu class

    Attributes (inherited by the SwitcherMenu)
    ------
    players_table : tinydb.table.Table
    tournaments_table : tinydb.table.Table
    id_player : None (str/int)
    id_tournament : None (str/int)

    Methods
    -------
    option_selected(self, selected_option)
        method to retrieve the option chosen by the user
    option_1(self)
        For add a new tournament
    option_2(self)
        View all tournament in the base
    option_3(self)
        For modify one specific tournament
    option_0()
        Option for return to the main menu
    """
    @pre_menu
    @tournament_menu
    def option_selected(self, selected_option):
        """
        method inherited from the SwitcherMenu class
        retrieve the option chosen by the user

        Parameters
        ----------
        selected_option : str
            input by the user
        """
        super().option_selected(selected_option)

    def option_1(self):
        """
        Adding a new tournament.
        All precedent tournaments must be finished before adding a new tournament
        adding_tournament = True
        """
        print(f"\033[33m{'Add new tournament':^120}\033[0m\n")
        list_tournament = deserialized_tournaments(self.tournaments_table)
        adding_tournament = True
        name_tournament_in_progress = str(None)
        for tournament in list_tournament:
            if not tournament.finished:
                name_tournament_in_progress = tournament.name
                adding_tournament = False
        if adding_tournament:
            self.id_tournament = len(list_tournament) + 1
            element_tournament = new_tournament()
            tournament = Tournament(
                name=element_tournament[0],
                place=element_tournament[1],
                date_tournament=element_tournament[2],
                control_time=element_tournament[3],
                description=element_tournament[4],
                id_tournament=self.id_tournament,
                number_of_round=element_tournament[5],
                number_of_players=element_tournament[6]
            )
            list_tournament.append(tournament)

            self.tournaments_table = serialized_tournaments(list_tournament)
        else:
            print(f"The tournament \033[33m{name_tournament_in_progress}\033[0m is always in progress. \n"
                  f"\033[91mYous must finished this tournament before adding a new.\033[0m\n")

    def option_2(self):
        """
        View all tournaments in the base
        """
        print(f"\033[33m{'View all tournament':^120}\033[0m\n")
        view_all_tournaments(self.tournaments_table)

    def option_3(self):
        """
        Modify one tournament
        Open the menu to choose an ID tournament for modification
        """
        print(f"\033[33m{'Modify one tournament':^120}\033[0m\n")
        modify_option = str(None)
        SwitcherModifyTournament(
            self.players_table, self.tournaments_table) \
            .option_selected(modify_option)
        while modify_option != 0:
            modify_option = choice_option()
            SwitcherModifyTournament(
                self.players_table, self.tournaments_table) \
                .option_selected(modify_option)
        tournament_option = str(None)
        SwitcherTournamentMenu(
            self.players_table,
            self.tournaments_table).option_selected(tournament_option)

    @staticmethod
    def option_0():
        """
        Back to main menu
        """
        print(f"\033[95m\n{'Back to main menu':^120}\n\033[0m")
        sleep(0.5)


class SwitcherModifyTournament(SwitcherMenu):
    """
    Menu for selected one specific tournament

    Attributes (inherited by the SwitcherMenu)
    ------
    players_table : tinydb.table.Table
    tournaments_table : tinydb.table.Table
    id_player : None (str/int)
    id_tournament : None (str/int)

    Methods
    -------
    option_selected(self, selected_option)
        method to retrieve the option chosen by the user
    option_1(self)
        Select the tournament id to modify
    option_0()
        Back to tournaments gestion menu

    """
    @pre_menu
    @tournament_modify_menu
    def option_selected(self, selected_option):
        """
        method inherited from the SwitcherMenu class
        retrieve the option chosen by the user

        Parameters
        ----------
        selected_option : str
            input by the user
        """
        super().option_selected(selected_option)

    def option_1(self):
        """
        select the tournament id to modify
        """
        view_all_tournaments(self.tournaments_table)
        select_tournament = selected_tournament(self.tournaments_table)
        if select_tournament == 0:
            SwitcherModifyTournament(
                self.players_table,
                self.tournaments_table
            ).option_selected('0')
        else:
            sub_modify_tournament_option = str(None)
            SwitcherModifyTournamentSub(
                self.players_table,
                self.tournaments_table,
                select_tournament
            ).option_selected(sub_modify_tournament_option)

            while sub_modify_tournament_option != 0:
                sub_modify_tournament_option = choice_option()
                SwitcherModifyTournamentSub(
                    self.players_table,
                    self.tournaments_table,
                    self.id_tournament,
                    select_tournament
                ).option_selected(sub_modify_tournament_option)

        SwitcherModifyTournament(self.players_table, self.tournaments_table) \
            .option_selected('0')

    @staticmethod
    def option_0():
        """
        Back to tournaments gestion menu
        """
        sleep(0.5)


class SwitcherModifyTournamentSub(SwitcherMenu):
    """
    interact with menu of one specific tournament

    Attributes (inherited by the SwitcherMenu)
    ------
    players_table : tinydb.table.Table
    tournaments_table : tinydb.table.Table
    id_player : None (str/int)
    id_tournament : None (str/int)

    Methods
    -------
    option_selected(self, selected_option)
        method to retrieve the option chosen by the user
    option_1(self)
        Add players on tournament
    option_2(self)
        Starting Round
    option_3(self)
        Ending Round and add results
    option_4(self)
        View result of the tournament
    option_0()
        back to the menu to select one tournament
    """
    @pre_menu
    @tournament_modify_sub_menu
    def option_selected(self, selected_option):
        """
        method inherited from the SwitcherMenu class
        retrieve the option chosen by the user

        Parameters
        ----------
        selected_option : str
            input by the user
        """
        super().option_selected(selected_option)

    def option_1(self):
        """
        Add players on tournament
        - search in the players database the registered players.
        - if len(list_possible_players) < number_of_players, redirection to the add players
        in the player gestion
        - saving players in players table with scores = 0
        - saving players of tournament in tournament table
        """
        list_possible_players = deserialized_players(self.players_table)
        tournaments_table = deserialized_tournaments(
            self.tournaments_table
        )
        tournament = tournament_in_progress(tournaments_table, self.id_tournament)

        if tournament:
            adding_players = True
            if len(tournament.list_of_round) != 0:
                adding_players = False
            if adding_players:
                number_of_players = int(tournament.number_of_players)
                if len(list_possible_players) < number_of_players:
                    print(f" Actually only {len(list_possible_players)} players are "
                          f"known in the players base. This tournament needs {number_of_players} "
                          f"players to be full.\n"
                          f" \033[91mPlease go to the 'Players gestion' to add new players in "
                          f"the base.\033[0m\n")
                else:

                    print(f" \033[33m{'Add players on tournament':^120}\033[0m \n"
                          f"{'-----':^120}\n"
                          f"\033[91m{tournament.name:^120}\033[0m\n"
                          )
                    # reinit scores players
                    for player in list_possible_players:
                        player.score = 0.0
                    self.players_table = serialized_players(list_possible_players)
                    view_all_players(self.players_table)

                    list_ids = []
                    for player in self.players_table:
                        list_ids.append(player['id_player'])
                    if len(tournament.list_of_players) == number_of_players:
                        print("\033[91mPlayers are already registered.\033[0m ")
                        list_players = modify_tournament_players(list_ids)
                        if list_players is not None:
                            tournament.list_of_players = list_players
                    else:
                        list_players = add_players(list_ids, number_of_players)
                        tournament.list_of_players = list_players
            elif tournament.finished:
                print(f"Tournament {tournament.name} was finished.\n"
                      f"\033[91mYou cannot add/modify players.\033[0m\n")
            else:
                print(f"Tournament {tournament.name} is in progress yet.\n"
                      f"\033[91mYou cannot add/modify players.\033[0m\n")
        self.tournaments_table = serialized_tournaments(tournaments_table)

    def option_2(self):
        """
        Starting Round
        - search the existing rounds for the tournament,
        - initialize the next one by looking at the maximum
        rounds' number defined at the tournament creation
        - add a start date and hour
        - generate the matches for the round
        - Save the round in the tournament round list
        - saving players in players table
        - saving players of tournament in tournament table
        """
        print(f"\033[33m{'Starting Round':^120}\033[0m\n")
        tournaments_table = deserialized_tournaments(
            self.tournaments_table
        )
        tournament = tournament_in_progress(tournaments_table, self.id_tournament)
        if tournament:
            nb_max_round = int(tournament.number_of_round)
            list_of_round = tournament.list_of_round
            if list_of_round is None:
                nb_round = 0
            else:
                nb_round = len(list_of_round)
            print(
                f"Number of rounds in the {tournament.name} "
                f":\033[91m {nb_round} / {nb_max_round}\033[0m\n\n")
            if nb_round >= nb_max_round:
                print("Maximum number of rounds for the tournament reached.\n")
            else:
                list_of_round = deserialized_round(list_of_round)
                result = True
                for a_round in list_of_round:
                    if a_round.date_heure_fin is None:
                        print(f"\033[91mThe round {a_round.name} must be "
                              f"ending before starting a new round\033[0m\n")
                        result = False
                if result:
                    print(f"\033\33mInitialization of Round{nb_round + 1}\033[0m\n")
                    tournaments_table.remove(tournament)
                    round_name = f"Round{nb_round + 1}"
                    date_start = datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
                    new_round = Round(
                        name=round_name,
                        date_heure_debut=date_start,
                        tournament_id=tournament.id_tournament,
                        tournament_name=tournament.name
                    )

                    list_all_players = deserialized_players(self.players_table)
                    list_player_tournament = []
                    for player in list_all_players:
                        for id_player in tournament.list_of_players:
                            if id_player == player.id_player:
                                list_player_tournament.append(player)

                    sort_by_rank = RoundGenerated(
                        list_player_tournament
                    ).sorted_players_rank()
                    if round_name == 'Round1':
                        first_round_matches = RoundGenerated(
                            list_player_tournament,
                        ).first_round(sort_by_rank)

                        new_round.match_list = first_round_matches

                    else:
                        sort_by_scores = RoundGenerated(
                            list_player_tournament
                        ).sorted_players_scores()
                        list_of_possible_match = RoundGenerated(
                            list_player_tournament
                        ).list_of_possibilities()

                        list_of_pairs = []  # for played matches

                        for a_round in list_of_round:
                            for a_match in a_round.match_list:
                                match_id = (a_match[0][0], a_match[1][0])
                                match_id = sorted(match_id)
                                list_of_pairs.append(match_id)
                        list_of_possible_match, list_matches_played = remove_playing_matches(
                            list_of_possible_match,
                            list_of_pairs
                        )

                        this_round_matches = RoundGenerated(
                            list_player_tournament
                        ).other_round(list_matches_played, sort_by_scores)
                        new_round.match_list = this_round_matches

                    view_matches_a_round(new_round, list_player_tournament)
                    new_round = serialized_round(new_round)

                    tournament.list_of_round.append(new_round)

                    for player in list_player_tournament:
                        for player_all in list_all_players:
                            if player.id_player == player_all.id_player:
                                list_all_players.remove(player_all)

                    for player in list_player_tournament:
                        list_all_players.append(player)
                    tournaments_table.append(tournament)

                    self.players_table = serialized_players(list_all_players)
        self.tournaments_table = serialized_tournaments(tournaments_table)

    def option_3(self):
        """
        Ending Round and add results
        -select the round that does not yet have an end date
        -enter the scores of the matches
        -add the end date and time
        -save the round in the tournament rounds list
        - saving players in players table
        - saving players of tournament in tournament table
        """
        print(f"{'Ending Round and add results':^120}\n")
        tournaments_table = deserialized_tournaments(
            self.tournaments_table
        )
        list_of_players = deserialized_players(
            self.players_table
        )
        tournament = tournament_in_progress(tournaments_table, self.id_tournament)
        if tournament:
            tournament = tournament
            tournaments_table.remove(tournament)
            list_of_round = deserialized_round(tournament.list_of_round)
            list_of_round_dict = []
            number_of_teminate_round = 0
            for a_round in list_of_round:

                if a_round.date_heure_fin is None:
                    date_stop = datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
                    print(f"Ending of round {a_round.name} : "
                          f"{date_stop}")
                    a_round.date_heure_fin = date_stop
                    view_matches_a_round(a_round, list_of_players)
                    print(f"\033[33mEnter results for the {a_round.name} \n"
                          f"\033[91m[0] :\033[0m lost, "
                          f"\033[91m[0.5] :\033[0m equal "
                          f"\033[91m[1] :\033[0m win\n")
                    add_result_round(a_round.match_list, self.players_table)

                number_of_teminate_round += 1
                list_of_round_dict.append(serialized_round(a_round))

            tournament.list_of_round = list_of_round_dict
            self.players_table = serialized_players(list_of_players)

            if int(number_of_teminate_round) == int(tournament.number_of_round) \
                    and not tournament.finished:

                print("\033[33mIt's over - Please enter the new ELO rank for all players :\033[0m\n")

                applicants = add_result_tournoi(tournament, list_of_players)
                for player in applicants:
                    for all_player in list_of_players:
                        if player[0] == all_player.id_player:
                            all_player.ranking = player[4]
                tournament.finished = True
                self.players_table = serialized_players(list_of_players)
            tournaments_table.append(tournament)
        self.tournaments_table = serialized_tournaments(tournaments_table)

    def option_4(self):
        """
        View result of the tournament
        """
        tournaments_table = deserialized_tournaments(
            self.tournaments_table
        )
        list_of_players = deserialized_players(self.players_table)
        tournament = tournament_in_progress(tournaments_table, self.id_tournament)
        view_one_tournament(tournament, list_of_players)

    @staticmethod
    def option_0():
        """
        back to the menu to select one tournament
        """
        sleep(0.5)
