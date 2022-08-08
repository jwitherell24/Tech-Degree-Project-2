from constants import TEAMS
from constants import PLAYERS
import copy
import dm


teams = TEAMS.copy()
players = PLAYERS.copy()
cleaned_players = []
num_players_team = int(len(players) / len(teams))
panthers = []
bandits = []
warriors = []
experienced = []
inexperienced = []


dm.main()
