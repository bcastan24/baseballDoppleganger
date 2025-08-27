import mysql.connector
from pybaseball import playerid_lookup
from pybaseball import batting_stats

playerId = None
firstLayerPlayers = []

def firstLayer(firstName:str, lastName:str):
    #make first and last name lowercase for player lookup
    first = firstName.lower()
    last = lastName.lower()
    #lookup player
    playerLookup = playerid_lookup(last, first)

    #get the year they first played and their last year playing
    firstYear = int(playerLookup['mlb_played_first'].iloc[0])
    lastYear = int(playerLookup['mlb_played_last'].iloc[0])
    #if they are a current player change last year to 2024 since 2025 stats arent available yet
    if lastYear == 2025:
        lastYear = 2024
    #get the stats for the seasons that they played
    seasonStats = batting_stats(firstYear, lastYear)
    #make the player name one string and capitalize first letters of first and last name
    playerName = first.capitalize() + " " + last.capitalize()
    #get the players stats
    playerStats = seasonStats[seasonStats['Name'] == playerName]
    playerId = playerStats['IDfg'].iloc[0]
    selectedColumns = ["IDfg", "Age", "OPS", "wRC+", "WAR"]
    playerStats = playerStats[selectedColumns]
    careerLen = lastYear - firstYear
    for i in range(careerLen):
        age = int(playerStats['Age'].iloc[i])
        if age == 28 or age == 24:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="baseballdatabase"
            )
            myCursor = db.cursor()
            myCursor.execute("SELECT * FROM first_level")
            for x in myCursor:
                #checking if it is not the same player, if they are the same age, if their ops are within .05 of each other, if their wRC+ are withing 10 of each other, and if their WAR are withing 0.5 of each other
                if int(x[0]) != playerId and int(x[5]) == age and float(x[1])-.051 < float(x[1]) < float(x[1])+.051 and int(x[2])-11 < int(x[2]) < int(x[2])+11 and float(x[3])-.51 < float(x[3]) < float(x[3])+.51:
                    firstLayerPlayers.append(int(x[0]))
    return firstLayerPlayers
