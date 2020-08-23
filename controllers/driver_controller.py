class DriverController(object):
  def __init__(self, driverService):
    self.driverService = driverService
  
  def addDriver(self, id, name):
    return self.driverService.addDriver(id, name)

  def addLicense(self, id, license_number):
    return self.driverService.addLicense(id, license_number)