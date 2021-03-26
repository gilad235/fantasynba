# accented_string = u'Málaga'
# # accented_string is of type 'unicode'
# import unidecode
# unaccented_string = unidecode.unidecode(accented_string)
# print(unaccented_string)
# # unaccented_string contains 'Malaga'and is of type 'str'
import pandas as pd
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot
import unidecode
# table = get_roster_stats("DEN", 2019, data_format='PER_GAME', playoffs=False)
# table.head()
import nba_py as nba
from nba_py import team
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
import random
from nba_py import player
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats import endpoints
from nba_py import game
import pandas as pd
import numpy as np
# nba.Scoreboard(month=12,day=25,year=2018)
# playerList = players.get_active_players() #519 players
# # # print(playerList)
# # # for i in range(1):
# # #     tempplayerdic = playerList[i]
# # #     tempid = tempplayerdic['id']
# # #     tempplayername = tempplayerdic['full_name']
# # #     tempdata = player.PlayerGameLogs(tempid).get_data_frames()[0] #default data 2018 season
# # #     path = r"C:\Users\gilad\PycharmProjects\nba\log-" + str(tempplayername) + "19-20.csv"
# # #     tempdata.to_csv(path, index=False)
# # df = player.get_player("Giannis Antetokounmpo",just_id=False)
# # print(df)

#Q2
def fins(s):
    #first rule will find a 2 letters palindrom, second rule will find 3 letters palindrom
    #all palindroms contain a 2 or letter palindrom
    lens = len(s)-1
    for i in range(lens):
        if (s[i]==s[i+1]) or (i+1<lens and s[i]==s[i+2]):
            return True
    return False

#Q3
def minR(arr,N):
    if sum(arr)<N:
        return False
    start = 0
    end = 0
    tempval = 0
    lens = len(arr)
    minlen = lens+1
    minend = 0
    minstart = 0
    while end <lens:
        while tempval<=N and end<lens:
            tempval+=arr[end]
            end+=1
        while tempval>N and start<lens:
            if (end-start)<minlen:
                minlen = end-start
                minend = end
                minstart = start
            tempval-=arr[start]
            start+=1
            while arr[start]==0:
                tempval -= arr[start]
                start += 1
                minlen = end - start
                minend = end
                minstart = start
    return (minstart,minend)
# a = [1,0,0,1,1,0,1,0]
# print(minR(a,3))


def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    lens = len(nums) - 1
    end = lens
    start = 0
    if lens == 0:
        return []
    if lens == 1:
        return [nums[0] ** 2]
    nums[0] = nums[0] ** 2
    nums[end] = nums[end] ** 2
    while start != end:
        if nums[start] < nums[end]:
            res.append(nums[end])
            end -= 1
            nums[end] = nums[end] ** 2
        else:
            res.append(nums[start])
            start += 1
            nums[start] = nums[start] ** 2
    res.append(nums[start])
    return (res[::-1] )

# print(sortedSquares([-4,-1,0,3,10]))

def luckyNumbers(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    temp = []
    lens = len(matrix) - 1
    for i in matrix:
        idx = i.index(min(i))
        larget = True
        for j in matrix:

            if (i[idx]) < (j[idx]):
                larget=False
                break
        if larget:
            temp.append(i[idx])
    return temp

trix = [[3,7,8],[9,11,13],[15,16,17]]
print(luckyNumbers(trix))

hm = {}
print(hm.get(1))