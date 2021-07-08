"""pour voir le classement des joueurs, en fonction des points
classement avant chaque tournoi
si premier tournoi et que pas de classement pré défini,
a définir par la personne qui rentre les utilisateurs
"""

from controllers.for_tournament import participants_tournament


def view_players_tournament(tournament, list_of_players, sort_by):

    applicants = participants_tournament(tournament, list_of_players, sort_by)

    print(f"\033[33m"
          f"{'List of participants':^120} \033[0m\n")
    i = 1
    for player in applicants:
        print(f"{' ':>20}\033[33m{i:3d} : \033[0m"
              f"{player[0]:5} - {player[1]} {player[2]} "
              f"\033[91m{'---':^10}\033[00m"
              f" Total score : {player[3]}\n")
        i += 1