import abc
class DriverServiceInterface(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def addDriver(self, id, name):
    pass

  @abc.abstractmethod
  def addLicense(self, id, license_number):
    pass
