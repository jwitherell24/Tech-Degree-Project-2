from constants import TEAMS
from constants import PLAYERS
import copy
import random


teams = TEAMS.copy()
players = PLAYERS.copy()
cleaned_players = []
num_players_team = len(players) / len(teams)
panthers = []
bandits = []
warriors = []
experienced = []
inexperienced = []

def clean_data(players):
    for player in players:
        fixed = {}
        fixed["name"] = player["name"]
        fixed["guardians"] = player["guardians"].split(" and ")
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        fixed["height"] = int(player["height"].split(" ")[0])
        cleaned_players.append(fixed)
        for key, value in fixed.items():
            if key == "name":
                print("\n{}: {}".format(key, value))
            else:
                print("{}: {}".format(key, value))

def balance_teams(cleaned_players):
    equal_experience = num_players_team / 2
    for player in cleaned_players:
        if player["experience"] == True:
            experienced.append(player)
        else:
            inexperienced.append(player





def main():
    clean_data(players)
    balance_teams(cleaned_players)
#if __name__ == "__main__":
