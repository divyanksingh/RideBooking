import abc
class RideServiceInterface(metaclass=abc.ABCMeta):
  
  @abc.abstractmethod
  def addRide(self,id,rider):
    pass

  @abc.abstractmethod
  def addDriver(self, id, driver):
    pass