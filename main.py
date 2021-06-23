#! /usr/bin/env python3
# coding: utf-8
from tinydb import TinyDB

from controllers.backup_restore_players import deserialized_players
from controllers.menu_choices import SwitcherMainMenu as Smm
from views.menu_input import choice_option

if __name__ == '__main__':
    pass
db = TinyDB('db.json')
players_table = db.table('players')
tournaments_table = db.table('tournaments')

main_option = None
Smm(players_table, tournaments_table).option_selected(main_option)

while main_option != 0:
    main_option = choice_option()
    Smm(players_table, tournaments_table).option_selected(main_option)
