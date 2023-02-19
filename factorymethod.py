class Employee:
    def __init__(self, name):
        self.name = name

    def assignOrder(self, order):
        pass

    def completeOrder(self, order):
        pass

class Manager(Employee):
    def assignOrder(self, order):
        order.assign_to(self)
        print(f"{self.name} assigned order #{order.id} to {order.assigned_to.name}")

    def completeOrder(self, order):
        order.complete()
        print(f"{self.name} marked order #{order.id} as complete")

class Cook(Employee):
    def assignOrder(self, order):
        order.assign_to(self)
        print(f"{self.name} assigned order #{order.id} to {order.assigned_to.name}")

    def completeOrder(self, order):
        order.complete()
        print(f"{self.name} marked order #{order.id} as complete")

class DeliveryPerson(Employee):
    def assignOrder(self, order):
        order.assign_to(self)
        print(f"{self.name} assigned order #{order.id} to {order.assigned_to.name}")

    def completeOrder(self, order):
        order.complete()
        print(f"{self.name} marked order #{order.id} as complete")


class EmployeeFactory:
    def create_employee(self, employee_type, name):
        if employee_type == "manager":
            return Manager(name)
        elif employee_type == "cook":
            return Cook(name)
        elif employee_type == "delivery_person":
            return DeliveryPerson(name)