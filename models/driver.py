from RideBooking.models.user import User

class Driver(User):
  def __init__(self):
    super(Driver).__init__()
    self.is_driver = True
