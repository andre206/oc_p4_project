#! /usr/bin/env python3
# coding: utf-8
""" Tournament menu choices
contains all class for make choice in the appliance about tournament.
"""
from time import sleep
from datetime import datetime

from controllers.menu_choices import SwitcherMenu
from controllers.backup_restore_tournament import (
    deserialized_tournaments,
    serialized_tournaments,
)
from controllers.backup_restore_round import (
    serialized_round,
    deserialized_round,
)
from controllers.backup_restore_players import (
    deserialized_players,
    serialized_players,
)
from controllers.menu_input import choice_option
from controllers.appairing_players import RoundGenerated
from views.decorators_menus import (
    pre_menu,
    tournament_menu,
    tournament_modify_menu,
    tournament_modify_sub_menu,
)
from views.menu_input_tournament import (
    new_tournament,
    modify_tournament,
)
from views.view_tournaments import view_all_tournaments
from views.view_players import view_all_players
from views.menu_input_tournament import (
    add_players,
    modify_tournament_players,
    add_result_round,
)
from models.tournament import Tournament
from models.round import Round


class SwitcherTournamentMenu(SwitcherMenu):
    @pre_menu
    @tournament_menu
    def option_selected(self, selected_option):
        super().option_selected(selected_option)

    def option_1(self):
        print(f"{'Add new tournament':^120}\n")
        list_tournament = deserialized_tournaments(self.tournaments_table)
        self.id_tournament = len(list_tournament) + 1
        element_tournament = new_tournament()
        new = Tournament(element_tournament[0], element_tournament[1],
                         element_tournament[2], element_tournament[3],
                         element_tournament[4], self.id_tournament)
        list_tournament.append(new)

        self.tournaments_table = serialized_tournaments(list_tournament)

    def option_2(self):
        print(f"{'View all tournament':^120}\n")
        view_all_tournaments(self.tournaments_table)

    def option_3(self):
        print(f"{'Modify one tournament':^120}\n")
        modify_option = None
        SwitcherModifyTournament(
            self.players_table, self.tournaments_table) \
            .option_selected(modify_option)
        while modify_option != 0:
            modify_option = choice_option()
            SwitcherModifyTournament(
                self.players_table, self.tournaments_table) \
                .option_selected(modify_option)
        tournament_option = None
        SwitcherTournamentMenu(
            self.players_table, self.tournaments_table) \
            .option_selected(tournament_option)

    def option_0(self):
        print(f"\n{'Back to main menu':^120}\n")
        sleep(1)


class SwitcherModifyTournament(SwitcherMenu):

    @pre_menu
    @tournament_modify_menu
    def option_selected(self, selected_option):
        super().option_selected(selected_option)

    def option_1(self):
        """
        select the tournament to modify
        """
        view_all_tournaments(self.tournaments_table)
        select_tournament = modify_tournament(self.tournaments_table)
        if select_tournament == 0:
            SwitcherModifyTournament(
                self.players_table,
                self.tournaments_table
            ).option_selected(0)
        else:
            sub_modify_tournament_option = None
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
            .option_selected(0)

    def option_0(self):
        sleep(0.5)


class SwitcherModifyTournamentSub(SwitcherMenu):
    @pre_menu
    @tournament_modify_sub_menu
    def option_selected(self, selected_option):
        super().option_selected(selected_option)

    def option_1(self):
        """
        Add players on tournament
        - search in the players database the registred players.
        - if it si not 8 players, redirection to the add players
        in the player gestion
        """
        list_possible_players = deserialized_players(self.players_table)
        if len(list_possible_players) < 8:
            print(f" Actually only {len(list_possible_players)} players are "
                  f"known in the players base.\n"
                  f" Please go to the 'Players gestion' to add new players in"
                  f"the base.")
        else:
            tournaments_table = deserialized_tournaments(
                self.tournaments_table
            )
            for tournament in tournaments_table:
                if tournament.id_tournament == int(self.id_tournament):
                    tournament_in_progress = tournament
                    print(f" {'Add players on tournament':>70} "
                          f"{tournament_in_progress.name}\n"
                          )
                    view_all_players(self.players_table)

                    list_ids = []
                    for player in self.players_table:
                        list_ids.append(player['id_player'])
                    if len(tournament_in_progress.list_of_players) == 8:
                        print("Players are already registered. ")
                        list_players = modify_tournament_players(list_ids)
                        if list_players is not None:
                            tournament_in_progress.list_of_players = list_players
                    else:
                        list_players = add_players(list_ids)
                        tournament_in_progress.list_of_players = list_players
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
        """
        print(f"{'Starting Round':^120}\n")
        tournaments_table = deserialized_tournaments(
            self.tournaments_table
        )
        for tournament in tournaments_table:
            if tournament.id_tournament == int(self.id_tournament):
                tournament_in_progress = tournament

                nb_max_round = int(tournament_in_progress.number_of_round)
                list_of_round = tournament_in_progress.list_of_round
                if list_of_round is None:
                    nb_round = 0
                else:
                    nb_round = len(list_of_round)
                if nb_round >= nb_max_round:
                    print(
                        f"Number of rounds in the {tournament_in_progress.name} "
                        f": {nb_round} / {nb_max_round}\n"
                        f"It's the Tournament's end.")
                else:
                    print(
                        f"Number of rounds in the {tournament_in_progress.name} "
                        f": {nb_round} / {nb_max_round}\n\n")
                    list_of_round = deserialized_round(tournament_in_progress.list_of_round)
                    result = True
                    for a_round in list_of_round:
                        if a_round.date_heure_fin is None:
                            print(f"The round {a_round.name} must be "
                                  f"ending before starting a new round")
                            result = False
                    if result:
                        print(f"Initialization of Round{nb_round + 1}\n")
                        tournaments_table.remove(tournament_in_progress)
                        round_name = f"Round{nb_round + 1}"
                        date_start = datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
                        print(date_start)
                        new_round = Round(
                            name=round_name,
                            date_heure_debut=date_start,
                            tournament_id=tournament_in_progress.id_tournament,
                            tournament_name=tournament_in_progress.name
                        )

                        list_all_players = deserialized_players(self.players_table)
                        list_player_tournament = []
                        for player in list_all_players:
                            for id_player in tournament_in_progress.list_of_players:
                                if id_player == player.id_player:
                                    list_player_tournament.append(player)

                        sort_by_rank = RoundGenerated(
                            list_player_tournament
                        ).sorted_players_rank()
                        if round_name == 'Round1':
                            for player in list_player_tournament:
                                player.score = 0
                            first_round_matches = RoundGenerated(
                                list_player_tournament,
                                sort_by_rank,
                            ).first_round()

                            new_round.match_list = first_round_matches
                            new_round = serialized_round(new_round)
                            tournament_in_progress.list_of_round.append(new_round)
                        else:
                            print(round_name)
                        for player in list_player_tournament:
                            for player_all in list_all_players:
                                if player.id_player == player_all.id_player:
                                    list_all_players.remove(player_all)

                        for player in list_player_tournament:
                            list_all_players.append(player)
                        tournaments_table.append(tournament_in_progress)


                        self.players_table = serialized_players(list_all_players)
        self.tournaments_table = serialized_tournaments(tournaments_table)

    def option_3(self):
        """
        Ending Round and add results
        -select the round that does not yet have an end date
        -enter the scores of the matches
        -add the end date and time
        -save the round in the tournament rounds list
        """
        print(f"{'Ending Round and add results':^120}\n")
        tournaments_table = deserialized_tournaments(
            self.tournaments_table
        )
        for tournament in tournaments_table:
            if tournament.id_tournament == int(self.id_tournament):
                tournament_in_progress = tournament
                tournaments_table.remove(tournament_in_progress)
                list_of_round = deserialized_round(tournament_in_progress.list_of_round)
                list_of_round_dict = []
                for a_round in list_of_round:
                    if a_round.date_heure_fin is None:
                        date_stop = datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
                        print(f"Ending of round {a_round.name} : "
                              f"{date_stop}")
                        a_round.date_heure_fin = date_stop
                        print(f"Enter results for the {a_round.name} \n"
                              f"[0] : lost, [0.5] : equal [1] : win\n")
                        add_result_round(a_round.match_list, self.players_table)
                    list_of_round_dict.append(serialized_round(a_round))

                tournament_in_progress.list_of_round = list_of_round_dict
                tournaments_table.append(tournament_in_progress)
        self.tournaments_table = serialized_tournaments(tournaments_table)

    def option_0(self):
        sleep(0.5)
