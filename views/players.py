#! /usr/bin/env python3
# coding: utf-8
""" view all players"""


def view_all_players(player_table, sorted_by='rank'):
    print(f" \033[91m{'_' * 118}\n"
          f" {'ID Player':18}|{'Name':<19}|{'Surname':<19}"
          f"|{'Date of birth':19}|{'Sex':19}|{'Elo rank':19} \n"
          f" {'_' * 118} \033[0m\n"
          )
    if sorted_by == 'rank':
        player_table = sorted(player_table, key=lambda players: int(players['ranking']), reverse=True)
    elif sorted_by == 'name':
        player_table = sorted(player_table, key=lambda players: players['name'], reverse=False)

    for player in player_table:
        print(f" \033[33m{player['id_player']:^18}|\033[0m"
              f" {player['name'][0:18]:<18}"
              f"\033[33m|\033[0m {player['surname'][0:18]:<18}"
              f"\033[33m|\033[0m{player['date_of_birth']:^19}"
              f"\033[33m|\033[0m{player['sex']:^19}"
              f"\033[33m|\033[0m{player['ranking']:^19} \n"
              f" \033[33m{'-' * 118}\033[0m\n"
              )
    print(f" \033[91m{'_' * 118}\033[0m\n")
