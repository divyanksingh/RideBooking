from RideBooking.services.ride_service_interface import RideServiceInterface
from RideBooking.models.ride import Ride

class RideService(RideServiceInterface):
  rideDetails = {}

  def addRide(self, id, customer, cab, status):
    ride = Ride(id, customer, cab, status)
    self.__class__.rideDetails[id] = ride
    return ride

  def updateCab(self, id, cab):
    #To-do:  exception handling
    ride = self.__class__.rideDetails.get(id)
    ride.setCab(cab)

    return ride

  def updateStatus(self, id, status):
    #To-do:  exception handling
    ride = self.__class__.rideDetails.get(id)
    ride.setStatus(status)

    return ride

  def getRidesByStatus(self, status):
    rides_by_status = []
    # Check
    for ride in self.__class__.rideDetails.values():
      print(ride.status)
      if ride.getStatus() == status:
        rides_by_status.append(ride)

    return rides_by_status