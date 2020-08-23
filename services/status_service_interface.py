import abc
class StatusServiceInterface(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def getAllStatus(self):
    pass