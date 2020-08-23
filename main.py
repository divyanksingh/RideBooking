import sys
sys.path.append('/Users/ds/Learning/coding_exercises/')

from RideBooking.controllers.customer_controller import CustomerController
from RideBooking.controllers.cab_controller import CabController
from RideBooking.controllers.location_controller import LocationController
from RideBooking.controllers.driver_controller import DriverController
from RideBooking.controllers.ride_controller import RideController

from RideBooking.services.ride_service import RideService
from RideBooking.services.customer_service import CustomerService
from RideBooking.services.cab_service import CabService
from RideBooking.services.location_service import LocationService
from RideBooking.services.driver_service import DriverService
from RideBooking.services.status_service import StatusService

customerController = CustomerController(CustomerService())
cabController = CabController(CabService(), StatusService())
locationController = LocationController(LocationService())
driverController = DriverController(DriverService())
rideController = RideController(RideService(), StatusService())


customer1 = customerController.addCustomer('cust1','pawan')
customer2 = customerController.addCustomer('cust2','arpit')
customerController.addLocation('cust1', locationController.addLocation(2, 6))
customerController.addLocation('cust2', locationController.addLocation(9, 3))

driver1 = driverController.addDriver('driver1', 'abhinav')
driver2 = driverController.addDriver('driver2', 'gyan')
driver3 = driverController.addDriver('driver3', 'ds')
driver4 = driverController.addDriver('driver4', 'nishant')

cab1 = cabController.addCab('cab1', 'KA01HN5532')
cab2 = cabController.addCab('cab2', 'KA01HN5502')
cab3 = cabController.addCab('cab3', 'KA01HN5432')
cab4 = cabController.addCab('cab4', 'KA01HN5512')

cabController.markAvailable('cab1')
cabController.markAvailable('cab2')
cabController.markAvailable('cab3')
cabController.markOffDuty('cab4')

cabController.updateLocation('cab1', locationController.addLocation(2, 6))
cabController.updateLocation('cab2', locationController.addLocation(12, 26))
cabController.updateLocation('cab3', locationController.addLocation(25, 36))
cabController.updateLocation('cab4', locationController.addLocation(20, 61))


cabForCust1 = cabController.findCabForRide(customer1.location)

ride1 = rideController.addRide('ride1', customer1, cabForCust1)

#Check
cabController.markBooked(cabForCust1.getId())

rideController.startRide('ride1')

cabForCust2 = cabController.findCabForRide(customer2.location)

ride2 = rideController.addRide('ride2', customer2, cabForCust2)

cabController.markBooked(cabForCust2.getId())

rideController.startRide('ride2')

inProgressCount = rideController.findInProgressCount()

print (ride1.customer.name, ride1.cab.reg_no, ride2.customer.name, ride2.cab.reg_no, inProgressCount)