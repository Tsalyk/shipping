import order_data, random
orders_id = []

class Order:
    """
    Creating an order
    """

    def __init__(self, user_name: str, city=None,
                 postoffice=None, items=None):
        global orders_id

        location = order_data.Location(city, postoffice)

        rand_id = random.randint(100000000, 999999999)
        while rand_id in orders_id:
            rand_id = random.randint(100000000, 999999999)
        orders_id.append(rand_id)

        self.orderId = rand_id
        self.user_name = user_name
        self.items = items
        self.city = location.city
        self.postoffice = location.postoffice
        self.vehicle = None

        print(f"Your order number is {self.orderId}.")

    def calculateAmount(self) -> int:
        """
        Calculate amount of order
        """
        return sum([item.price for item in self.items])

    def assignVehicle(self, vehicle: order_data.Vehicle):
        self.vehicle = vehicle

    def __str__(self):
        return (f"Your order #{self.orderId} is sent to {self.city}. "
                f"Total price: {self.calculateAmount()} UAH.")


class LogisticSystem:
    """
    Processing an order
    """

    def __init__(self, vehicles: list):
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        self.orders.append(order)

        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                order.vehicle = vehicle.vehicleNo
                vehicle.isAvailable = False
                break
        else:
            print("There is no available vehicle to deliver an order.")

    def trackOrder(self, orderId: int) -> str:
        order = list(filter(lambda element: element.orderId == orderId,
                            self.orders))

        if len(order) != 0 and order[0].vehicle:
            return order[0].__str__()
        else:
            return "No such order."


# test
if __name__ == "__main__":
    vehicles = [order_data.Vehicle(1), order_data.Vehicle(2)]
    logSystem = LogisticSystem(vehicles)

    my_items = [order_data.Item('book',110), order_data.Item('chupachups',44)]
    my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
    logSystem.placeOrder(my_order)
    print(logSystem.trackOrder(my_order.orderId))


    my_items2 = [order_data.Item('flowers',11), order_data.Item('shoes',153), order_data.Item('helicopter',0.33)]
    my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    logSystem.placeOrder(my_order2)
    print(logSystem.trackOrder(my_order2.orderId))


    my_items3 = [order_data.Item('coat',61.8), order_data.Item('shower',5070), order_data.Item('rollers',700)]
    my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    logSystem.placeOrder(my_order3)
    print(logSystem.trackOrder(my_order3.orderId))