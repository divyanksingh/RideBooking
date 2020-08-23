class Cab(object):
  def __init__(self, id, reg_no):
    self.id = id
    self.reg_no = reg_no
    self.location = None
    self.driver = None
    self.status = None

  def setId(self,id):
    self.id = id

  def getId(self):
    return self.id

  def setRegNo(self, reg_no):
    self.reg_no = reg_no

  def getRegNo(self):
    return self.reg_no

  def setLocation(self, location):
    self.location = location

  def getLocation(self):
    return self.location

  def setDriver(self, driver):
    self.driver = driver

  def getDriver(self):
    return self.driver

  def setStatus(self, status):
    self.status = status

  def getStatus(self):
    return self.status