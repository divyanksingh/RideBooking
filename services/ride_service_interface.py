import abc
class RideServiceInterface(metaclass=abc.ABCMeta):
  
  @abc.abstractmethod
  def addRide(self,id,customer, cab, status):
    pass

  @abc.abstractmethod
  def updateCab(self,id,cab):
    pass
  
  @abc.abstractmethod
  def updateStatus(self,id,status):
    pass

  @abc.abstractmethod
  def getRidesByStatus(self,status):
    pass