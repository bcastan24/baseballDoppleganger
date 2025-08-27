import database as db
import filtering as ft

#I commented this out because I only needed to run it once, now all the player data is in the right tables
#db.addPlayersToDB()

firstName = input("What is the players first name?: ")
lastName = input("What is the players last name?: ")
players = ft.firstLayer(firstName, lastName)
for x in players:
    print(x)
