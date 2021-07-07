#! /usr/bin/env python3
# coding: utf-8
""" view all players"""


def view_all_players(player_table, sorted_by='rank'):
    print(f"|{'-' * 118}|\n"
          f"|{'ID Player':18}|{'Name':<19}|{'Surname':<19}"
          f"|{'Date of birth':19}|{'Sex':19}|{'Elo rank':19}|"
          f"|{'-' * 118}|"
          )
    if sorted_by == 'rank':
        player_table = sorted(player_table, key=lambda players: int(players['ranking']), reverse=True)
    elif sorted_by == 'name':
        player_table = sorted(player_table, key=lambda players: players['name'], reverse=False)

    for player in player_table:
        print(f"|{player['id_player']:^18}|{player['name'][0:19]:<19}"
              f"|{player['surname'][0:19]:<19}|{player['date_of_birth']:^19}"
              f"|{player['sex']:^19}|{player['ranking']:^19}|"
              f"|{'-' * 118}|"
              )

if __name__ == '__main__':
    from tinydb import TinyDB

    db = TinyDB('C:\Git\oc_p4_project\db.json')
    players_table = db.table('players')

    view_all_players(players_table, 'name')