import platform
import os
import json

from controllers.control_user_data import ControlPlayerEntry as Cpe


def clean():
    """For clean the console display"""
    p = platform.system()
    commands = {"Windows": "cls", "Linux": "clear"}
    try:
        os.system(commands[p])
    except:  # empty string or Java os name
        print(chr(27) + "[2J")


def entete_menu(suite_menu):
    """ for the title of the appliance"""

    def avant_menu(*args, **kwargs):
        clean()
        print("-------------------------------------------------------------------------------------------------------")
        print("| @ @@ @                                                                                       @ @@ @ |")
        print("| @@@@@@                                                                                       @@@@@@ |")
        print("|   @@                                       ######################                              @@   |")
        print("|  @@@@                                      ## Chess Tournament ##                             @@@@  |")
        print("| @@@@@@                                     ######################                            @@@@@@ |")
        print("|@@@@@@@@                                                                                     @@@@@@@@|")
        print("|-----------------------------------------------------------------------------------------------------|")
        suite_menu(*args, **kwargs)

    return avant_menu


class Menus:
    """ class with all menus for the appliance"""

    @entete_menu
    def main_menu(self):
        """
        print the main menu
        """
        print("|                                                Principal Menu                                       |")
        print("|-----------------------------------------------------------------------------------------------------|")
        print("|                                                                                                     |")
        print("|                                            [1] Tournament gestion                                   |")
        print("|                                            [2] Players gestion                                      |")
        print("|                                            [0] Exit Chess Tournament                                |")
        print("-------------------------------------------------------------------------------------------------------")

    @entete_menu
    def players_menu(self):
        """ print the player menu on the console
        """
        print("|                                                Player gestion                                       |")
        print("|-----------------------------------------------------------------------------------------------------|")
        print("|                                                                                                     |")
        print("|                                            [1] Add new player                                       |")
        print("|                                            [2] View all player                                      |")
        print("|                                            [0] Return principal menu                                |")
        print("|-----------------------------------------------------------------------------------------------------|")

    def new_user(self):
        name = input("Name : ")
        while Cpe().control_nameplayer(name) == 0:
            name = input("Name : ")
        surname = input("Surname : ")
        date_of_birth = input("Date of birth (jj/mm/aaaa) : ")
        sex = input("sex (M or F) : ")
        ranking = input("Ranking : ")

        print(name, surname, date_of_birth, sex, ranking)
        return name, surname, date_of_birth, sex, ranking

    def view_all_users(self, list_player):
        print('|{:1}|'.format('-' * 101))
        print('|{:14}|'.format('ID Player'),
              '|{:15}|'.format('Name'),
              '|{:15}|'.format('Surname'),
              '|{:14}|'.format('Date od birth'),
              '|{:14}|'.format('Sex'),
              '|{:14}|'.format('Ranking'),
              )
        print('|{:1}|'.format('-'*101))
        for player in list_player:
            print('|{:^14}|'.format(player['id_player']),
                  '|{:15}|'.format(player['name']),
                  '|{:15}|'.format(player['surname']),
                  '|{:^14}|'.format(player['date_of_birth']),
                  '|{:^14}|'.format(player['sex']),
                  '|{:^14}|'.format(player['ranking']),
                  )
        print('|{:1}|'.format('-' * 101))
        pass


if __name__ == "__main__":

    tab = [["nom", "prenom", "age"], ["kate", "lyne", "22"], ["sara", "parker", "78"]]

    form = "{0:10}{1:10}{2:10}"
    for val in tab:
        print(form.format(*val))
    pass
