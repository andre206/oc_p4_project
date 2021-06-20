import platform
import os
import time

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
        print('|{:1}|'.format('-' * 118))
        print("| @ @@ @ {} @ @@ @ |".format(' ' * 102))
        print("| @@@@@@ {} @@@@@@ |".format(' ' * 102))
        print("|   @@   {} {} {}   @@   |".format(' ' * 39, '#' * 22, ' ' * 39))
        print("|  @@@@  {} ## Chess Tournament ## {}  @@@@  |".format(' ' * 39, ' ' * 39))
        print("| @@@@@@ {} {} {} @@@@@@ |".format(' ' * 39, '#' * 22, ' ' * 39))
        print("|@@@@@@@@{}@@@@@@@@|".format(' ' * 102))
        print('|{:1}|'.format('-' * 118))
        suite_menu(*args, **kwargs)

    return avant_menu


class PrincipalMenu:
    """ class with all menus for the appliance"""

    @entete_menu
    def main_menu(self):
        """
        print the main menu
        """
        print("|{:^118}|".format('Principal Menu'))
        print('|{:1}|'.format('-' * 118))
        print('|{:1}|'.format('-' * 118))
        print("|{:>45}{:<30s}{:>43}|".format(' ', '[1] Tournament gestion', ' '))
        print("|{:>45}{:<30s}{:>43}|".format(' ', '[2] Players gestion', ' '))
        print("|{:>45}{:<30s}{:>43}|".format(' ', '[3] Reports', ' '))
        print("|{:>45}{:<30s}{:>43}|".format(' ', '[0] Exit Chess Tournament', ' '))
        print('|{:1}|'.format('-' * 118))


class PlayersMenu:
    @entete_menu
    def __init__(self):
        """ print the player menu on the console
        """
        print("|{:^118}|".format('Player gestion '))
        print('|{:1}|'.format('-' * 118))
        print('|{:1}|'.format('-' * 118))
        print("|{:>45}{:<30s}{:>43}|".format(' ', '[1] Add new player', ' '))
        print("|{:>45}{:<30s}{:>43}|".format(' ', '[2] View all player', ' '))
        print("|{:>45}{:<30s}{:>43}|".format(' ', '[3] Modify one player', ' '))
        print("|{:>45}{:<30s}{:>43}|".format(' ', '[4] Delete all player', ' '))
        print("|{:>45}{:<30s}{:>43}|".format(' ', '[0] Return principal menu', ' '))
        print('|{:1}|'.format('-' * 118))

    def new_user(self):
        name = input("Name : ").upper()
        while Cpe().control_name_surname_player(name) == 0:
            name = input("Name : ").upper()

        surname = input("Surname : ").capitalize()
        while Cpe().control_name_surname_player(surname) == 0:
            surname = input("Surname : ").capitalize()

        date_of_birth = input("Date of birth (jj/mm/aaaa) : ")
        while Cpe().control_date_of_birth(date_of_birth) == 0:
            date_of_birth = input("Date of birth (jj/mm/aaaa) : ")

        sex = input("sex (M or F) : ").upper()
        while Cpe().control_sex(sex) == 0:
            sex = input("sex (M or F) : ").upper()

        ranking = input("Ranking : (Leave blank if no classification yet) ")
        while Cpe().control_ranking(ranking) == 0:
            ranking = input("Ranking : (Leave blank if no classification yet) ")

        print(name, surname, date_of_birth, sex, ranking)

        time.sleep(2)
        return name, surname, date_of_birth, sex, ranking

    def view_all_users(self, player_table):
        print('|{0:1}|'.format('-' * 118))
        print('|{0:14}'.format('ID Player'),
              '|{0:<19}'.format('Name'),
              '|{0:<19}'.format('Surname'),
              '|{0:19}'.format('Date od birth'),
              '|{0:19}'.format('Sex'),
              '|{0:18}|'.format('Ranking'),
              )
        print('|{:1}|'.format('-' * 118))
        for player in player_table:
            print('|{0:^14}'.format(player['id_player']),
                  '|{0:<19}'.format(player['name'][0:19]),
                  '|{0:<19}'.format(player['surname'][0:19]),
                  '|{0:^19}'.format(player['date_of_birth']),
                  '|{0:^19}'.format(player['sex']),
                  '|{0:^18}|'.format(player['ranking']),
                  )
        print('|{:1}|'.format('-' * 118))
        pass

    def delete_all_user(self):
        validation_delete = input("Are your sure to delete all users ?"
                                  "This action is irreversible"
                                  "Type 'yes' to confirm : ")
        return validation_delete


class ModifyPlayer(PlayersMenu):

    @entete_menu
    def __init__(self):
        """ print the modify menu on the console
        """
        print("|{:^118}|".format('Player gestion '))
        print('|{:1}|'.format('-' * 118))
        print('|{:1}|'.format('-' * 118))
        print("|{:>45}{:<30s}{:>43}|".format(' ', '[1] Choose the ID player to modify', ' '))
        print("|{:>45}{:<30s}{:>43}|".format(' ', '[0] Return Player gestion', ' '))
        print('|{:1}|'.format('-' * 118))

    def view_all_users(self, player_table):
        super().view_all_users(player_table)

    def modify_player(self, id_player, player_table):
        for player in player_table:
            if player['id_player'] == int(id_player):
                print(player)


if __name__ == "__main__":

    tab = [["nom", "prenom", "age"], ["kate", "lyne", "22"], ["sara", "parker", "78"]]

    form = "{0:10}{1:10}{2:10}"
    for val in tab:
        print(form.format(*val))
    pass
