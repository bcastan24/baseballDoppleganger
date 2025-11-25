class Player:
    def __init__(self, data, name):
      self.data = data
      self.war = self.make_list()
      self.name = name

    def make_list(self):
      summed = self.data.groupby('Age')['WAR'].sum()
      aw = summed.to_list()
      return aw

    def first_age(self):
      return self.ages()[0]

    def first_war(self):
      return self.war[0]

    def get_name(self):
      return self.name

    def career_len(self):
      return len(self.war)

    def ages(self):
        s = self.data['Age'].to_list()
        s.sort()
        return s

    def get_list(self):
        return self.war