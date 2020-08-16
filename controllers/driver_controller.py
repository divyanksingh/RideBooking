class DriverController(object):
  def __init__(self, driverService):
    self.driverService = driverService
  
  def addDriver(self, id, name):
    return self.driverService.addDriver(id, name)

  def addLocation(self, id, location):
    return self.driverService.addLocation(id, location)

  def findDriver(self, ride):
    return self.driverService.getNearestDriver(ride)