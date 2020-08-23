import abc
class CustomerServiceInterface(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def addCustomer(self, id, name):
    pass

  @abc.abstractmethod
  def addLocation(self, id, location):
    pass