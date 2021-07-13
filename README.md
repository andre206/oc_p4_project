# Chess tournament management
***
The aim of this application is to manage offline chess tournaments.
You can create new tournaments, new players, add some players to a tournament,
start and stop rounds, add results, and at the end, add new ELO rank. 
You can also view ranking, for a tournament or general, view all tournaments
registered in the base, or the information of one tournament. 
You can at least modify elements of one player or one tournament, at any time.

## How to execute the application ?
***
At first, you have to install ___python3___ (I use the 3.9.6 version). 
You can find on the official site 
[Python](https://www.python.org/downloads/) your version for 
Windows /Linux/ Mac.

Then you need to install a new environment for running the application, 
containing the packages included in the file 
[requirement.txt](https://github.com/maticha84/oc_p4_project/blob/master/requirements.txt)
.To do this, please follow the instructions below:

Create a virtual environment at the root of the project, using the command
python -m venv env. Then, activate this environment : 

- _Windows_: __venv\Scripts\activate.bat__
- _Linux_ & _Mac_: __source venv/Scripts/activate__

After that, install the requirement.txt with using this command : 
__pip install -r requirements.txt__

Now you can start the application by running the main.py file: __py main.py__


## Help for this application
***
To read some help about this application, you can use the command : 
__py -m pydoc -b__ at the root of the project. It will open a browser page
with the html help. it retrieves the docstrings present in the modules, 
describing the functioning of the different classes, methods and functions.

You can also retreive this documentation here :
[docstrings html](https://github.com/maticha84/oc_p4_project/tree/master/docstrings_html)


## Flake8 report
***

You can find a flake8 report here : 
[report](https://github.com/maticha84/oc_p4_project/tree/master/flake8_rapport)

You can also do this command to make a new flake report, according the 
specifications : 

__flake8 --format html --htmldir flake8_rapport 
--max-line-length 119 main.py controllers models views__


## Presentation of this application
***

At first, when you start the application, you have a main menu : 

1. [Tournaments management](#tournaments-management)
2. [Players management](#players-management)
3. [Reports](#reports)
4. [Exit](#exit)

For interact with the application, you just have to enter 
your menu choice.
### Tournaments management
***

In this part of the application, you can manage a tournament.

1. Add new tournament

in this part, you can configure a new tournament, with all options 
like name, place of tournament, date start and stop, control time
(blitz, bullet or quick), number of even players, number of rounds

2. View all tournaments
  
this way displays all tournaments known in the base. 

3. Modify on tournament
  
This option allows you to modify elements of tournament

- add players

- starting round

- ending round and add results

- view results of tournament

4. Return to main menu

### Players management
***
In this part of the application, you can manage the players

1. add players

Allow you to add new players. You will be able to fill in the surname, 
first name, date of birth, gender and the ELO rating already known to 
the user. If this ranking does not exist (new player), by default the
application will give a ranking of 1000.

2. view all players

this way displays all players known in the base.

3. Modify one player

This option allows you to modify elements of player
* surname
* first name
* date of birth
* gender
* ELO rank
4. Return to main menu

### Reports
***

### Exit
***