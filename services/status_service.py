from RideBooking.services.status_service_interface import StatusServiceInterface
from RideBooking.models.status import Status

class StatusService(StatusServiceInterface):

  def getAllStatus(self):
    return Status
