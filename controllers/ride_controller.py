class RideController(object):
  def __init__(self, rideService):
    self.rideService = rideService
  
  def addRide(self, id, rider):
    return self.rideService.addRide(id, rider)

  def addDriver(self, id, driver):
    return self.rideService.addDriver(id, driver)