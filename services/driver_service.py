import math

from RideBooking.services.driver_service_interface import DriverServiceInterface
from RideBooking.models.driver import Driver

class DriverService(DriverServiceInterface):
  driverDetails = {}
  def addDriver(self, id, name):
    driver = Driver()
    driver.setId(id)
    driver.setName(name)		

    self.__class__.driverDetails[id] = driver
    return driver

  def addLocation(self, id, location):
    #To-do:  exception handling
    driver = self.__class__.driverDetails.get(id)
    driver.setLocation(location)

    return driver

  def getNearestDriver(self, ride):
    least_distance = 99999
    nearest_driver = None
    rider = ride.rider

    for driver in self.__class__.driverDetails.values():
      distance = self._get_distance(rider, driver)
      print(driver.name, distance)
      if distance < least_distance:
        nearest_driver = driver
        least_distance = distance

    return nearest_driver

  def _get_distance(self, rider, driver):
    return math.sqrt( math.pow( (driver.location[1] - rider.location[1]), 2 ) + math.pow( (driver.location[0] - rider.location[0]), 2 ) )  