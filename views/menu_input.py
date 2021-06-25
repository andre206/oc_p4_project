#! /usr/bin/env python3
# coding: utf-8
""" Menus input globols fonctions and methode"""


def choice_option():
    try:
        option = int(input("Enter your choice : "))
    except ValueError:
        print("You must choose a number")
        option = None
    return option









"""
player_data = db.get(doc_id=1)  # c'est un dictionnaire

player_data["name"]  # manipulation directe du dictionnaire - pas pratique car pas d'autocomplétion et plus verbeux

player = Player(**player_data)  # transmition des clés/valeurs du dictionnaire à l'initialisation d'un objet Player
player.name  # utilisation de la POO pour accéder aux valeurs
player.save()  # on peut aussi utiliser des méthodes, chose impossible en manipulant directement le dictionnaire"""
