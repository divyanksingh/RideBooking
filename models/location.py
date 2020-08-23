class Location(object):
  def __init__(self, latitude, longitude):
    self.latitude = latitude
    self.longitude = longitude

  #Why
  def setLatitude(self, latitude):
    self.latitude = latitude

  def getLatitude(self):
    return self.latitude

  #Why
  def setLongitude(self, longitude):
    self.longitude = longitude

  def getLongitude(self):
    return self.longitude