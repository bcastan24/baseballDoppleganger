import mysql.connector
import gatherAndCleanData as gcd

def addPlayersToDB():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="baseballdatabase"
    )
    myCursor = db.cursor()
    data = gcd.getData()
    for i in range(len(data)):
        id = data["IDfg"].iloc[i]
        name = data["Name"].iloc[i]
        age = data["Age"].iloc[i]
        ops = data["opsPlus"].iloc[i]
        wRCPlus = data["wRCPlus"].iloc[i]
        kPerc = data["kPerc"].iloc[i]
        WAR = data["WAR"].iloc[i]
        PA = data["PA"].iloc[i]
        BBPerc = data["BBPerc"].iloc[i]
        HR = data["HR"].iloc[i]

