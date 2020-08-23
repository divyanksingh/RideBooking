class CustomerController(object):
  def __init__(self, customerService):
    self.customerService = customerService
  
  def addCustomer(self, id, name):
    return self.customerService.addCustomer(id, name)

  def addLocation(self, id, location):
    return self.customerService.addLocation(id, location)