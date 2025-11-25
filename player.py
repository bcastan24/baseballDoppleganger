class Player:
    def __init__(self, data, name):
      self.data = data
      self.age_and_war = self.make_dict()
      self.name = name

    def make_dict(self):
      summed = self.data.groupby('Age')['WAR'].sum()
      aw = summed.to_dict()
      return aw

    def first_age(self):
      return min(self.age_and_war.keys())

    def first_war(self):
      return self.age_and_war.get(self.first_age())

    def get_war(self, age):
      return self.age_and_war[age]

    def get_name(self):
      return self.name

    def career_len(self):
      return len(self.ages())

    def ages(self):
      return self.age_and_war.keys()