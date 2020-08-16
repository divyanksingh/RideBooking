import abc
class UserServiceInterface(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def addUser(self, id, name):
    pass

  @abc.abstractmethod
  def addLocation(self, id, location):
    pass