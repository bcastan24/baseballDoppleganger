from pybaseball import batting_stats
import pandas as pd
import os

def getData():
    if os.path.exists("batting.csv") == False:
        batting = batting_stats(1980, 2002, qual=200)
        batting.to_csv("batting1.csv", index=False)
        batting = batting_stats(2003, 2024, qual=200)
        batting.to_csv("batting2.csv", index=False)
        df = pd.concat(map(pd.read_csv, ['batting1.csv', 'batting2.csv']), ignore_index=True)
        dfFiltered = df.groupby("IDfg").filter(lambda x: x.shape[0] > 7)
        selectedColumns = ["IDfg", "Name", "Season","Age", "OPS", "wRC+", "K%", "WAR", "PA", "BB%", "HR"]
        dfFiltered = dfFiltered[selectedColumns]
        dfFiltered.to_csv("batting.csv", index=False)
        return dfFiltered
    else:
        data = pd.read_csv("batting.csv")
        return data