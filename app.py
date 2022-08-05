from constants import TEAMS
from constants import PLAYERS


def cleaned_data(PLAYERS):
    cleaned_players = []
    for player in PLAYERS:
        fixed = {}
        fixed["name"] = player["name"]
        fixed["guardians"] = player["guardians"]
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        fixed["height"] = int(player["height"].split(" ")[0])
        cleaned_players.append(fixed)

    for key, value in fixed.items():
        print("{}: {}".format(key, value))

def balance_teams(PLAYERS, TEAMS):
    cleaned_data(PLAYERS)
    while True:
        Panthers = []
        Bandits = []
        Warriors = []
        for player in cleaned_data(PLAYERS):
            if len(Panthers) < 6:
                Panthers.append(player)
                continue
            if len(Bandits) < 6:
                Bandits.append(player)
                continue
            if len(Warriors) < 6:
                Warriors.append(player)
                continue
            else:
                break

        return Panthers, Bandits, Warriors

cleaned_data(PLAYERS)
#print(balance_teams(PLAYERS, TEAMS))

#if __name__ == "__main__":
