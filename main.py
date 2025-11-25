import cleanData as cd
import doppleganger as dp

players = cd.clean_data()
print(dp.get_doppleganger(players, 'Juan Soto'))
