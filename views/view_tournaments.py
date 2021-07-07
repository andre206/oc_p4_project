#! /usr/bin/env python3
# coding: utf-8
""" view tournaments"""
from controllers.backup_restore_round import deserialized_round
from controllers.new_tournament import participants_tournament


def view_all_tournaments(tournament_table):
    for tournament in tournament_table:
        date_debut = tournament['date_tournament'][0]
        date_fin = tournament['date_tournament'][1]
        date_str = f'{date_debut} - {date_fin}'

        print(f"|ID Tournament : {tournament['id_tournament']:^17}"
              f"|Name : {tournament['name']:^30}"
              f"|Place : {tournament['place']:^38}|\n"
              f"|{'-' * 118}|\n"
              f"|Date(s) of tournament : {date_str:^38}\n"
              f"|{'-' * 118}|\n"
              f"|Control time : {tournament['control_time']:^50}"
              f"| Number of rounds : "
              f"{str(tournament['number_of_round']):^22}\n"
              f"|{'-' * 118}|\n"
              f"|Description : {tournament['description']}|\n"
              f"|{'-' * 118}|\n\n|{'-' * 118}|"
              )


def view_one_tournament(tournament, list_of_players):
    print(f"\n{' ':>40}Result of Tournament {tournament.name}")
    list_round = deserialized_round(tournament.list_of_round)

    applicants = participants_tournament(tournament, list_of_players)

    print("Final score ranking of participants \n")
    i = 1
    for player in applicants:
        print(f"{' ':>20}{i} : {player[0]} - {player[1]} {player[2]} - Total score : {player[3]}\n")
        i += 1
    print(f"\n{' ':>40}Details of the tournament {tournament.name} \n")
    for a_round in list_round:
        number_matches = len(a_round.match_list)
        print(f"\nResult for {a_round.name}")
        for i in range(0, number_matches):
            print(f"{' ':>20}Match {i + 1} : {a_round.match_list[i]}")
