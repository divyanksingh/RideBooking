class User(object):
  def __init__(self):
    self.id = None
    self.name = None
    self.location = (0, 0)
    self.is_driver = False

  def setId(self,id):
    self.id = id

  def getId(self):
    return self.id

  def setName(self, name):
    self.name = name

  def getName(self):
    return self.name

  def setLocation(self, location):
    self.location = location

  def getLocation(self):
    return self.location