import abc
class DriverServiceInterface(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def addDriver(self, id, name):
    pass

  @abc.abstractmethod
  def addLocation(self, id, location):
    pass

  @abc.abstractmethod
  def getNearestDriver(self, rider):
    pass