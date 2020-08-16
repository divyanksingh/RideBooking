from RideBooking.services.user_service_interface import UserServiceInterface
from RideBooking.models.user import User

class UserService(UserServiceInterface):
  userDetails = {}
  def addUser(self, id, name):
    user = User()
    user.setId(id)
    user.setName(name)		

    self.__class__.userDetails[id] = user
    return user

  def addLocation(self, id, location):
    #To-do:  exception handling
    user = self.__class__.userDetails.get(id)
    user.setLocation(location)

    return user