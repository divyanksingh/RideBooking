class LocationController(object):
  def __init__(self, locationService):
    self.locationService = locationService
  
  def addLocation(self, latitude, longitude):
    return self.locationService.addLocation(latitude, longitude)
