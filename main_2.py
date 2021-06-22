#! /usr/bin/env python3
# coding: utf-8
from tinydb import TinyDB

from controllers.backup_restore_players import BackupRestorePlayers as BRP
from controllers.main_menu import SwitcherMainMenu as SMM
from views.menu import choice_option

if __name__ == '__main__':
    pass
db = TinyDB('db.json')
players_table = db.table('players')
list_players = BRP().deserialized_players(players_table)

main_option = None
SMM(players_table).option_selected(main_option)

while main_option != 0:
    main_option = choice_option()
    SMM(players_table).option_selected(main_option)
