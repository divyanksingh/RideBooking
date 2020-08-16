class UserController(object):
  def __init__(self, userService):
    self.userService = userService
  
  def addUser(self, id, name):
    return self.userService.addUser(id, name)

  def addLocation(self, id, location):
    return self.userService.addLocation(id, location)