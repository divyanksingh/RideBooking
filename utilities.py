import math

def getDistance(from_location, to_location):
    return math.sqrt( math.pow( (to_location.longitude - from_location.longitude), 2 ) + math.pow( (to_location.latitude - from_location.latitude), 2 ) )