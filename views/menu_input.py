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
