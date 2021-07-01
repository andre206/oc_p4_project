#! /usr/bin/env python3
# coding: utf-8
""" view tournaments"""


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
