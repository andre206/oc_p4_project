# Chess tournament management

The aim of this application is to manage offline chess tournaments.
You can create new tournaments, new players, add some players to a tournament,
start and stop rounds, add results, and at the end, add new ELO rank. 
You can also view ranking, for a tournament or general, view all tournaments
registered in the base, or the information of one tournament. 
You can at least modify elements of one player or one tournament, at any time.

----
## How to execute the application ?

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

----

## Help for this application

To read some help about this application, you can use the command : 
__py -m pydoc -b__ at the root of the project. It will open a browser page
with the html help. it retrieves the docstrings present in the modules, 
describing the functioning of the different classes, methods and functions.

You can also retreive this documentation here :
[docstrings html](https://github.com/maticha84/oc_p4_project/tree/master/docstrings_html)

----
## Flake8 report

You can find a flake8 report here : 
[report](https://github.com/maticha84/oc_p4_project/tree/master/flake8_rapport)

You can also do this command to make a new flake report, according the 
specifications : 

__flake8 --format html --htmldir flake8_rapport 
--max-line-length 119 main.py controllers models views__

----
## Presentation of this application
