class Ride(object):
  def __init__(self):
    self.id = None
    self.rider = None
    self.driver = None

  def setId(self, id):
    self.id = id

  def getId(self):
    return self.id

  def setRider(self, rider):
    self.rider = rider

  def getRider(self):
    return self.rider

  def setDriver(self, driver):
    self.driver = driver

  def getDriver(self):
    return self.driver