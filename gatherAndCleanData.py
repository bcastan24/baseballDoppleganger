import pandas as pd

data = pd.read_csv('name_age_war.csv')
data.dropna(inplace=True)
data['WAR'] = data['WAR'].round(1)
