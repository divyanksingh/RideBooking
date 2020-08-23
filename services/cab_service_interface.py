import abc
class CabServiceInterface(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def addCab(self, id, reg_no):
    pass

  @abc.abstractmethod
  def updateCabLocation(self, id, location):
    pass

  @abc.abstractmethod
  def updateCabDriver(self, id, driver):
    pass

  @abc.abstractmethod
  def updateCabStatus(self, id, status):
    pass