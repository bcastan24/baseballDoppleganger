class Player:
    def __init__(self, data, name):
      self.data = data
      self.ages, self.war = self.__make_list()
      self.name = name

    def __make_list(self):
      summed = self.data.groupby('Age')['WAR'].sum().sort_index()
      ages = list(summed.index)
      wars = list(summed.values)
      if wars[0] < 0.0:
          wars.pop(0)
          ages.pop(0)
      return ages, wars

    def first_age(self):
      return self.ages[0]

    def first_war(self):
      return self.war[0]

    def get_name(self):
      return self.name

    def career_len(self):
      return len(self.war)


    def get_wars(self):
        return self.war

    def get_ages(self):
        return self.ages