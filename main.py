import sys
sys.path.append('/Users/ds/Learning/coding_exercises/')

from RideBooking.controllers.user_controller import UserController
from RideBooking.controllers.driver_controller import DriverController
from RideBooking.controllers.ride_controller import RideController

from RideBooking.services.ride_service import RideService
from RideBooking.services.user_service import UserService
from RideBooking.services.driver_service import DriverService

userController = UserController(UserService())
driverController = DriverController(DriverService())
rideController = RideController(RideService())


user1 = userController.addUser('user1','pawan')
userController.addLocation('user1', (2, 6))

driver1 = driverController.addDriver('driver1', 'abhinav')
driver2 = driverController.addDriver('driver2', 'gyan')
driver3 = driverController.addDriver('driver3', 'ds')
driver4 = driverController.addDriver('driver4', 'nishant')

driverController.addLocation('driver1', (4, 2))
driverController.addLocation('driver2', (10, 9))
driverController.addLocation('driver3', (0, 3))
driverController.addLocation('driver4', (1, 20))

ride1 = rideController.addRide('ride1', user1)
assigned_driver = driverController.findDriver(ride1)
rideController.addDriver('ride1', assigned_driver)

print (ride1.rider.name, ride1.driver.name)