from enum import Enum

class Status(Enum):
  AVAILABLE = 0
  BOOKED = 1
  IN_PROGRESS = 2
  COMPLETED = 3
  CANCELLED = 4
  OFF_DUTY = 5

  