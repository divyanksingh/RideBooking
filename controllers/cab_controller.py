from RideBooking.utilities import getDistance

class CabController(object):
  def __init__(self, cabService, statusService):
    self.cabService = cabService
    self.allStatus = statusService.getAllStatus()
  
  def addCab(self, id, reg_no):
    return self.cabService.addCab(id, reg_no)

  def updateLocation(self, id, location):
    return self.cabService.updateCabLocation(id, location)

  def updateDriver(self, id, driver):
    return self.cabService.updateCabDriver(id, driver)

  def markAvailable(self, id):
    return self.cabService.updateCabStatus(id, self.allStatus.AVAILABLE)

  def markOffDuty(self, id):
    return self.cabService.updateCabStatus(id, self.allStatus.OFF_DUTY)

  def markBooked(self, id):
    return self.cabService.updateCabStatus(id, self.allStatus.BOOKED)

  def findCabForRide(self, location):
    availableCabs = self.cabService.getCabByStatus(self.allStatus.AVAILABLE)
    leastDistance = 99999
    nearestCab = None

    for cab in availableCabs:
      distance = getDistance(location, cab.getLocation())
      if distance < leastDistance:
        nearestCab = cab
        leastDistance = distance

    return nearestCab
