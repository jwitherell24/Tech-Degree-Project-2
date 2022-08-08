from constants import TEAMS
from constants import PLAYERS
import copy

teams = TEAMS.copy()
players = PLAYERS.copy()
cleaned_players = []
num_players_team = int(len(players) / len(teams))
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

        if __name__ == "__main__":
            for key, value in fixed.items():
                if key == "name":
                    print("\n{}: {}".format(key, value))
                else:
                    print("{}: {}".format(key, value))

def equal_team(team):
    while True:
        if len(team) == num_players_team:
            break
        elif len(team) < (num_players_team / 2):
            player = experienced.pop()
            team.append(player)
            continue
        elif len(team) >= (num_players_team / 2):
            player = inexperienced.pop()
            team.append(player)
            continue

def balance_teams(cleaned_players):
    for player in cleaned_players:
        if player["experience"] == True:
            experienced.append(player)

        else:
            inexperienced.append(player)

    equal_team(panthers)
    equal_team(bandits)
    equal_team(warriors)

def main_menu():
    print("""BASKETBALL TEAM STATS TOOL

    ---- MENU ----

    Here are your choices:
        A) Display Team Stats
        B) Quit\n""")

    option_1 = input("Please enter an option:  ")

    while True:
        if option_1.lower() == "b":
            print("Thank you for browsing.")
            break
        if option_1.lower() != "a" and "b":
            option_1= input("That is an invalid value, please try again. (A or B)  ")
            continue
        if option_1.lower() == "a":
            print("""\nTeams:
            A) Panthers
            B) Bandits
            C) Warriors\n""")

            option_2 = input("Please pick a team.  ")
            while True:
                if option_2.lower() == "a":
                    print(f"""\nTeam: {TEAMS[0]} Stats
------------------------""")
                    team_menu(panthers)
                    break
                if option_2.lower() == "b":
                    print(f"""\nTeam: {TEAMS[1]} Stats
------------------------""")
                    team_menu(bandits)
                    break
                if option_2.lower() == "c":
                    print(f"""\nTeam: {TEAMS[2]} Stats
------------------------""")
                    team_menu(warriors)
                    break
                if option_2.lower() != "a" and "b" and "c":
                    option_2 = input("That is an invalid value, please try again. (A, B, or C)  ")
                    continue

def team_menu(team):
    print(f"Total Players: {len(team)}")

def main():
    clean_data(players)
    balance_teams(cleaned_players)
    main_menu()

if __name__ == "__main__":
    main()
