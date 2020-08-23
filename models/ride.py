class Ride(object):
  def __init__(self, id, customer, cab, status):
    self.id = id
    self.customer = customer
    self.cab = cab
    self.status = status

  def setId(self, id):
    self.id = id

  def getId(self):
    return self.id

  def setCustomer(self, customer):
    self.customer = customer

  def getCustomer(self):
    return self.customer

  def setCab(self, cab):
    self.cab = cab

  def getCab(self):
    return self.cab

  def setStatus(self, status):
    self.status = status

  def getStatus(self):
    return self.status
