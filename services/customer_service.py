from RideBooking.services.customer_service_interface import CustomerServiceInterface
from RideBooking.models.customer import Customer

class CustomerService(CustomerServiceInterface):
  customerDetails = {}
  def addCustomer(self, id, name):
    customer = Customer()
    customer.setId(id)
    customer.setName(name)		

    self.__class__.customerDetails[id] = customer
    return customer

  def addLocation(self, id, location):
    #To-do:  exception handling
    customer = self.__class__.customerDetails.get(id)
    customer.setLocation(location)

    return customer