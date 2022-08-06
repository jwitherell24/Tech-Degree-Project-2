from constants import TEAMS
from constants import PLAYERS
import copy

teams = TEAMS.copy()
players = PLAYERS.copy()
cleaned_players = []

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
                print("\n{}:{}".format(key, value))
            else:
                print("{}:{}".format(key, value))

def main():
    clean_data(players)

#if __name__ == "__main__":
