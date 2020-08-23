import abc
class LocationServiceInterface(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def addLocation(self, lat, long):
    pass

