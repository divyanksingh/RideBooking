import math

def getDistance(from_location, to_location):
    return math.sqrt( math.pow( (to_location.getLongitude() - from_location.getLongitude()), 2 ) + math.pow( (to_location.getLatitude() - from_location.getLatitude()), 2 ) )