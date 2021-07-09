""" voir les paires de joueurs à initier au début de chaque round
premier round : joueur 1 - joueur 5
second round, par points puis par rang si les points sont identiques :
round 2 : joueur 1 - joueur 2, et si déjà rencontré,
 alors joueur 1- joueur 3 et joueur 2 joueur 4 etc..."""

from controllers.backup_restore_round import deserialized_round


def view_rounds_matches(tournament, list_of_players):
    list_round = deserialized_round(tournament.list_of_round)

    for a_round in list_round:
        number_matches = len(a_round.match_list)
        print(f"\n {' ':>10}\033[91mResult for {a_round.name}\n")
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

            print(f"\033[33mMatch {i + 1} : \033[0m"
                  f"{player_one.name:20} {player_one.surname:20} - {score_player_one:3} "
                  f"\033[91m{'---':^5} \033[0m"
                  f"{player_two.name:20} {player_two.surname:20} - {score_player_two:3} \n")


if __name__ == '__main__':
    from tinydb import TinyDB
    from controllers.backup_restore_players import deserialized_players
    from controllers.backup_restore_tournament import deserialized_tournaments
    from controllers.for_tournament import tournament_in_progress

    db = TinyDB('C:\Git\oc_p4_project\db.json')
    players_table = db.table('players')
    tournaments_table = db.table('tournaments')

    tournaments_table = deserialized_tournaments(tournaments_table)
    list_of_players = deserialized_players(
        players_table
    )
    tournament = tournament_in_progress(tournaments_table, 1)

    view_rounds_matches(tournament, list_of_players)
