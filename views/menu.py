# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

# Create the menu
menu = ConsoleMenu("Title", "Subtitle")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
#menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
#function_item = FunctionItem("Call a Python function", input, ["Enter an input"])
name = FunctionItem("Add a name",input('name : '))
# A CommandItem runs a console command
#command_item = CommandItem("Run a console command", "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
player_menu = SelectionMenu(["Surname", "Date of birth", "sex"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
new_player = SubmenuItem("Create a new player", player_menu, menu)
#player_name = SubmenuItem("name", name, player_menu)



# Once we're done creating them, we just add the items to the menu
#menu.append_item(menu_item)
#menu.append_item(function_item)
#menu.append_item(command_item)
menu.append_item(new_player)
player_menu.append_item(name)


# Finally, we call show to show the menu and allow the user to interact
menu.show()