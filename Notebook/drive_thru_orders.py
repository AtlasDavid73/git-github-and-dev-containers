class Order:
    def __init__(self, id):
        self.id = id
class OrderStack:
    def __init__(self):
        self.stack = []
    def add_order(self, order):
        self.stack.append(order)
        print(f"Order {order.id} added to the stack.")
        
    def process_order(self):
        if self.stack:
            order = self.stack.pop()
            print(f"Processed {order.id}")
        else:
            print("No orders to process.")
    def current_stack(self):
        return [order.id for order in self.stack]
def main():
    order_stack = OrderStack()
    
    while True:
        print(f"\nCurrent Stack: {order_stack.current_stack()}")
        print("1: Add Order, 2: Process Order, 3: Show Current Stack, 4: Exit")
        choice = input("Enter your choice:")
        
        if choice == "1":
            order_id = input("enter Order Id: ")
            new_order = Order(order_id)
            order_stack.add_order(new_order)
        
        elif choice == "2":
            order_stack.process_order()
        
        elif choice == "3":
            print(f"Current Stack: {order_stack.current_stack()}")
            
        elif choice == "4":
            print("Exitiing system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

main()