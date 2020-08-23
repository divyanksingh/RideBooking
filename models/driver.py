from RideBooking.models.user_base import UserBase

class Driver(UserBase):
  def __init__(self):
    super().__init__()
    self.license_number = None

  def setLicenseNumber(self, license_number):
    self.license_number = license_number

  def getLicenseNumber(self):
    return self.license_number