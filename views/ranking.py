"""
For view players of one tournament, sort by score or by name

Functions
---------
view_players_tournament(tournament, list_of_players, sort_by)
    view all players of a tournament, sort by score or by name
"""

from controllers.for_tournament import participants_tournament


def view_players_tournament(tournament, list_of_players, sort_by):
    """
    view all players of a tournament, sort by score or by name

    Parameters
    ----------
    tournament: Tournament
        an instance of tournament class
    list_of_players: list
        list of players in the tournament
    sort_by: str
        must be 'score' or 'name'
    """
    applicants = participants_tournament(tournament, list_of_players, sort_by)

    print(f"\033[33m"
          f"{'List of participants':^120} \033[0m\n")
    i = 1
    for player in applicants:
        player_text = (f"{' ':>20}\033[33m{i:3d} : \033[0m"
                       f"{player[0]:5} - {player[1]:20} {player[2]:20} "
                       f"\033[91m{'---':^10}\033[00m"
                       f" Total score : {player[3]}\n")
        print(player_text)
        i += 1
