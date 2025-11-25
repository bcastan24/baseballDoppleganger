import numpy as np
def war_similarity(w1, w2):
    n = min(len(w1), len(w2))
    return sum((abs(w2[i] - w1[i])/w1[i])*100 for i in range(n)) / n

def get_doppleganger(players, name):
  p = players[0]
  my_dict = {}
  for player in players:
    if player.get_name() == name:
      p = player
  p1 = p.first_war() + 1
  p2 = p.first_war() - 1
  potential = []
  for player in players:
    if p2 < player.first_war() < p1 and player.get_name() != p.get_name():
      potential.append(player)
  for q in potential:
    if q.career_len() > p.career_len():
        w1 = p.get_wars()
        w2 = q.get_wars()
        acc = 100 - float(war_similarity(w1, w2))
        if acc > 80.0:
            my_dict[q.get_name()] = acc

  return my_dict