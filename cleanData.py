import pandas as pd
from player import Player
def clean_data():
    data = pd.read_csv('name_age_war.csv')
    data.dropna(inplace=True)
    data['WAR'] = data['WAR'].round(1)

    players = []
    for name, group in data.groupby('Name'):
      players.append(Player(group, name))
    return players