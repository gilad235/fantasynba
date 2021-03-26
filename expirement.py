import pandas as pd
import numpy as np
df = pd.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
                  index=['mouse', 'rabbit'],
                  columns=['one', 'two', 'three'])
a= df.filter(items=['three','one'])
# print(a)
# print(a.values[0])
print(' '.join("Kelly Oubre jr.".split(' ')[:-1]))


# print(agg_dic)
def predicter(myteam,oppteam,startdate,enddate,curdate=today,cats=defcats, season_schduele=season_schduele):
    a = np.zeros(shape=(2, 9))
    mat = pd.DataFrame(a, columns=cats)
    mat.set_index(cats)

    FG0,FGA0,FT0,FTA0,FG1,FGA1,FT1,FTA1 = 0,0,0,0,0,0,0,0

    for cat in cats:
        # if cat=="FG%":
        #     """i can add FG,FGA to the code and than devide"""
        #     pass
        # # elif cat == "FT%":
        # #     pass
        # else:
        for i in range(2):
            if i==0:
                team = myteam
            else:
                team=oppteam
            for player in team:
                dataexis = True
                """can get a diffrent avg"""
                avr = players_df[players_df.Player == str(player)][cat]
                tempdate = startdate
                """need to edit this to updated teams"""
                player_team = players_df[players_df.Player == str(player)]["Tm"]
                path = r"C:\Users\gilad\PycharmProjects\nba\log-" + player + "20-21.csv"
                try:
                    player_data = pd.read_csv(path)
                except:
                    dataexis = False
                    print("no data for "+player)
                while (tempdate<curdate and tempdate<=enddate and dataexis):
                    """for every date that already accured the date adds
                                         myteam stat to the final mat"""
                    if not season_schduele[season_schduele.DATE == tempdate][agg_dic[player_team.values[0].upper()] == season_schduele.VISITOR].empty\
                            or not season_schduele[season_schduele.DATE == tempdate][agg_dic[player_team.values[0].upper()] == season_schduele.HOME].empty:
                        if cat=="FG%":
                            if i==0:
                                FG0 += player_data[player_data.DATE == tempdate]["FG"].values[0]
                                FGA0 += player_data[player_data.DATE == tempdate]["FGA"].values[0]
                            else:
                                FG1 += player_data[player_data.DATE == tempdate]["FG"].values[0]
                                FGA1 += player_data[player_data.DATE == tempdate]["FGA"].values[0]
                        elif cat=="FT%":
                            if i==0:
                                FT0 += player_data[player_data.DATE == tempdate]["FT"].values[0]
                                FTA0 += player_data[player_data.DATE == tempdate]["FTA"].values[0]
                            else:
                                FT1 += player_data[player_data.DATE == tempdate]["FT"].values[0]
                                FTA1 += player_data[player_data.DATE == tempdate]["FTA"].values[0]
                        else:
                            mat[cat][i] += player_data[player_data.DATE == tempdate][cat].values[0]

                    tempdate = datetime.strptime(tempdate, '%Y-%m-%d')
                    tempdate += timedelta(days=1)
                    tempdate = tempdate.strftime('%Y-%m-%d')

                while ((tempdate>=curdate or dataexis==False) and tempdate<=enddate) :
                    """adds the prediction for every game that
                     havent accured yeat"""
                    if not season_schduele[season_schduele.DATE == tempdate][
                        agg_dic[player_team.values[0].upper()] == season_schduele.VISITOR].empty \
                            or not season_schduele[season_schduele.DATE == tempdate][
                        agg_dic[player_team.values[0].upper()] == season_schduele.HOME].empty:
                        if cat=="FG%":
                            if i==0:
                                FG0 += players_df[players_df.Player == str(player)]["FG"].values[0]
                                FGA0 += players_df[players_df.Player == str(player)]["FGA"].values[0]
                            else:
                                FG1 += players_df[players_df.Player == str(player)]["FG"].values[0]
                                FGA1 += players_df[players_df.Player == str(player)]["FGA"].values[0]
                        elif cat=="FT%":
                            if i==0:
                                FT0 += players_df[players_df.Player == str(player)]["FT"].values[0]
                                FTA0 += players_df[players_df.Player == str(player)]["FTA"].values[0]
                            else:
                                FT1 += players_df[players_df.Player == str(player)]["FT"].values[0]
                                FTA1 += players_df[players_df.Player == str(player)]["FTA"].values[0]
                        else:
                            mat[cat][i] += avr

                    tempdate = datetime.strptime(tempdate, '%Y-%m-%d')
                    tempdate += timedelta(days=1)
                    tempdate = tempdate.strftime('%Y-%m-%d')


    if FGA0!=0:
        mat["FG%"][0] = FG0/FGA0
    if FGA1 != 0:
        mat["FG%"][1] = FG1 / FGA1
    if FTA0!=0:
        mat["FT%"][0] = FT0/FTA0
    if FTA1!=0:
        mat["FT%"][1] = FT1/FTA1
    print(mat)

