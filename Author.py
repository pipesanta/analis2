class Author:
  def __init__(self, name, institution, article):
    self.name = name
    self.institution = institution
    self.article = article

  def print(self):
    print(self.name + self.institution + self.article)