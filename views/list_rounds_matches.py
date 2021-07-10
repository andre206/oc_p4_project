""" voir les paires de joueurs à initier au début de chaque round
premier round : joueur 1 - joueur 5
second round, par points puis par rang si les points sont identiques :
round 2 : joueur 1 - joueur 2, et si déjà rencontré,
 alors joueur 1- joueur 3 et joueur 2 joueur 4 etc..."""

from controllers.backup_restore_round import deserialized_round


def view_rounds_matches(tournament, list_of_players):
    list_round = deserialized_round(tournament.list_of_round)

    for a_round in list_round:
        view_matches_a_round(a_round, list_of_players)


def view_matches_a_round(a_round, list_of_players):
    number_matches = len(a_round.match_list)
    fin = a_round.date_heure_fin
    if a_round.date_heure_fin is None:
        fin = "in progress"
    print(f"\n {' ':>10}\033[91m{a_round.name} start : {a_round.date_heure_debut:10} --- "
          f"stop : {fin}\n")
    for i in range(0, number_matches):
        id_player_one = int(a_round.match_list[i][0][0])
        id_player_two = int(a_round.match_list[i][1][0])
        player_one = id_player_one
        player_two = id_player_two
        score_player_one = score_player_two = None
        for player in list_of_players:
            if id_player_one == int(player.id_player):
                player_one = player
                score_player_one = float(a_round.match_list[i][0][1])
            elif id_player_two == int(player.id_player):
                player_two = player
                score_player_two = float(a_round.match_list[i][1][1])

        print(f"\033[33mMatch {i + 1} : \033[91m{player_one.id_player} -\033[0m "
              f"{player_one.name:19} {player_one.surname:19} - {score_player_one:3} "
              f"\033[33m{'---':^5} \033[91m{player_two.id_player} -\033[0m "
              f"{player_two.name:19} {player_two.surname:19} - {score_player_two:3} \n")
