from RideBooking.models.user_base import UserBase

class Customer(UserBase):
  def __init__(self):
    super().__init__()

    self.location = None

  def setLocation(self, location):
    self.location = location

  def getLocation(self):
    return self.location