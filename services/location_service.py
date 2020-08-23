from RideBooking.services.location_service_interface import LocationServiceInterface
from RideBooking.models.location import Location

class LocationService(LocationServiceInterface):
  def addLocation(self, latitude, longitude):
    location = Location(latitude, longitude)
    return location


