class Employee:
    def __init__(self, name):
        self.name = name
        self.state = Available(self)

    def assignOrder(self, order):
        self.state.assignOrder(order)

    def completeOrder(self, order):
        self.state.completeOrder(order)

class EmployeeState:
    def __init__(self, employee):
        self.employee = employee

    def assignOrder(self, order):
        return

    def completeOrder(self, order):
        return

class Available(EmployeeState):
    def assignOrder(self, order):
        self.employee.state = Busy(self.employee)
        print(f"{self.employee.name} is now busy and working on {order}.")

    def completeOrder(self, order):
        print(f"{self.employee.name} cannot complete order {order} as they are not working on it.")

class Busy(EmployeeState):
    def assignOrder(self, order):
        print(f"{self.employee.name} is unavailable at the moment.")

    def completeOrder(self, order):
        print(f"{self.employee.name} has completed order {order}.")
        self.employee.state = Available(self.employee)