from controllers.control_user_data import ControlUserData as cud
class menu:

    def principal_menu(self):
        print('------------------------------------------------------------')
        print(' @ @@ @                                              @ @@ @ ')
        print(' @@@@@@                                              @@@@@@ ')
        print('   @@             ######################               @@   ')
        print('  @@@@            ## Chess Tournament ##              @@@@  ')
        print(' @@@@@@           ######################             @@@@@@ ')
        print('@@@@@@@@                                            @@@@@@@@')
        print('|----------------------------------------------------------|')
        print('|                      Principal Menu                      |')
        print('|----------------------------------------------------------|')
        print('|                                                          |')
        print("|                     [1] Players gestion                  |")
        print("|                     [2] Tournament gestion               |")
        print("|                     [0] Exit Chess Tournament            |")
        print('------------------------------------------------------------')

    def players_menu(self):
        print('------------------------------------------------------------')
        print(' @ @@ @                                              @ @@ @ ')
        print(' @@@@@@                                              @@@@@@ ')
        print('   @@             ######################               @@   ')
        print('  @@@@            ## Chess Tournament ##              @@@@  ')
        print(' @@@@@@           ######################             @@@@@@ ')
        print('@@@@@@@@                                            @@@@@@@@')
        print('|----------------------------------------------------------|')
        print('|                      Players Menu                        |')
        print('|----------------------------------------------------------|')
        print('|                                                          |')
        print("|                     [1] Add a nex player                 |")
        print("|                     [2] See all players                  |")
        print("|                     [0] Return principal menu            |")
        print('------------------------------------------------------------')



if __name__ == '__main__':
    menu().principal_menu()
    option_player = 999
    try:
        option_principal = int(input("Enter your option: "))
    except ValueError:
        print("Vous devez choisir un chiffre")
        option_principal = 999

    while option_principal != 0:
        if option_principal == 1:
            print()
            menu().players_menu()
            while option_player != 0 :
                try:
                    option_player = int(input("Enter your option: "))
                except ValueError:
                    print("Vous devez choisir un chiffre")
                    option_player = 999
                if option_player == 1:
                    player = cud().add_player()
                    print(player)
            menu().principal_menu()


        elif option_principal == 2:
            print(r'Option choisie : {} '.format(option_principal))
            menu().principal_menu()
        else:
            print("Option non existante")
            menu().principal_menu()



        try:
            option_principal = int(input("Enter your option: "))
        except ValueError:
            print("Vous devez choisir un chiffre")
            option_principal = 999

    print("\nBonne fin de journée et à bientôt")