import pandas as pd
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot
from basketball_reference_scraper.box_scores import get_box_scores
# from predicting import *
import unidecode
"""https://github.com/vishaalagartha/basketball_reference_scraper
the code from the scraper"""
# players_df = pd.read_excel("Players 9 Cat - 2020.xlsx",sheet_name="Per Game",skiprows=4)
# players = players_df.Player.tolist()
# dfbooker = get_game_logs("Devin Booker", "2019-10-10", "2020-10-10", playoffs=False)
# dfbooker.head()
start = False
# d = get_box_scores('2020-01-06', 'DEN', 'ATL')
# list(d['DEN'].columns)
# n = d['DEN']['PLAYER'][0]
# # print(d)
# # print("Nikola Jokić"=="Nikola Jokić")
# temp = get_game_logs(n, "2019-10-10", "2020-10-10", playoffs=False)
# path = r"C:\Users\gilad\PycharmProjects\nba\log-" + str(n) + "19-20.csv"
# temp.to_csv(path, index=False)
def get_players_game_log(players):
    """
    scrapes the game log for the list of players and creates a CSV for each
    :param players: players to scrape data
    :return: void
    """
    for player in players:
# TODO: create cache to download only missing parts of the data.
# TODO: can make easy cache to get last dates or cpmlex for all missing data

        try:
            temp = get_game_logs(player, "2020-10-10", "2021-10-10", playoffs=False)
            path = r"C:\Users\gilad\PycharmProjects\nba\log-"+str(player)+"20-21.csv"
            temp.to_csv(path,index=False)
        except:
            print("no data for " + player)

# from basketball_reference_scraper.seasons import get_schedule, get_standings
# curseas = get_schedule(2021, playoffs=False)
# curseas.head()
# curseas.to_csv(r"C:\Users\gilad\PycharmProjects\nba\season2021.csv",index=False)

# get_players_game_log(my_team+mili_team)
# get_players_game_log(["Kelly Oubre jr."])
