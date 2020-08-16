from RideBooking.services.ride_service_interface import RideServiceInterface
from RideBooking.models.ride import Ride

class RideService(RideServiceInterface):
  rideDetails = {}
  def addRide(self, id, rider):
    ride = Ride()
    ride.setId(id)
    ride.setRider(rider)		

    self.__class__.rideDetails[id] = ride
    return ride

  def addDriver(self, id, driver):
    #To-do:  exception handling
    ride = self.__class__.rideDetails.get(id)
    ride.setDriver(driver)

    return ride