from datetime import datetime, timedelta
from games import *
import numpy as np
import pandas as pd
"""need to update player 9 cat csv
need to edit new rookies data
need to offer avg stats based on this year not only on last year"""

today = datetime.today().strftime("%Y-%m-%d")


defcats = ["FG%","3P","FT%","TRB","AST","STL","BLK","TOV","PTS"]
players_df = pd.read_excel("Players 9 Cat - 2020.xlsx", sheet_name="Per Game", skiprows=4)
new_df= players_df

season_schduele = pd.read_csv(r"C:\Users\gilad\PycharmProjects\nba\season2021.csv")
season_schduele = season_schduele.drop_duplicates()

from sportsreference.nba.teams import *

# teams = Teams()
# houston_schedule = Schedule('HOU')
# houston_schedule.head()

from nba_api.stats.static import teams
teams = teams.get_teams()
agg_dic = {}
for team in teams:
    agg_dic[team["abbreviation"]]=team["full_name"]


def team_has_game(player_team,date):
    """
    :param player_team:
    :param date:
    :return: true if the team has a game
    """
    if not season_schduele[season_schduele.DATE == date][
        agg_dic[player_team.values[0].upper()] == season_schduele.VISITOR].empty\
            or not season_schduele[season_schduele.DATE == date][
        agg_dic[player_team.values[0].upper()] == season_schduele.HOME].empty:
        return True
    return False
def predict_stats(player_data):
    """

    :param player_data:
    :return: returns avg stats, can be changed to a learning algorithem to predict better data
    """
    return player_data.filter(items=["FG","FGA","3P","FT","FTA","TRB","AST","STL","BLK","TOV","PTS"])


def precit_vec(myteam,oppteam,startdate,enddate,curdate=today,cats=defcats, season_schduele=season_schduele):
    column_names = ["FG","FGA","3P","FT","FTA","TRB","AST","STL","BLK","TOV","PTS"]
    row_names = ['1', '2']

    a = np.zeros(shape=(2, 11))
    all_stats = pd.DataFrame(a, columns=column_names, index=row_names)

    for i in range(2):
        if i == 0:
            team = myteam
        else:
            team = oppteam
        for player in team:
            dataexis = True

            if str(player).endswith("jr."):
                player_name=' '.join(str(player).split(' ')[:-1])
            else:
                player_name = str(player)
            """need to edit this to updated teams"""
            player_team = players_df[players_df.Player == player_name]["Tm"]
            path = r"C:\Users\gilad\PycharmProjects\nba\log-" + player + "20-21.csv"

            """can get a diffrent avg"""
            player_st = players_df[players_df.Player == player_name]
            players_predict_stats = player_st.filter(items=["FG","FGA","3P","FT","FTA","TRB","AST","STL","BLK","TOV","PTS"])

            tempdate = startdate
            try:
                player_data = pd.read_csv(path)
            except:
                dataexis = False
                print("no data for " + player)
            while (tempdate <= enddate):
                if team_has_game(player_team,tempdate):
                    if (dataexis and player_data.isin([tempdate]).any().any()):

                        all_stats.values[i] += player_data[player_data.DATE == tempdate].filter(items=["FG","FGA","3P","FT","FTA","TRB","AST","STL","BLK","TOV","PTS"]).values[0]
                    else:
                        all_stats.values[i] += players_predict_stats.values[0]
                tempdate = datetime.strptime(tempdate, '%Y-%m-%d')
                tempdate += timedelta(days=1)
                tempdate = tempdate.strftime('%Y-%m-%d')

    try:
        all_stats["FG%"] = all_stats["FG"]/all_stats["FGA"]
        all_stats["FT%"] = all_stats["FT"] / all_stats["FTA"]
        del all_stats["FG"],all_stats["FGA"],all_stats["FT"],all_stats["FTA"]
    except:
        print("no attempts tried")

    print(all_stats)


my_team = ["Giannis Antetokounmpo","Rudy Gobert","Ben Simmons","Tomáš Satoranský","Kelly Oubre jr.",
           "Mike Conley","Draymond Green","Thaddeus Young","DeMar DeRozan","Mitchell Robinson"]
my_bugs_players = ["De'Anthony Melton","Joe Ingles"]
mili_team = ["Jaylen Brown","Coby White","Kemba Walker","LeBron James","Larry Nance"
    ,"Bam Adebayo","Mason Plumlee", "DeAndre Jordan","Kristaps Porziņģis"]
guy_team = ["Seth Curry","Luka Dončić","Danny Green","Caris LeVert","Eric Bledsoe","Steven Adams","Marcus Smart",
            "Zion Williamson","Donovan Mitchell","Tyler Herro","Andrew Wiggins","Clint Capela"]
gal_team = ["Malik Beasley","Malcolm Brogdon","Michael Porter","Richaun Holmes","Domantas Sabonis","Nikola Jokić","Jimmy Butler","P.J. Washington"]
dauber_team = ["Kevin Durant","Russell Westbrook", "Dejounte Murray","Eric Gordon","Victor Oladipo","Caris LeVert",
               "DeAndre Jordan","Kyle Anderson","Kyle Lowry","Jusuf Nurkić","Terry Rozier","Bogdan Bogdanović","Enes Kanter"]
kasher = """Trae Young
Terrence Ross
D'Angelo Russell
Bojan Bogdanović
Rui Hachimura
Julius Randle
Al Horford
De'Aaron Fox
Joel Embiid
Derrick Rose
Shai Gilgeous-Alexander""".split("\n")
lerer = """Damian Lillard
Duncan Robinson
Collin Sexton
Harrison Barnes
Tobias Harris
Nikola Vučević
Jarrett Allen
Jonas Valančiūnas
Khris Middleton
Evan Fournier""".split("\n")
eilon_team = """Jrue Holiday
CJ McCollum
OG Anunoby
Joe Harris
Dennis Schröder
Kyle Kuzma
Miles Bridges
John Collins
Anthony Davis
Monte Morris
Kyrie Irving
Lauri Markkanen""".split("\n")
nitzan_team = """Lonzo Ball
Bradley Beal
Norman Powell
Serge Ibaka
LaMarcus Aldridge
Ivica Zubac
Deandre Ayton
Brook Lopez
Fred VanVleet
James Harden""".split("\n")
truman = """Donte DiVincenzo
Devin Booker
Cam Reddish
Danilo Gallinari
Jerami Grant
Jayson Tatum
Robert Covington
Myles Turner
Zach LaVine
Devonte' Graham
Jeremy Lamb
Dāvis Bertāns""".split("\n")
# get_players_game_log(my_team+guy_team)
precit_vec(my_team,guy_team,"2021-03-22","2021-03-28")
# predicter(my_team,mili_team,"2021-03-15","2021-03-21")