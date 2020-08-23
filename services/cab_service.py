from RideBooking.services.cab_service_interface import CabServiceInterface
from RideBooking.models.cab import Cab

class CabService(CabServiceInterface):

  cabDetails = {}

  def addCab(self, id, reg_no):
    cab = Cab(id, reg_no)
    self.__class__.cabDetails[id] = cab
    return cab

  def updateCabLocation(self, id, location):
    cab = self.__class__.cabDetails[id]
    cab.setLocation(location)
    return cab

  def updateCabDriver(self, id, driver):
    cab = self.__class__.cabDetails[id]
    cab.setDriver(driver)
    return cab

  def updateCabStatus(self, id, status):
    cab = self.__class__.cabDetails[id]
    cab.setStatus(status)
    return cab

  def getCabByStatus(self, status):
    cabs_by_status = []
    # Check
    for cab in self.__class__.cabDetails.values():
      print(cab.status)
      if cab.getStatus() == status:
        cabs_by_status.append(cab)

    return cabs_by_status