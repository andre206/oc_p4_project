#! /usr/bin/env python3
# coding: utf-8
"""
view tournaments -
--> all tournaments
--> a specific tournament
--> first information about tournament
--> all informations

Functions
---------
view_all_tournaments(tournament_table)
    view a list of all tournament in the base
view_all_tournaments(tournament_table)
    view information of one specify tournament
first_informations_about_tournament(tournament)
    view the first information of a tournament, including id, name, date start and stop,
    number of round, number of players, status
report_all_informations_one_tournament(tournament)
    for reporting all informations of one tournament, including the first informations and
    place, control time and description
"""

from models.backup_restore_tournament import deserialized_tournaments
from controllers.for_tournament import participants_tournament
from views.list_rounds_matches import view_rounds_matches


def view_all_tournaments(tournament_table):
    """
    Display a list of all Tournament
    just the first informations

    Parameters
    ----------
    tournament_table: tinydb.TinyDB.table
        tournaments table
    """
    table_tournament = deserialized_tournaments(tournament_table)
    all_tournament = sorted(table_tournament, key=lambda tournaments: tournaments.id_tournament)
    for tournament in all_tournament:
        first_informations_about_tournament(tournament)


def view_one_tournament(tournament, list_of_players):
    """
    view information of one specify tournament

    Parameters
    ----------
    tournament: Tournament
        an instance of tournament class
    list_of_players: list
        a list of players
    """
    title_text = (f"\n\033[33m{'Result of Tournament':^120} \n"
                  f"\033[91m{tournament.name:^120}\033[0m\n"
                  f"\n\033[33m{'Final score ranking of participants':^120}\033[0m \n")

    print(title_text)

    applicants = participants_tournament(tournament, list_of_players)
    i = 1

    for player in applicants:
        player_text = (f"{' ':>20}\033[33m{i:3d} : \033[0m"
                       f"{player[0]:5} - {player[1]:20} {player[2]:20} "
                       f"\033[91m{'---':^10}\033[00m"
                       f" Total score : {player[3]}\n")
        print(player_text)
        i += 1

    print(f"\n{' ':>40}\033[33mDetails of the tournament {tournament.name} \033[0m\n")
    view_rounds_matches(tournament, list_of_players)


def first_informations_about_tournament(tournament):
    """
    view the first information of a tournament, including id, name, date start and stop,
    number of round, number of players, status

    Parameters
    ----------
    tournament: Tournament
        an instance of tournament class
    """
    date_debut = tournament.date_tournament[0]
    date_fin = tournament.date_tournament[1]
    date_str = f'{date_debut} - {date_fin}'
    if tournament.finished:
        status = 'Finished'
    else:
        status = "In progress"
    information_text = (f"\033[91m {'_' * 118} \033[0m\n"
                        f" \033[33mID Tournament :\033[0m {tournament.id_tournament:<10} "
                        f"\033[33m| Name : \033[0m{tournament.name:30} "
                        f"\033[33m| Date(s) of tournament : \033[0m{date_str}\n"
                        f"\033[91m {'-' * 118} \033[0m \n"
                        f" \033[33mNumber of rounds :  \033[0m"
                        f"{str(len(tournament.list_of_round)):>3}/{str(tournament.number_of_round):3}"
                        f"\033[33m| Number of players : \033[0m{tournament.number_of_players:<5} "
                        f"\033[33m| Status : \033[0m{status}\n"
                        f"\033[91m {'_' * 118} \033[0m\n"
                        )
    print(information_text)


def report_all_informations_one_tournament(tournament):
    """
    for reporting all informations of one tournament, including the first informations and
    place, control time and description

    Parameters
    ----------
    tournament: Tournament
        an instance of tournament class
    """
    first_informations_about_tournament(tournament)
    other_informations = (f"\033[33m Place :\033[0m {tournament.place:19}"
                          f"\033[33m| Control Time :\033[0m {tournament.control_time}\n"
                          f"\033[91m {'-' * 118} \033[0m \n"
                          f" \033[33mDescription :\033[0m {tournament.description:>5}\n"
                          f"\033[91m {'_' * 118} \033[0m\n")
    print(other_informations)
