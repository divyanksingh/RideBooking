class RideController(object):
  def __init__(self, rideService, statusService):
    self.rideService = rideService
    self.allStatus = statusService.getAllStatus()
  
  def addRide(self, id, customer, cab):
    return self.rideService.addRide(id, customer, cab, self.allStatus.BOOKED)

  def startRide(self, id):
    return self.rideService.updateStatus(id, self.allStatus.IN_PROGRESS)

  def completeRide(self, id):
    return self.rideService.updateStatus(id, self.allStatus.COMPLETED)

  def cancelRide(self, id):
    return self.rideService.updateStatus(id, self.allStatus.CANCELLED)
    
  def findInProgressCount(self):

    inProgressRides = self.rideService.getRidesByStatus(self.allStatus.IN_PROGRESS)
    return len(inProgressRides)