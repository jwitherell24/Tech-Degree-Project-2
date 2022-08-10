from constants import TEAMS
from constants import PLAYERS

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
        if player["experience"] is True:
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
        if option_1.lower() < "a":
            option_1 = input("\nThat is an invalid value, please try again. (A or B)  ")
            continue
        if option_1.lower() > "b":
            option_1 = input("That is an invalid value, please try again. (A or B)  ")
            continue
        elif option_1.lower() == "b":
            print("\nThank you for browsing.")
            break
        elif option_1.lower() == "a":
            print("""\nTeams:
            A) Panthers
            B) Bandits
            C) Warriors\n""")

            team_menu()
            break


def team_menu():
    option_2 = input("Please pick a team.  ")

    while True:
        if option_2.lower() < "a":
            option_2 = input("That is an invalid value, please try again. (A, B, or C)  ")
            continue
        if option_2.lower() > "c":
            option_2 = input("That is an invalid value, please try again. (A, B, or C)  ")
            continue
        elif option_2.lower() == "a":
            print(f"""\nTeam: {TEAMS[0]} Stats
    {"-" * 25}""")
            team_stats(panthers)
            break
        elif option_2.lower() == "b":
            print(f"""\nTeam: {TEAMS[1]} Stats
{"-" * 25}""")
            team_stats(bandits)
            break
        elif option_2.lower() == "c":
            print(f"""\nTeam: {TEAMS[2]} Stats
{"-" * 25}""")
            team_stats(warriors)
            break


def team_stats(team):
    player_names = []
    experienced = []
    inexperienced = []
    player_heights = []
    guardians = []

    for player in team:
        player_names.append(player["name"])
        if player["experience"] is True:
            experienced.append(player)
        if player["experience"] is False:
            inexperienced.append(player)
        player_heights.append(player["height"])
        guardians.append(player["guardians"])

    print(f"""Total Players: {len(team)}
Total Experienced: {len(experienced)}
Total Inexperienced: {len(inexperienced)}
Average Height: {int(sum(player_heights) / num_players_team)}\n
Players:
{", ".join(player_names)}
\nGuardians:""")
    enum_guardians = []
    for i, guardian in enumerate(guardians):
        enum_guardians += guardians[i]
    print(", ".join(enum_guardians))

    print("\nPress any key to go back to main menu.")
    back_to_menu = input("> ")

    main_menu()


def main():
    clean_data(players)
    balance_teams(cleaned_players)
    main_menu()

if __name__ == "__main__":
    main()
