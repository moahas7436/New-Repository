class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = "pending"

    def editOrder(self, new_order_details):
        print(f"Order {self.order_id} has been edited with new details: {new_order_details}")
        self.status = "edited"

    def cancelOrder(self):
        print(f"Order {self.order_id} has been canceled")
        self.status = "canceled"

    def accept(self, visitor):
        visitor.visitOrder(self)
        
class OrderVisitor:
    def visitOrder(self, order):
        return

class EditOrderVisitor(OrderVisitor):
    def visitOrder(self, order):
        order.editOrder()
        
class CancelOrderVisitor(OrderVisitor):
    def visitOrder(self, order):
        order.cancelOrder()