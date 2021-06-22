
import time

from views.decorators_menus import pre_menu
from controllers.user_data import ControlPlayerEntry as CPE

def choice_option():
    try:
        option = int(input("Enter your option P: "))
    except ValueError:
        print("You must choose a number")
        option = None
    return option


class PlayersMenu:

    def new_user(self):
        name = input("Name : ").upper()
        while CPE().control_name_surname_player(name) == 0:
            name = input("Name : ").upper()
        print(f"name : {name}")
        surname = input("Surname : ").capitalize()
        while CPE().control_name_surname_player(surname) == 0:
            surname = input("Surname : ").capitalize()
        print(f"surname : {surname}")
        date_of_birth = input("Date of birth (jj/mm/aaaa) : ")
        while CPE().control_date_of_birth(date_of_birth) == 0:
            date_of_birth = input("Date of birth (jj/mm/aaaa) : ")
        print(f"date of birth : {date_of_birth}")
        sex = input("sex (M or F) : ").upper()
        while CPE().control_sex(sex) == 0:
            sex = input("sex (M or F) : ").upper()
        print(f"sex : {sex}")
        ranking = input("Ranking : (Leave blank if no classification yet) ")
        while CPE().control_ranking(ranking) == 0:
            ranking = input("Ranking : (Leave blank if no classification yet) ")
        print(f"ranking : {ranking}")

        time.sleep(2)
        return name, surname, date_of_birth, sex, ranking

    def view_all_users(self, player_table):
        print(f"|{'-' * 118}|\n"
              f"|{'ID Player':18}|{'Name':<19}|{'Surname':<19}"
              f"|{'Date of birth':19}|{'Sex':19}|{'Ranking':19}|"
              f"|{'-' * 118}|"
              )

        for player in player_table:
            print(f"|{player['id_player']:^18}|{player['name'][0:19]:<19}"
                  f"|{player['surname'][0:19]:<19}|{player['date_of_birth']:^19}"
                  f"|{player['sex']:^19}|{player['ranking']:^19}|"
                  f"|{'-' * 118}|"
                  )

    def delete_all_user(self):
        validation_delete = input("Are your sure to delete all users ?"
                                  "This action is irreversible"
                                  "Type 'yes' to confirm : ")
        return validation_delete


class ModifyPlayer(PlayersMenu):

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
"""
player_data = db.get(doc_id=1)  # c'est un dictionnaire

player_data["name"]  # manipulation directe du dictionnaire - pas pratique car pas d'autocomplétion et plus verbeux

player = Player(**player_data)  # transmition des clés/valeurs du dictionnaire à l'initialisation d'un objet Player
player.name  # utilisation de la POO pour accéder aux valeurs
player.save()  # on peut aussi utiliser des méthodes, chose impossible en manipulant directement le dictionnaire"""
