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
        id = int(id)
        name = data["Name"].iloc[i]
        name = str(name)
        age = data["Age"].iloc[i]
        age = int(age)
        ops = data["OPS"].iloc[i]
        ops = float(ops)
        wRCPlus = data["wRC+"].iloc[i]
        wRCPlus = int(wRCPlus)
        kPerc = data["K%"].iloc[i]
        kPerc = float(kPerc) * 100.0
        WAR = data["WAR"].iloc[i]
        WAR = float(WAR)
        PA = data["PA"].iloc[i]
        PA = int(PA)
        BBPerc = data["BB%"].iloc[i]
        BBPerc = float(BBPerc) * 100.0
        HR = data["HR"].iloc[i]
        HR = int(HR)

        if age == 19:
            myCursor.execute("INSERT INTO age_19 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 20:
            myCursor.execute("INSERT INTO age_20 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 21:
            myCursor.execute("INSERT INTO age_21 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 22:
            myCursor.execute("INSERT INTO age_22 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 23:
            myCursor.execute("INSERT INTO age_23 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 24:
            myCursor.execute("INSERT INTO age_24 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            myCursor.execute("INSERT INTO first_level (id, opsPlus, wRCPlus, WAR, name, age) VALUES (%s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, WAR, name, age))
            db.commit()
        elif age == 25:
            myCursor.execute("INSERT INTO age_25 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 26:
            myCursor.execute("INSERT INTO age_26 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 27:
            myCursor.execute("INSERT INTO age_27 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 28:
            myCursor.execute("INSERT INTO age_28 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            myCursor.execute("INSERT INTO first_level (id, opsPlus, wRCPlus, WAR, name, age) VALUES (%s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, WAR, name, age))
            db.commit()
        elif age == 29:
            myCursor.execute("INSERT INTO age_29 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 30:
            myCursor.execute("INSERT INTO age_30 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 31:
            myCursor.execute("INSERT INTO age_31 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 32:
            myCursor.execute("INSERT INTO age_32 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 33:
            myCursor.execute("INSERT INTO age_33 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 34:
            myCursor.execute("INSERT INTO age_34 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 35:
            myCursor.execute("INSERT INTO age_35 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 36:
            myCursor.execute("INSERT INTO age_36 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 37:
            myCursor.execute("INSERT INTO age_37 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 38:
            myCursor.execute("INSERT INTO age_38 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 39:
            myCursor.execute("INSERT INTO age_39 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 40:
            myCursor.execute("INSERT INTO age_40 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 41:
            myCursor.execute("INSERT INTO age_41 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 42:
            myCursor.execute("INSERT INTO age_42 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 43:
            myCursor.execute("INSERT INTO age_43 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 44:
            myCursor.execute("INSERT INTO age_44 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
        elif age == 45:
            myCursor.execute("INSERT INTO age_45 (id, opsPlus, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, ops, wRCPlus, kPerc, WAR, PA, BBPerc, HR, name))
            db.commit()
