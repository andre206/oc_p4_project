"""
view rounds and matches in a round


Functions
---------
view_rounds_matches(tournament, list_of_players)
    view all matches in al round for a tournament
    call the function view_matches_a_round(a_round, list_of_players)
view_matches_a_round(a_round, list_of_players)
    view all matches in a round
"""

from models.backup_restore_round import deserialized_round


def view_rounds_matches(tournament, list_of_players):
    """
    view all matches in al round for a tournament
    call the function view_matches_a_round(a_round, list_of_players)

    Parameters
    ----------
    tournament : Tournament
        an instance of Tournament class
    list_of_players: list
        list of players
    """
    list_round = deserialized_round(tournament.list_of_round)

    for a_round in list_round:
        view_matches_a_round(a_round, list_of_players)


def view_matches_a_round(a_round, list_of_players):
    """
    view all matches in a round

    Parameters
    ----------
    a_round: Round
        an instance of Round class
    list_of_players: list
        a list of players
    """
    number_matches = len(a_round.match_list)
    fin = a_round.date_hour_stop
    if a_round.date_hour_stop is None:
        fin = "in progress"
    title = (f"\n {' ':>10}\033[91m{a_round.name} start : {a_round.date_hour_start:10} --- "
             f"stop : {fin}\n")
    print(title)

    for i in range(0, number_matches):
        id_player_one = int(a_round.match_list[i][0][0])
        id_player_two = int(a_round.match_list[i][1][0])
        player_one = id_player_one
        player_two = id_player_two
        score_player_one = score_player_two = 0
        for player in list_of_players:
            if id_player_one == int(player.id_player):
                player_one = player
                score_player_one = float(a_round.match_list[i][0][1])
            elif id_player_two == int(player.id_player):
                player_two = player
                score_player_two = float(a_round.match_list[i][1][1])
        match_text = (f"\033[33mMatch {i + 1} : \033[91m{player_one.id_player:3} -\033[0m "
                      f"{player_one.name:19} {player_one.first_name:19} - {score_player_one:3} "
                      f"\033[33m{'---':^5} \033[91m{player_two.id_player:3} -\033[0m "
                      f"{player_two.name:19} {player_two.first_name:19} - {score_player_two:3} \n")
        print(match_text)
