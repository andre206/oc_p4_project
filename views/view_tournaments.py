#! /usr/bin/env python3
# coding: utf-8
""" view tournaments"""


def view_all_tournaments(tournament_table):
    print(f"|{'-' * 118}|\n"
          f"|{'ID Tournament':18}|{'Name':<19}|{'Place':<19}"
          f"|{'Date':19}|{'Description':39}|"
          f"|{'-' * 118}|"
          )
    
    for tournament in tournament_table:
        print(f"|{tournament['id_tournament']:^18}|{tournament['name'][0:19]:<19}"
              f"|{tournament['place'][0:19]:<19}|{tournament['date']:<19}"
              f"|{tournament['description'][0:39]:<39}|"
              f"|{'-' * 118}|"
              )
