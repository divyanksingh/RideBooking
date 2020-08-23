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

  def addLicense(self, id, license_number):
    driver = self.__class__.driverDetails[id]
    return driver.setLicenseNumber(license_number)


    