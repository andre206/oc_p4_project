#! /usr/bin/env python3
# coding: utf-8
"""
view all players

Functions
---------
view_all_players(player_table, sorted_by='rank')
    view all players in the base. Sorted by rank by default. Possibility to sort by name
"""


def view_all_players(player_table, sorted_by='rank'):
    """
    view all players in the base. Sorted by rank by default. Possibility to sort by name

    Parameters
    ----------
    player_table: tinydb.TinyDB.table
        table players
    sorted_by: str
        sorted by rank by default, possibly by name
    """
    list_players_text = (f" \033[91m{'_' * 118}\n"
                         f" {'ID Player':18}|{'Name':<19}|{'Surname':<19}"
                         f"|{'Date of birth':19}|{'Sex':19}|{'Elo rank':19} \n"
                         f" {'_' * 118} \033[0m\n"
                         )
    print(list_players_text)
    if sorted_by == 'rank':
        player_table = sorted(player_table, key=lambda players: int(players['ranking']), reverse=True)
    elif sorted_by == 'name':
        player_table = sorted(player_table, key=lambda players: players['name'], reverse=False)

    for player in player_table:
        player_text = (f" \033[33m{player['id_player']:^18}|\033[0m"
                       f" {player['name'][0:18]:<18}"
                       f"\033[33m|\033[0m {player['surname'][0:18]:<18}"
                       f"\033[33m|\033[0m{player['date_of_birth']:^19}"
                       f"\033[33m|\033[0m{player['sex']:^19}"
                       f"\033[33m|\033[0m{player['ranking']:^19} \n"
                       f" \033[33m{'-' * 118}\033[0m\n"
                       )
        print(player_text)
    print(f" \033[91m{'_' * 118}\033[0m\n")
